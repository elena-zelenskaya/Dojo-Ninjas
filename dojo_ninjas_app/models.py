from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    desc = models.TextField(default="old_dojo")
    amount_of_ninjas = models.IntegerField(default=0)
    def __repr__(self):
        return f"Id: {self.id}, name: {self.name}, city: {self.city}, {self.state}"
    def delete_dojo(self, number):
        dojo_to_delete = Dojo.objects.get(id = number)
        dojo_to_delete.delete()

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo_id = models.ForeignKey(Dojo, related_name = 'ninjas', on_delete = models.CASCADE)
    def __repr__(self):
        return f"Id: {self.id}, name: {self.first_name} {self.last_name}, dojo: {self.dojo_id.name} from {self.dojo_id.city}, {self.dojo_id.state}"
