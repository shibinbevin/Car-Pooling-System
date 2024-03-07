from django.db import models
from accounts.models import User, Pooler

# Create your models here.

class UserComplaint(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pooler= models.ForeignKey(Pooler, on_delete=models.CASCADE,  null=True, blank=True, default=None)
    complaint_text = models.TextField()
    complaint_date = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    resolved_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"Complaint from {self.user} on {self.complaint_date}"