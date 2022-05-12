from django.db import models


# Creating the form structure for the app
class djangoClasses(models.Model):
    title = models.CharField(max_length=50)
    courseNumber = models.IntegerField(default=0)
    instructor = models.CharField(max_length=30)
    duration = models.FloatField(default=0)

    # Adding a class manager
    objects = models.Manager()

    def __str__(self):
        return self.title


# Creating variables from the class objects and assigning values to them
object1 = djangoClasses(title="SomeObject", courseNumber=1, instructor="Billy", duration=2.5)
object1.save()

object2 = djangoClasses(title="anotherObject", courseNumber=2, instructor="BillyBob", duration=60)
object2.save()

object3 = djangoClasses(title="thisObject", courseNumber=3, instructor="Joe", duration=30)
object3.save()

