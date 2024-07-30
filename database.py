from peewee import *

db = SqliteDatabase('passwords.db')

class Usuario(Model):
    name = CharField()
    email = CharField()
    password = CharField()

    class Meta:
        database = db

class Password(Model):
    usuario = ForeignKeyField(Usuario, backref='usuarios')
    title = CharField()
    password = CharField()

    class Meta:
        database = db