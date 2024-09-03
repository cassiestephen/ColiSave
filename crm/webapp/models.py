from django.db import models

import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras.layers import Dense, Dropout
from sklearn.preprocessing import MinMaxScaler


import joblib

# Create your models here.
SURGERY = (
    ('no', 'No'),
    ('yes', 'Yes'),
)

SURGICAL_LESION = (
    ('no', 'No'),
    ('yes', 'Yes'),
)

EXTREMITY_TEMP = (
    ('cold', 'Cold'),
    ('cool', 'Cool'),
    ('normal', 'Normal'),
    ('warm', 'Warm'),
)

P_PULSE = (
    ('increased', 'Increased'),
    ('normal', 'Normal'),
    ('reduced', 'Reduced'),
    ('absent', 'Absent'),
)

MUC_MEM = (
    ('normal_pink', 'Normal Pink'),
    ('bright_pink', 'Bright Pink'),
    ('pale_pink', 'Pale Pink'),
    ('pale_cyanotic', 'Pale Cyanotic'),
    ('bright_red', 'Bright Red'),
    ('dark_cyanotic', 'Dark Cyanotic'),
)

REFILL_TIME = (
    ('less_3_sec', 'Less than 3 sec'),
    ('more_3_sec', 'More than 3sec'),
    ('3_sec', '3_sec'),
)

PAIN = (
    ('alert', 'Alert'),
    ('depressed', 'Depressed'),
    ('mild_pain', 'Mild Pain'),
    ('extreme_pain', 'Extreme Pain'),
    ('severe_pain', 'Severe Pain'),
)

PERISTALISIS = (
    ('hypermotile', 'Hypermotile'),
    ('normal', 'Normal'),
    ('hypomotile', 'Hypomotile'),
    ('absent', 'Absent'),
)


DISTENTION = (
    ('none', 'None'),
    ('slight', 'Slight'),
    ('moderate', 'Moderate'),
    ('severe', 'Severe'),
)

AGE = (
    ('adult', 'Adult'),
    ('young', 'Young'),
)



class Client(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True) # auto adds date to new Client object
    name = models.CharField(max_length=100, default='')
    owner = models.CharField(max_length=100, default='')
    phone = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')
    surgery = models.CharField(max_length=100, choices=SURGERY, default='yes/no')
    age = models.CharField(max_length=100, choices=AGE, default='yes/no')
    rectal_temp = models.FloatField()
    pulse = models.FloatField()
    respiratory_rate = models.FloatField()
    temp_of_extremities = models.CharField(max_length=100, choices=EXTREMITY_TEMP, default='')
    peripheral_pulse = models.CharField(max_length=100, choices=P_PULSE, default='')
    mucous_membrane = models.CharField(max_length=100, choices=MUC_MEM, default='')
    capillary_refill_time = models.CharField(max_length=100, choices=REFILL_TIME, default='')
    pain = models.CharField(max_length=100, choices=PAIN, default='')
    peristalsis = models.CharField(max_length=100, choices=PERISTALISIS, default='')
    abdominal_distention = models.CharField(max_length=100, choices=DISTENTION, default='')
    packed_cell_volume = models.PositiveIntegerField()
    total_protein = models.FloatField()
    surgical_lesion = models.CharField(max_length=100, choices=SURGICAL_LESION, default='yes/no')
    lesion_1 = models.PositiveIntegerField()
    lesion_2 = models.PositiveIntegerField()
    predictions = models.CharField(max_length=100, blank=True)
    

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model/ml_colic_model.joblib')
        df = [[self.rectal_temp, self.pulse, self.respiratory_rate, self.packed_cell_volume, 
               self.total_protein, self.lesion_1, self.lesion_2,
               int(self.surgery == 'no'),
               int(self.surgery == 'yes'),
               int(self.age == 'adult'),
               int(self.age == 'young'),
               int(self.temp_of_extremities == 'cold'),
               int(self.temp_of_extremities == 'cool'),
               int(self.temp_of_extremities == 'normal'),
               int(self.temp_of_extremities == 'warm'),
               int(self.peripheral_pulse == 'absent'),
               int(self.peripheral_pulse == 'increased'),
               int(self.peripheral_pulse == 'normal'),
               int(self.peripheral_pulse == 'reduced'),
               int(self.mucous_membrane == 'bright_pink'),
               int(self.mucous_membrane == 'bright_red'),
               int(self.mucous_membrane == 'dark_cyanotic'),
               int(self.mucous_membrane == 'normal_pink'),
               int(self.mucous_membrane == 'pale_cyanotic'),
               int(self.mucous_membrane == 'pale_pink'),
               int(self.capillary_refill_time == '3_sec'),
               int(self.capillary_refill_time == 'less_3_sec'),
               int(self.capillary_refill_time == 'more_3_sec'),

               int(self.pain == 'alert'),
               int(self.pain == 'depressed'),
               int(self.pain == 'extreme_pain'),
               int(self.pain == 'mild_pain'),
               int(self.pain == 'severe_pain'),

               int(self.peristalsis == 'absent'),
               int(self.peristalsis == 'hypermotile'),
               int(self.peristalsis == 'hypomotile'),
               int(self.peristalsis == 'normal'),

               int(self.abdominal_distention == 'moderate'),
               int(self.abdominal_distention == 'none'),
               int(self.abdominal_distention == 'severe'),
               int(self.abdominal_distention == 'slight'),

               int(self.surgical_lesion == 'no'),
               int(self.surgical_lesion == 'yes'),]]
        # generate predicitons upon creation of horse
        self.predictions = ml_model.predict(df)
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.name + " " + self.name
