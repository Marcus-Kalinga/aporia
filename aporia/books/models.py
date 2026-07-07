from django.db import models

# Create your models here.
class BookModel(models.Model):
	book_title= models.CharField(max_length=30, default= " ")
	book_author=models.CharField(max_length=30,  default= " ")
	book_short_review= models.CharField(max_length=100, default=" ")
	date_added= models.DateField(auto_now_add=True)
	
	def __str__(self):
		return self.title
		
