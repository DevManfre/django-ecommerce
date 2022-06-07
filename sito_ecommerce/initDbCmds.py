from django.contrib.auth.models import User
import datetime
from hashlib import md5

from app_utenti.models import EcommerceUser

def eraseDatabase():
    User.objects.all().delete()

    print("--->DATABASE ELIMINATO<---")

def initDatabase():
    #Creazione Admin
    user = User(
        username = 'admin',
        email = 'admin@admin.admin',
        first_name = 'admin',
        last_name = 'admin',
    )
    user.set_password('admin')
    user.is_superuser = True
    user.is_staff = True
    user.last_login = datetime.date.today()
    user.save()

    #Creazione Utenti Random
    users = {
        "username" : [
            "Alessio",
            "gattino00",
            "justice_",
            "fonforo",
            "cavallopazzo",
            "asdasd",
            "wallet",
            "raph",
            "italo_calvino",
            "Mississipi"
        ],
        "first_name" : [
            "Alessio",
            "Francesco",
            "Marco",
            "Alfredo",
            "Francesco",
            "Tommaso",
            "Luca",
            "Alice",
            "Sara",
            "Jessica"
        ],
        "last_name" : [
            "Manfredini",
            "Venturelli",
            "Ferrara",
            "Dozza",
            "Pia",
            "Vandelli",
            "Cantelli",
            "Severi",
            "Ferrari",
            "Maia"
        ],
        "birthDate" : [
            datetime.date(2000,5,16),
            datetime.date(2002,4,14),
            datetime.date(1980,1,30),
            datetime.date(2001,6,6),
            datetime.date(1999,2,28),
            datetime.date(1999,3,3),
            datetime.date(1998,5,15),
            datetime.date(1997,7,21),
            datetime.date(1996,9,20),
            datetime.date(1999,11,27)
        ],
        "email" : [
            "alessio@manfredini.it",
            "francesco@venturelli.com",
            "marco@ferrara.com",
            "alfredo@dozza.com",
            "francesco@pia.com",
            "tommaso@vandelli.it",
            "luca@cantelli.com",
            "alice@severi.com",
            "sara@ferrari.com",
            "jessica@maia.com",
            "tommaso",
            "comodino00",
            "masterofpuppets!",
            "itopinonavevanonipoti",
            "cavolfiori123"
        ],
        "password" : [
            "Alessio",
            "Django02",
            "ferrara!",
            "alfredozza22",
            "frapia69!",
            "fortnite",
            "samsung",
            "raph00",
            "qwerty09",
            "zxcdsaqwe"
        ],
        "iban" : [
            "IT52A0300203280258515626349",
            "",
            "IT25X0300203280442154535952",
            "",
            "IT46H0300203280896418952432",
            "",
            "IT53Y0300203280762661629485",
            "",
            "IT61S0300203280467765126978",
            "" 
        ]
    }

    for i in range(len(users["first_name"])):
        ecommerceuser = EcommerceUser()
        ecommerceuser.username = users["username"][i]
        ecommerceuser.first_name = users["first_name"][i]
        ecommerceuser.last_name = users["last_name"][i]
        ecommerceuser.birthDate = users["birthDate"][i]
        ecommerceuser.email = users["email"][i]
        ecommerceuser.set_password(md5(users["password"][i].encode()).hexdigest())
        ecommerceuser.iban = users["iban"][i]
        ecommerceuser.last_login = datetime.date.today()

        # DECOMMENTARE LA LINEA PER RICEVERE UNA DESCRZIONE DEI DATI CREATI NEL DB
        #print(ecommerceuser.description())     

        ecommerceuser.save()

    print("--->DATABASE CREATO<---\n")