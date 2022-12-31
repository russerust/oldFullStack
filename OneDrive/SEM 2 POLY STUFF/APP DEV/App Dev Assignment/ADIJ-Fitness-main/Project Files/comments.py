import uuid

class Comments:

    def __init__(self, text, author, post):
        self.id = str(uuid.uuid4())
        self.text = text
        self.author = author
        self.post = post

    def __str__(self):
        return f'Text: {self.text}\n' \
               f'Author: {self.author}\n' \
               f'Post: {self.post}\n' \
               f'ID: {self.id}\n'