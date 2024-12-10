import dominate
from dominate.tags import *
import pandas as pd

class Course:
    def __init__(self, name, tutors, resources):
        self.name = name # String, name of the course
        self.tutors = tutors # List of Tutors
        self.resources = resources # List of Resources

class Tutor:
    def __init__(self, name, email, phone_number, can_tutor, availability):
        self.name = name # String
        self.email = email # String
        self.phone_number = phone_number # String
        self.can_tutor = can_tutor # Boolean
        self.availability = availability # String

class Resource:
    def __init__(self, name, link):
        self.name = name # Name of the resource
        self.link = link # Link to the resouce

# Grab CSV data to create website
df = pd.read_csv("responses.csv")
# Crate an empty dataframe to show how it generates
# Comment out this line to show responses
#df = pd.DataFrame(    columns=["student_id","name","email","class_id","class_name","credits","department","can_tutor","tutoring_availability","note_id","note_title","content","notebook_id","title","file"])

# Generate courses from the dataframe
courses = []
unique_courses = df["class_id"].unique()
for course in unique_courses:
    courses.append(Course(course.upper(), [], []))

# For each course, grab the relevant tutors and resources
for index, row in df.iterrows():
    for course in courses:
        if course.name == row["class_id"].upper():
            can_tutor = (row["can_tutor"] == "Yes")
            course.tutors.append(
                Tutor(row["name"], row["email"], "617-777-7777", can_tutor, row["tutoring_availability"])
            )
            # If we have a resouce uploaded, add that as well
            if type(row["note_id"]) == float and row["note_id"] > 0:
                course.resources.append(
                    Resource(row["note_title"], row["content"].rsplit('/', 1)[-1])
                )
            if type(row["notebook_id"]) == float and row["notebook_id"] > 0:
                course.resources.append(
                    Resource(row["title"], row["file"].rsplit('/', 1)[-1])
                )
            break

# Generate index.html
doc = dominate.document(title="Class index")
with doc.head:
    link(rel="icon", href="favicon.png")
    link(rel="stylesheet", href="style.css")
with doc:
    h1("Welcome!")
    p("Below is a list of courses that are supported by this program.")
    h2("Courses")
    with div(id="resources").add(ul()):
        for course in courses:
            li(a(course.name, href=f"{course.name}.html")) 
with open(f"index.html", "w") as f:
    f.write(str(doc))

# Generate course pages
for course in courses:
    doc = dominate.document(title=course.name)
    with doc.head:
        link(rel="icon", href="favicon.png")
        link(rel="stylesheet", href="style.css")
    with doc:
        h1(course.name)
        h3("Tutors:")
        with div(cls="resource_list").add(ul()):
            for tutor in course.tutors:
                li(tutor.name)
                with div().add(ul()):
                    li("Email: " + tutor.email)
                    li("Phone: " + tutor.phone_number)
                    if tutor.can_tutor:
                        li("Availability: " + tutor.availability)
                    else:
                        li("This person is not available to tutor at this time")
        br()
        h3("Resources:")
        with div(cls="resource_list").add(ul()):
            for resource in course.resources:
                li(a(resource.name, href=resource.link))
        a("Return to index", href="index.html")
    with open(f"{course.name}.html", "w", encoding="utf-8") as f:
        f.write(str(doc))