import base64
import uuid


class Programme:

    status_active = 1
    status_deleted = 0

    comments = []

    def __init__(self, title, desc, image):
        self.id = str(uuid.uuid4())
        self.title = title
        self.desc = desc
        self.image = image
        self.comments = Programme.comments

    def __str__(self):
        return f'Title: {self.title}\n' \
               f'Description: {self.desc}\n' \
               f'Images: {self.image}\n' \
               f'ID: {self.id}\n'
