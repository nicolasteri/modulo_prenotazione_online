import peewee
import datetime

db = peewee.SqliteDatabase("prenotazione.db")

class Tavolo(peewee.Model):

    id_tavolo = peewee.IntegerField()
    n_max = peewee.IntegerField()

    class Meta:

        database = db
        db_table = 'Tavolo'



class Utenti(peewee.Model):

    nome = peewee.CharField()
    cognome = peewee.CharField()
    email = peewee.CharField()
    numero = peewee.CharField()
    password = peewee.CharField()
    privacy = peewee.BooleanField()

    class Meta:

        database = db
        db_table = 'Utente'



class Prenotazioni(peewee.Model):

    id_utente = peewee.IntegerField()
    id_tavolo = peewee.IntegerField()
    data = peewee.DateTimeField()
    ora = peewee.DateTimeField()

    class Meta:

        database = db
        db_table = 'Prenotazioni'




Tavolo.create_table()
Utenti.create_table()
Prenotazioni.create_table()



