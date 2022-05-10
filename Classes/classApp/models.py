from django.db import models


# Creating the form structure for the app
class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField()
    instructor = models.CharField(max_length=30)
    duration = models.DecimalField(decimal_places=3, max_digits=10000)

    # Adding a class manager
    objects = models.Manager()

    def __str__(self):
        return self.title

# Creating variables from the class objects and assigning values to them
classVar = djangoClasses()
x = classVar.title
y = classVar.courseNumber
z = classVar.instructor
