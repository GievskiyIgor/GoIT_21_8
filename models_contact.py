from mongoengine import connect, Document, StringField, BooleanField

connect(
    db="db_21",
    host="mongodb+srv://sillahed:iyCdrVhpY6UfeqmX@dbmongo.xwbmns2.mongodb.net/",
)

class Contact(Document):
    full_name = StringField(required =True, unique=True)
    email = StringField(required=True, unique =True)
    message_sent = BooleanField(default=False)
    phone =StringField()
    preferred_contact_method = StringField(choices=["email","sms"], default="email")