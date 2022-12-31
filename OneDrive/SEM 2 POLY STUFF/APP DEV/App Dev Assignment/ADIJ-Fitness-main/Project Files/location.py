import uuid


class Location:

    status_active = 1
    status_closed = 0

    def __init__(self, location, image):
        self.location = location
        self.id = str(uuid.uuid4())
        self.status = Location.status_active
        self.image = image

    def get_location(self):
        return self.location

    def open_location(self):
        self.status = Location.status_active

    def close_location(self):
        self.status = Location.status_closed

    def __str__(self):
        return f'ID: {self.id}\n' \
               f'Location: {self.location}\n' \
               f'Status: {self.status}\n' \
               f'Image: {self.image}'
