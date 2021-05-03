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





import calendar

class Utente():

    def __init__(self, nome, cognome, email, numero,passw):
        self.nome = nome
        self.cognome = cognome
        self.email = email
        self.numero = numero
        self.passw = passw

    def stampa_utenti(self):
        print("DATI PERSONALI: \nNome: %s, Cognome: %s, Email: %s, Numero: %s, Password: %s" % (self.nome.title(),self.cognome.title(),self.email,self.numero,self.passw))

    def cambia_passw(self):
        old_passw = str(input("Inserire vecchia password: "))
        if(self.passw == old_passw):
            new_passw = str(input("Inserire nuova password: "))
            self.passw = new_passw
            print("\nPassword cambiata con successo!\nNuova Password: %s" %(self.passw))                
        else:
            print("\nErrore, Password non corretta!")

    def registrazione(self,lista):
        lista = lista.append(self)
        #lista.append(self)
        print("\nRegistrazione Confermata!")


class Messaggio():

    def __init__(self,contenuto,utente):

        self.contenuto = contenuto
        self.utente = utente

    
class Sms(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.numero = self.utente.numero

    def stampa_mess(self):
        print("\nMessaggio: %s\nNumero: %s" % (self.contenuto,self.numero))



class Email(Messaggio):

    def __init__(self,contenuto,utente):
        super().__init__(contenuto,utente)
        self.email = self.utente.email   




class Tavolo():

    def __init__(self,id_tavolo,n_max=4):
        self.id_tavolo = id_tavolo
        self.n_max = n_max
        self.prenotazioni = []

    def prenota(self,utente,n_persone,data,orai,n_ore=2):
        oraf = orai+n_ore
        if (0 < n_persone <= self.n_max):          #verifica che il n persone sia entro il max
            if not (self.prenotato(data, orai, n_ore)):     #verifica che non sia gia prenotato    ("SE NON E' PRENOTATO")
                self.prenotazioni.append(Prenotazioni(utente,n_persone,data,orai,n_ore))         #crea e aggiunge dentro la lista prenotazioni l'oggetto della classe Prenotazioni()
                print("\nPrenotazione effettuata a nome di %s , per %d persone.\nData %s Ora: %d.00 - %d.00\n" %(utente.nome.title()+" "+utente.cognome.title(),n_persone,data,orai,oraf))

            else:
                print("%s, IL TAVOLO E' GIA PRENOTATO IN DATA: %s ORA: %d.00 - %d.00\n" % (utente.nome.title(),data, orai, oraf))
        else:
            print("%s, PRENOTAZIONE FALLITA. NUMERO PERSONE SUPERIORE A 4 !" % utente.nome.title())
              

    def prenotato(self,data,orai,n_ore):
        oraf = orai+n_ore
        for pr in self.prenotazioni:
            if (pr.data == data and (pr.orai <= orai < pr.oraf or pr.orai < oraf <= pr.oraf)):
                return True
            
        return False
    
    def stampa_cal(self):
        for pr in self.prenotazioni:
            print("Data: %s Ora: %d.00 - %d.00 " % (pr.data, pr.orai, pr.oraf))


class Prenotazioni():

    def __init__(self,utente,n_persone,data,ora,n_ore=2):
        self.utente = utente
        self.n_persone = n_persone
        self.data = data
        self.n_ore = n_ore #controllo ore       
        self.orai = ora
        self.oraf = self.orai+n_ore




lista_utenti = [] 
utente1 = Utente("nicola", "losito", "nicola@gmail.com", "333444555123", "1234")
utente2 = Utente("mario", "rossi", "mariorossi@gmail.com", "3572895645", "0000")
utente3 = Utente("guido", "lavespa", "guidolav@gmail.com", "3450789433", "4321")

tavolo1 = Tavolo(1,4)
tavolo1.prenota(utente1, 4, "26.04.2021", 10)
tavolo1.prenota(utente1, 2, "26.04.2021", 11)
tavolo1.prenota(utente2, 2, "26.04.2021", 11)
tavolo1.prenota(utente2, 3, "26.04.2021", 12)
tavolo1.prenota(utente1, 2, "27.04.2021", 13)
tavolo1.prenota(utente1, 6, "26.04.2021", 14)
tavolo1.prenota(utente1, 4, "26.04.2021", 14)

print("----- LISTA PRENOTAZIONI TAVOLO %d -----" % tavolo1.id_tavolo)
tavolo1.stampa_cal()

tavolo2 = Tavolo(2,6)
tavolo2.prenota(utente3, 6, "26.04.2021", 10)
tavolo2.prenota(utente1, 2, "26.04.2021", 11)
tavolo2.prenota(utente3, 2, "26.04.2021", 11)
tavolo2.prenota(utente3, 3, "26.04.2021", 12)
tavolo2.prenota(utente1, 2, "27.04.2021", 13)
tavolo2.prenota(utente3, 6, "26.04.2021", 14)
tavolo2.prenota(utente3, 4, "26.04.2021", 14)

print("----- LISTA PRENOTAZIONI TAVOLO %d -----" % tavolo2.id_tavolo)
tavolo2.stampa_cal()
'''
mess_num = Sms("Prenotazione effettuata con successo !",myown)
mess_num.stampa_mess()
#print("\n")
myown.stampa_utenti()
#myown.cambia_passw("5678")
myown.cambia_passw()

myown.registrazione(lista_utenti)

for utente in lista_utenti:
    utente.stampa_utenti()


#calendar.prcal(2021)


'''



