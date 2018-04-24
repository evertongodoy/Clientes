from django.db import models

# Classes que desrevem o modelo do negocio
# upload_to = Caso voce queira salvar em uma  pasta especial dentro da pasta de medias

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    class Meta:
        db_table = 'person' # define your custom name  https://stackoverflow.com/questions/32657766/how-to-control-table-names-created-by-django-migrate

    def __str__(self):
    	return self.first_name + ' ' + self.last_name
