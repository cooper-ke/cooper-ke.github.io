import dominate
from dominate.tags import *
import csv

class Course:
    def __init__(self, name, tutors, resources):
        self.name = name # String, name of the course
        self.tutors = tutors # List of Tutors
        self.resources = resources # List of Resources

class Resource:
    def __init__(self, name, link):
        self.name = name # Name of the resource
        self.link = link # Link to the resouce

class Tutor:
    def __init__(self, name, email, phone_number):
        self.name = name # String
        self.email = email # String
        self.phone_number = phone_number # String
      
# Grab CSV data to create website
courses = []
with open("DS5110ExampleFormResponses.csv") as responses_file:
    responses = csv.reader(responses_file)
    for response in responses:
        # Add a tutor
        if response[0] == "Self":
            added_tutor = False
            for course in courses:
                if course.name == response[4]:
                    course.tutors.append(Tutor(response[1], response[2], response[3]))
                    added_tutor = True
                    break
            if added_tutor == False:
                courses.append(Course(response[4],
                                      [Tutor(response[1], response[2], response[3])], []))
        # Add a material
        elif response[0] == "Material":
            added_resource = False
            for course in courses:
                if course.name == response[6]:
                    course.resources.append(Resource("Resource", response[7]))
                    added_resource = True
                    break
            if added_resource == False:
                courses.append(Course(response[6], [],
                                      [Resource("Resource", response[7])]))

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
        h3("Resources:")
        with div(cls="resource_list").add(ul()):
            for resource in course.resources:
                li(a(resource.name, href=resource.link))
        a("Return to index", href="index.html")
    with open(f"{course.name}.html", "w") as f:
        f.write(str(doc))