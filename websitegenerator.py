import dominate
from dominate.tags import *

class Course:
    def __init__(self, name, tutors, resources):
        self.name = name # String, name of the course
        self.tutors = tutors # List of strings, names of tutors
        self.resources = resources # List of Resource classes

class Resource:
    def __init__(self, name, link):
        self.name = name # Name of the resource
        self.link = link # Link to the resouce

courses = [
    Course("DS5110", ["John Smith", "Jane Doe"], [Resource("Khan Academy Python", "https://www.khanacademy.org/computing/intro-to-python-fundamentals")])
    ]

# Generate index.html
doc = dominate.document(title="Class index")
with doc.head:
    link(rel="icon", href="favicon.png")
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
    with doc:
        h1(course.name)
        p("Tutors:")
        with div(id="tutors").add(ul()):
            for tutor in course.tutors:
                li(tutor)
        p("Resources:")
        with div(id="resources").add(ul()):
            for resource in course.resources:
                li(a(resource.name, href=resource.link))
        a("Return to index", href="index.html")
    with open(f"{course.name}.html", "w") as f:
        f.write(str(doc))