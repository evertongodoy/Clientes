from django.db import models

# Classes que desrevem o modelo do negocio

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()

    class Meta:
        db_table = 'person' # define your custom name  https://stackoverflow.com/questions/32657766/how-to-control-table-names-created-by-django-migrate

    def __str__(self):
    	return self.first_name + ' ' + self.last_name
