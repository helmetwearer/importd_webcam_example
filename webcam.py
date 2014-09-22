from importd import d
d(DEBUG=True, INSTALLED_APPS=["django.contrib.auth","core_models", "south"])

from core_models.models import PictureUpload
from uuid import uuid4
import base64, os

@d("/")
def index(request):
    if request.method == 'POST':
        base_64_picture = request.POST.get('picture')
        picture_string = base64.b64decode(base_64_picture)
        filename = '%s.jpg' % uuid4()
        file = open('static/media/images/%s' % filename, 'wb+')
        file.write(picture_string)
        file.close()
        upload = PictureUpload()
        upload.picture = 'media/images/%s' % filename
        upload.name = request.POST.get('name', filename)
        upload.save()
        return {
                "success":True,
                "file": upload.picture.url
                }
    
    return "webcam.html"

@d('/pictures')
def pictures(request):
    return "pictures.html", {'pictures': [os.path.basename(picture.picture.name) for picture in  PictureUpload.objects.all()]}

if __name__ == "__main__":
    d.main()
