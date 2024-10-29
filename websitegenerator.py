import dominate
from dominate.tags import *

class Course:
    def __init__(self, name, tutors, resources):
        self.name = name
        self.tutors = tutors
        self.resources = resources

class Resource:
    def __init__(self, name, link):
        self.name = name
        self.link = link

courses = [
    Course("DS5110", ["John Smith", "Jane Doe"], [Resource("Khan Academy – Python", "https://www.khanacademy.org/computing/intro-to-python-fundamentals")])
    ]

# Generate index.html
doc = dominate.document(title="Class index")
with doc:
    h1("Courses")
    with div(id="resources").add(ul()):
        for course in courses:
            li(a(course.name, href=f"{course.name}.html")) 
with open(f"index.html", "w") as f:
    f.write(str(doc))

# Generate course pages
for course in courses:
    doc = dominate.document(title=course.name)
    with doc:
        h1(course.name)
        p("Tutors:")
        with div(id="tutors").add(ul()):
            for i in course.tutors:
                li(i)
        p("Resources:")
        with div(id="resources").add(ul()):
            for i in course.resources:
                li(a(i.name, href=i.link))
        a("Return to index", href="index.html")
    with open(f"{course.name}.html", "w") as f:
        f.write(str(doc))