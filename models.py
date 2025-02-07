import mongoengine as me

class Players(me.Document):
    name = me.StringField(required=True)
    kit_number = me.IntField()
    image = me.StringField()
    position = me.StringField()
        