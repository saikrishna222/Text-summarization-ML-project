from django.db import models

class UserRegistrationModel(models.Model):
    idno=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100,unique=True)
    current_address=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    status=models.CharField(max_length=50,default=True)


class UrlSummarization(models.Model):
    sid=models.AutoField(primary_key=True)
    url_link=models.TextField(default=True)
    user_mail=models.EmailField()
    summarized_content=models.TextField()
    content_keywords=models.TextField()
    len_total_content=models.CharField(max_length=100)
    len_summarized_content=models.CharField(max_length=100)

class DocumentUploadMOdel(models.Model):
    did=models.AutoField(primary_key=True)
    dno=models.IntegerField(default=True)
    user_mail=models.EmailField()
    document=models.FileField(upload_to="files/",default=False)

class DocumentSummarizationModel(models.Model):
    sid=models.AutoField(primary_key=True)
    dno=models.IntegerField(default=True)
    document_link=models.TextField(default=True)
    user_mail=models.EmailField()
    summarized_content=models.TextField()
    content_keywords=models.TextField()
    len_total_content=models.CharField(max_length=100)
    len_summarized_content=models.CharField(max_length=100)

class ImageDataExtractionModel(models.Model):
    iid=models.AutoField(primary_key=True)
    ino=models.IntegerField()
    user_mail=models.EmailField(default=True)
    image=models.ImageField(upload_to="images/")
    data_extraction=models.TextField()
    content_keywords=models.TextField(default=True)
    len_total_content=models.CharField(max_length=100,default=True)
    len_extracted_data=models.CharField(max_length=100)