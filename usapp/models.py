from django.db import models

class Folder(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    parentId = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')
    type = models.CharField(max_length=6, default="Folder")
    def __str__(self):
        return self.name

class Text(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    parentId = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True, blank=True)
    type = models.CharField(max_length=4, default="Text")
    def __str__(self):
        return self.name

class Image(models.Model):
    photo = models.ImageField(upload_to='images/')