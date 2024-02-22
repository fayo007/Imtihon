from rest_framework import serializers
from main import models

class StaffCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Staff
        fields = ['id','first_name','last_name']
      

        