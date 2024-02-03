# coloranalyzerapp/views.py

from django.shortcuts import render
from PIL import Image, ImageStat
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.conf import settings
from django.templatetags.static import static

def color_analyzer(request):
    dominant_color = None
    uploaded_image = None

    if request.method == 'POST' and request.FILES['image']:
        image = request.FILES['image']
        uploaded_image, dominant_color = process_image(image)

    return render(request, 'coloranalyzerapp/color_analyzer.html', {'dominant_color': dominant_color, 'uploaded_image': uploaded_image})

def process_image(image):
    # Save the image to the media directory
    img = Image.open(image)
    img.save("media/uploaded_image.png")

    # Get dominant color
    img.thumbnail((100, 100))
    stat = ImageStat.Stat(img)
    dominant_color = tuple(int(val) for val in stat.mean[:3])

    # Convert the image to BytesIO format
    image_io = BytesIO()
    img.save(image_io, format='PNG')

    # Create InMemoryUploadedFile for the image
    uploaded_image = InMemoryUploadedFile(
        ContentFile(image_io.getvalue()),
        None,
        'uploaded_image.png',
        'image/png',
        image_io.tell(),
        None
    )

    # Get the absolute URL of the uploaded image
    uploaded_image_url = settings.MEDIA_URL + 'uploaded_image.png'

    return uploaded_image_url, dominant_color
