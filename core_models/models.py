from django.db.models import *

class PictureUpload(Model):
    name = CharField(max_length=128)
    picture = ImageField("Image", upload_to="images/")