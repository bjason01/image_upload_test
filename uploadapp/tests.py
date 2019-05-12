"""
Test module for uploadapp
"""

# Django
from django.test import TestCase, Client
from django.test.client import MULTIPART_CONTENT
from django.core.files import File
from django.core.files.uploadedfile import InMemoryUploadedFile

# fileupload
from fileuploadexample.settings import MEDIA_ROOT

# initialize the Client
client = Client()


class TestViewPostImage(TestCase):
    """
    Class for view ImageView.
    A param must be of image.
    """

    def test_data_with_image(self):
    
        headers = {'Content-type' : MULTIPART_CONTENT}
        request_url = '/upload/'

        reopen = open(MEDIA_ROOT + "/imhisson.jpg", "rb")
        django_file = File(reopen)
        django_file.seek(0)
        
        image_file = InMemoryUploadedFile(
            django_file, None, 'image_name.jpg', 'image/jpg', None, None)

        data = {'image': image_file}

        response = client.post(request_url,
                               data=data,
                               headers=headers)

        self.assertEqual(response.status_code, 201)
