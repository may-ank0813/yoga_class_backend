from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Enroll(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.IntegerField()
    email = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    @classmethod
    def create(cls,title):
        en = cls(name = title.get("name") , email = title.get("email") , user_id = title.get("user_id")) 
        return en

    def __str__(self):
        return self.name


