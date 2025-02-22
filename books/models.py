from mongoengine import Document, EmbeddedDocument, fields

class Review(EmbeddedDocument):
    rating = fields.IntField(required=True, min_value=1, max_value=5)
    comment = fields.StringField()

class Book(Document):
    title = fields.StringField(required=True, max_length=200)
    author = fields.StringField(required=True, max_length=100)
    publication_year = fields.IntField(required=True)
    genre = fields.StringField(required=True)
    reviews = fields.EmbeddedDocumentListField(Review)
