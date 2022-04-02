from secrets import choice
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




STATUS_CHOICE = {
    ('Not Started', 'Not Started'),
    ('In Progress', 'In Progress'),
    ('Watch', 'Watch'),
    ('Complete', 'Complete'),
}

class Project(models.Model):
    name = models.CharField(max_length =50)
    description = models.TextField()
    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta: 
        ordering = ['create_at']