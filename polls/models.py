from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class File(models.Model):
    document_type = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='list/pdfs/')

    def __str__(self):
    	return self.title

    
    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)  # Call the "real" save() method.
      	 




