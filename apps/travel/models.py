from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

class userManager(models.Manager):
    def basic_validator(self, postData):
        errors = []
        if len(postData['name']) < 3:
            errors.append("Name should be more than 3 characters")
        if len(postData['userName']) < 3:
            errors.append("User Name should be more than 3 characters")
        if len(postData['password']) < 8:
            errors.append("password should be more than 8 characters")
        if postData['password']!=postData['confirmPW']:
            errors.append("password must match")
        return (errors)
    
class user(models.Model):
    name = models.CharField(max_length=255)
    Username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = userManager()

class TravelManager(models.Manager):
    def travel_validation(self,postData):
        errors =[]
        if len(postData['destination'])<=0:
            errors.append("Destination place cant be empty")   
        if len(postData['description'])<=0:
            errors.append("Description cant be empty")
        if 'start_date' in postData:
           
            if str(date.today()) > str(postData['start_date']):
                errors.append("Please input a valid Date. Note: Start time can not be in the past.")
        else:
            errors.append("Start date cant be empty.")
        if 'end_date' in postData:
           
            if str(date.today()) > postData['end_date']:
                errors.append("Please input a valid Date. Note: End date must be in the future")
            if postData['start_date'] > postData['end_date']:
                errors.append("Travel Date From can not be in the future of Travel Date To")
        else:
            errors.append("End date cant be empty.")
        return errors

class Travel(models.Model):
    destination = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    start= models.DateField()
    end= models.DateField()
    creator= models.ForeignKey(user, related_name= "planner")
    books = models.ManyToManyField(user, related_name="Travels")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = TravelManager()