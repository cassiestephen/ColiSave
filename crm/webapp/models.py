from django.db import models

# Create your models here.


class Client(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True) # auto adds date to new Client object
    name = models.CharField(max_length=100, default='')
    owner = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    surgery = models.CharField(max_length=20, default='yes/no')
    age = models.CharField(max_length=200, default='')
    rectal_temp = models.CharField(max_length=100, default='')
    pulse = models.CharField(max_length=100, default='')
    respiratory_rate = models.CharField(max_length=100, default='')
    temp_of_extremities = models.CharField(max_length=100, default='')
    peripheral_pulse = models.CharField(max_length=100, default='')
    mucous_membrane = models.CharField(max_length=100, default='')
    capillary_refill_time = models.CharField(max_length=100, default='')
    pain = models.CharField(max_length=100, default='')
    peristalsis = models.CharField(max_length=100, default='')
    abdominal_distention = models.CharField(max_length=100, default='')
    packed_cell_volume = models.CharField(max_length=100, default='')
    total_protein = models.CharField(max_length=100, default='')
    surgical_lesion = models.CharField(max_length=100, default='yes/no')
    lesion_1 = models.CharField(max_length=100, default='yes/no')
    lesion_2 = models.CharField(max_length=100, default='yes/no')

    


    def __str__(self):
        return self.first_name + " " + self.last_name
