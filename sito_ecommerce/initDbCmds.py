import re
from django.contrib.auth.models import User
import datetime
from hashlib import md5
import os
from django.core.files.images import ImageFile
import random
import exrex

from sito_ecommerce.settings import PRODUCTS_IMAGES_DIR

from app_utenti.models import *
from app_prodotti.models import *


def eraseDatabase():
    def deleteTmpImages():
        regex = re.compile(
            '^[a-z]{0,3}-{0,1}[a-z]{0,1}_[a-zA-Z0-9_]{7,}\.avif$')
        fileList = os.listdir(PRODUCTS_IMAGES_DIR)

        for file in fileList:
            if regex.match(file):
                os.remove(os.path.join(PRODUCTS_IMAGES_DIR, file))

    def deleteTables():
        User.objects.all().delete()

        Category.objects.all().delete()
        Brand.objects.all().delete()
        Product.objects.all().delete()
        Score.objects.all().delete()

    deleteTables()
    deleteTmpImages()

    print("--->DATABASE ELIMINATO<---")


def initDatabase():
    def adminCreation():
        user = User(
            username='admin',
            email='admin@admin.admin',
            first_name='admin',
            last_name='admin',
        )
        user.set_password('admin')
        user.is_superuser = True
        user.is_staff = True
        user.last_login = datetime.date.today()
        user.save()

    def usersCreation():
        users = {
            "username": [
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
            "first_name": [
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
            "last_name": [
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
            "birthDate": [datetime.date(
                random.randint(1950, 2004),
                random.randint(1, 12),
                random.randint(1, 28)
            ) for i in range(10)],
            "email": [
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
            "password": [
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
            "iban": [""]*5 + [exrex.getone('IT[A-Z0-9]{4}300203280[AZ0-9]{12}') for i in range(5)]
        }

        for i in range(len(users["first_name"])):
            ecommerceuser = EcommerceUser()
            ecommerceuser.id = i
            ecommerceuser.username = users["username"][i]
            ecommerceuser.first_name = users["first_name"][i]
            ecommerceuser.last_name = users["last_name"][i]
            ecommerceuser.birthDate = users["birthDate"][i]
            ecommerceuser.email = users["email"][i]
            ecommerceuser.set_password(
                md5(users["password"][i].encode()).hexdigest())
            ecommerceuser.iban = users["iban"][i]
            ecommerceuser.last_login = datetime.date.today()

            if ecommerceuser.iban != '':
                ecommerceuser.isVendor = True

            ecommerceuser.save()

    def categoriesCreation():
        categories = [
            "ALTRO",
            "Tapis Roulant",
            "Cyclette",
            "Spin Bike",
            "Pesi, Manubri e Bilanceri",
            "Step e Stepper",
            "Abbigliamento",
            "Accessori"
        ]

        for i in range(len(categories)):
            category = Category()
            category.id = i
            category.name = categories[i]
            category.save()

    def brandsCreation():
        brands = [
            "ALTRO",
            "Domyos",
            "Schwinn",
            "Cadenza",
            "Corength",
            "Pro-Form",
            "Puma",
            "Adidas",
            "Nabaiji"
        ]

        for i in range(len(brands)):
            brand = Brand()
            brand.id = i
            brand.name = brands[i]
            brand.save()

    def productsCreation():
        products = {
            'name': [
                'Tapis Roulant Connesso T540C',
                'Tapis roulant comfort T520B',
                'Cyclette ESSENTIAL EB 120',
                'Bici biking SCHWINN IC8 800IC',
                'Cadenza Fitness S35 Indoor Magnetic Bike Display 18 Kg',
                'Indoor bike EVO S2000 YS2000H a frizione con supporto tablet-smartphone',
                'Kit manubri e bilanciere bodybuilding 93kg',
                'Kit manubri e bilanciere bodybuilding 50kg',
                'Disco ghisa bodybuilding 28mm',
                'Bilanciere curl bodybuilding 28mm',
                'Manubri pvc 2x2 kg blu',
                'Manubri pvc 2x3 kg grigi',
                'Step and Tone Stepper con sistema walky per allenamento degli arti superiori',
                'Stepper MS500 avorio-rosa',
                'Stepper Cardio HIIT TRAINER L6',
                'T-shirt uomo fitness Puma regular cotone bianca',
                'Canotta uomo bodybuilding stringer verde militare',
                'Scarpe Flashfilm Train 2',
                'Pantaloncini uomo fitness Puma ACTIVE misto cotone neri',
                'Pantaloncini uomo fitness Adidas misto cotone neri',
                'Scarpe fitness uomo 100 nere',
                'Calze antiscivolo unisex fitness 900 traspiranti grigie',
                'Pantaloni uomo fitness cotone con bottoni laterali blu',
                'Supporto per le spalle',
                'Telo microfibra L 80x130 cm arancione',
                'Telo microfibra M 60 x 80 cm grigio',
                'Cavigliera compressiva ambidestra unisex SOFT 900 nera'
            ],
            'description': [
                '''Gli appassionati di fitness hanno sviluppato questo tapis roulant per migliorare le capacità cardiovascolari.
            Tapis roulant silenzioso con superficie di corsa ideale per gli sportivi che corrono fino a 16km/h.
            Il T540 è compatibile con l'app Domyos E-Connected, per seguire gli allenamenti.''',
                '''Gli appassionati di fitness hanno sviluppato questo tapis roulant per mantenersi in forma e snellire la linea, per un uso domestico.
            Il tapis roulant T520 è ideato per praticare running a bassa intensità, in casa. Semplice ed intuitivo, sarà il partner ideale per mantenere
            e migliorare le tue capacità cardiache!''',
                '''La nostra equipe di ideazione ha sviluppato questa cyclette per aiutarti a mantenerti in forma e bruciare calorie.
            Vuoi mantenerti in forma in casa? L'EB 120 Domyos è l'ideale! In più ha un manubrio ergonomico per un comfort maggiore e una consolle
            con 5 funzioni per seguire i tuoi allenamenti!''',
                '''Bici biking top di gamma. Un ottimo partner di allenamento, ti porterà lungo escursioni rilassanti o ti
            farà arrampicare sulle cime più alte, per pedalate esaltanti!''',
                '''La S35 è una bicicletta indoor ad alte prestazioni per atleti professionisti e un esaltante power trainer per tutti i tipi di atleti.''',
                '''La bici indoor EVO S2000 è perfetta per chi è alle prime armi con il ciclismo indoor. Utilizzo consigliato fino a 7 ore settimanali e
            con monitor LCD per controllare RPM, tempo, calorie e distanza''',
                '''Questo kit è stato sviluppato dai nostri istruttori e dalla nostra equipe di ideazione per praticare bodybuilding in casa con manubri
            e bilanciere. Kit completo per realizzare tanti esercizi di bodybuilding, bicipiti, tricipiti, deltoidi, pettorali, dorsali
            e parte inferiore del corpo, affondi e squat.''',
                '''Il kit 50 kg è stato sviluppato dai nostri istruttori e dalla nostra equipe di ideazione per praticare bodybuilding in casa.
            Kit completo con bilanciere, manubri e dischi per realizzare tanti esercizi di bodybuilding, come bicipiti, tricipiti, deltoidi, pettorali,
            dorsali e parte inferiore del corpo.''',
                '''Questo disco con diametro 28mm è stato sviluppato dai nostri coach e dalla nostra equipe di ideazione.
            Serie completa 0.5, 1, 2, 5, 10, e 20 kg, per seguirti al meglio nei tuoi progressi. Presa facile grazie al bordo.''',
                '''Le nostre equipe di ideazione hanno sviluppato per voi questo bilanciere da bodybuilding con una solidità a prova di tutto!
            La zigrinatura permette un grip migliore e quindi una pratica in tutta sicurezza. Compatibile con dischi di 28mm.''',
                '''Questi manubri ergonomici sono stati disegnati per permettere una presa facile: tutto quello che ti serve per effettuare una seduta 
            in condizioni ottimali! I manubri sono fondamentali per le sedute di fitness. Quindi abbiamo puntato tutto sulla facilità di presa,
            ma anche sulla forma che evita che rotolino quando vengono appoggiati per terra.''',
                '''Questi manubri ergonomici sono stati disegnati per permettere una presa facile: tutto quello che ti serve per effettuare una seduta in
            condizioni ottimali! I manubri sono fondamentali per le sedute di fitness. Quindi abbiamo puntato tutto sulla facilità di presa, ma anche
            sulla forma che evita che rotolino quando vengono appoggiati per terra.''',
                '''Ideato per l'allenamento degli arti inferiori e superiori del corpo! Stepper con MOVIMENTO ORBITALE TWISTER!''',
                '''Sviluppato dai nostri ideatori, lo stepper MS500 ti offre la possibilità di fare un lavoro cardio e di rafforzare tutti i muscoli del corpo.
            Apprezzerai il movimento twister dello stepper MS500 con elastici, per tonificare tutto il corpo.''',
                '''Lo stepper cardio HIIT L6 di Proform è ideato per bruciare il massimo delle calorie e per aumentare la forza. Abbonamento di un anno
            iFit Family incluso. L'Hiit (High-Intensity Interval Training) è un allenamento tecnico ad alta intensità composto da periodi molto
            brevi di sforzo intenso alternati a periodi di recupero.''',
                '''Ideata per praticare fitness e ginnastica dolce. Questa t-shirt principalmente in cotone è il prodotto perfetto per essere trendy
            in palestra... e non solo! Questa t-shirt intramontabile, non potrà che conquistarti con il suo comfort e la sua super traspirabilità!''',
                '''I nostri ideatori appassionati di bodybuilding hanno sviluppato questa canotta stringer per permetterti di essere a tuo agio in tutti
            i movimenti. Questa canotta valorizza la muscolatura ed assicura un'ottima libertà di movimento in tutte le sedute di bodybuilding.''',
                '''Modello ultraleggero per la palestra e il tempo libero''',
                '''Prodotto ideato per la pratica del fitness e della ginnastica dolce. Questi pantaloncini sono il prodotto perfetto per essere trendy
            in palestra... e non solo! Lunghezza a metà coscia per più libertà di movimento, cotone spesso e traspirante... Ed un grande stile!''',
                '''Pratica la tua attività sportiva in tutta tranquillità con questi pantaloncini Adidas confortevoli e dal look sportivo! Il taglio
            adatto per fare sport e la grafica dinamica Adidas rendono questi pantaloncini un capo indispensabile.
            L'elastico in vita con coulisse e la tasca posteriore permettono di avere più comfort.''',
                '''La nostra equipe di appassionati di fitness ha ideato queste scarpe per permetterti di iniziare a praticare fitness in palestra.
            Vuoi una calzatura adatta per iniziare a fare fitness? Queste scarpe ti accompagneranno in tutte le tue sedute.
            Flessibili, leggere e ammortizzanti, diventeranno indispensabili.''',
                '''La nostra esperienza al vostro servizio con queste calze antiscivolo che diventeranno il tuo migliore alleato per fare sport... e non solo!
            Il comfort comincia dai piedi, per questo abbiamo puntato sul sostegno, sull'aderenza e sul comfort per queste calze, in modo da farti
            trascorrere dei bei momenti sportivi... O di relax in casa!''',
                '''Ideato dai nostri ingegneri prodotto per facilitare la vestizione a chi ha difficoltà motorie.
            Tessuto in cotone per garantire morbidezza e comfort, bottoni laterali per facilitare la vestizione.''',
                '''Supporto per le spalle di colore nero/grigio.''',
                '''Le nostre squadre di design hanno sviluppato questo telo per tutti gli sportivi che vogliono asciugarsi bene.
            Poco spazio nello zaino? Il telo in microfibra L 80 x 130 cm extra-compatto ti accompagnerà ovunque asciugando molto in fretta.''',
                '''Le nostre squadre di design hanno sviluppato questo telo per tutti gli sportivi che vogliono asciugarsi bene.
            Piccolo telo in microfibra molto pratico, extra-compatto ed extra-assorbente. Da portare ovunque! Taglia M: 65x90 cm.''',
                '''La cavigliera Soft 900 è ideata per assicurare sostegno muscolare, alleviare i dolori legati ad un'instabilità o all'artrite.
            Maglia compressiva estremamente confortevole e senza cuciture, traspirante grazie alle aerazioni. Gli inserti in schiuma intorno al
            malleolo offrono più comfort quando si indossano le scarpe.'''
            ],
            'price': [
                599.99,
                499.99,
                179.99,
                899.99,
                459.00,
                399.00,
                229.99,
                149.99,
                1.49,
                34.99,
                14.99,
                19.99,
                109.99,
                59.99,
                999.99,
                11.99,
                9.99,
                74.95,
                24.99,
                32.99,
                19.99,
                6.99,
                34.99,
                59.99,
                5.99,
                3.99,
                19.99
            ],
            'category': [
                Category.objects.get(name='Tapis Roulant'),
                Category.objects.get(name='Tapis Roulant'),
                Category.objects.get(name='Cyclette'),
                Category.objects.get(name='Cyclette'),
                Category.objects.get(name='Spin Bike'),
                Category.objects.get(name='Spin Bike'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Pesi, Manubri e Bilanceri'),
                Category.objects.get(name='Step e Stepper'),
                Category.objects.get(name='Step e Stepper'),
                Category.objects.get(name='Step e Stepper'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Abbigliamento'),
                Category.objects.get(name='Accessori'),
                Category.objects.get(name='Accessori'),
                Category.objects.get(name='Accessori'),
                Category.objects.get(name='Accessori')
            ],
            'brand': [
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Schwinn'),
                Brand.objects.get(name='Cadenza'),
                Brand.objects.get(name='ALTRO'),
                Brand.objects.get(name='Corength'),
                Brand.objects.get(name='Corength'),
                Brand.objects.get(name='Corength'),
                Brand.objects.get(name='Corength'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='ALTRO'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Pro-Form'),
                Brand.objects.get(name='Puma'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='ALTRO'),
                Brand.objects.get(name='Puma'),
                Brand.objects.get(name='Adidas'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='Domyos'),
                Brand.objects.get(name='ALTRO'),
                Brand.objects.get(name='ALTRO'),
                Brand.objects.get(name='Nabaiji'),
                Brand.objects.get(name='Nabaiji'),
                Brand.objects.get(name='ALTRO')
            ],
            "vendor": [user for user in EcommerceUser.objects.filter(isVendor=True)]*6
        }

        for i in range(len(products["name"])):
            product = Product()
            product.id = i
            product.name = products["name"][i]
            product.description = products['description'][i]
            product.price = products["price"][i]
            product.image = ImageFile(open(os.path.join(
                PRODUCTS_IMAGES_DIR, product.name.lower().replace(' ', '-') + '.avif'), 'rb'))
            product.category = products["category"][i]
            product.brand = products["brand"][i]
            product.vendor = products["vendor"][i]

            product.save()

    def scoresCreation():
        textScores = [
            'Perfetto,tutto quello che volevo.',
            'Sono soddisfatta del mio acquisto!',
            'Non sono soddisfatto del mio acquisto!',
            '''Ho fatto un acquisto che nemmeno immaginavo di aver un prodotto al top di gamma lo consiglio assolutamente altre
            100 volte è fatto benissimo. Acquistatelo vedete che vi troverete benissimo. Buona visione''',
            'Proprio quello che cercavo.',
            'Ottimo per uso casalingo',
            'Se vuoi mantenerti in forma e’ una buona alternativa se non puoi andare in palestra anche come prezzo molto conveniente',
            'Prodotto ottimo, soddisfa a pieno le aspettative ...',
            'Il rapporto qualita’ prezzo e secondo me ottimo, molto soddisfacente risponde perfettamente alle mie necessità.',
            'Tutto come da indicazioni ricevute.',
            ''
        ]
        scores = {
            'product': [product for product in Product.objects.all()]*2,
            'user': [user for user in EcommerceUser.objects.all()]*6,
            'value': [random.randint(Score.MIN_VALUE, Score.MAX_VALUE) for random_int in range(100)],
            'text': [textScores[random.randint(0, len(textScores)-1)] for i in range(100)]
        }

        for i in range(len(scores['product'])):
            score = Score()
            score.id = i
            score.product = scores['product'][i]
            score.user = scores['user'][i]
            score.value = scores['value'][i]
            score.text = scores['text'][i]
            score.save()

    adminCreation()
    usersCreation()
    categoriesCreation()
    brandsCreation()
    productsCreation()
    scoresCreation()

    print("--->DATABASE CREATO<---\n")
