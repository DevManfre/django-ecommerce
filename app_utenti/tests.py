from django.test import TestCase
from django.test.client import Client
from hashlib import md5

# Create your tests here.
client = Client()

class ViewTest(TestCase):
    def test_vendorWelcomePage_access(self):
        #Accesso da Anonimo
        response = client.get('/login/vendor/')
        self.assertTrue(response.status_code>399, f"Codice accesso anonimo = {response.status_code}")

        #Accesso da Utente
        client.login(username="Alessio", password=md5("Alessio".encode()).hexdigest())
        response = client.get('/login/vendor/')
        self.assertTrue(response.status_code>399, f"Codice accesso utente = {response.status_code}")

        #Accesso da Venditore
        client.login(username="raph", password=md5("raph00".encode()).hexdigest())
        response = client.get('/login/vendor/')
        self.assertTrue(response.status_code<300, f"Codice accesso venditore = {response.status_code}")