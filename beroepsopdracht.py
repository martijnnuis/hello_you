from pickle import STOP
import time


def verhaal1():
    print("Je slaapt, maar je wordt wakker gemaakt het luchtalarm gaat af en je ouders komen je kamer binnen")
    time.sleep(.3)
    print("rennen. Snel vluchten ze samen met jouw naar de schuil kelder, het huis naast die van jou is opgeblazen.")
    time.sleep(.3)
    print("Dit was de druppel voor je moeder, ze wilt naar een ander land toe gaan ergens in Europa.")
    time.sleep(.3)
    print("Je vader wilt daarentegen gewoon thuis in Syrië blijven.")
    time.sleep(.3)
    print("Je moet een keuze maken of A: je blijft of B: je gaat mee.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal21()
        elif d == "B" or d == "b":
            verhaal2()

def verhaal2():
    print("Je verlaat ’s ochtends vroeg samen met je moeder het huis en gaat lopen gelukkig")
    print("woon je niet ver van de grens met Libanon en Turkije.")
    print(" Je moet bepalen welk land je in wilt, wil je A: naar Libanon of B: naar Turkije.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal11()
        elif d == "B" or d == "b":
            verhaal3()

def verhaal3():
    print("Eenmaal aangekomen bij de Turkse grens probeer je over de muur te klimmen dat lukt gelukkig onopgemerkt.")
    print("Je zet je reis voort richting Istanboel, want je hebt gehoord dat Nederland een goed en veilig land")
    print("is van andere mensen die over de muur probeerden te komen.")
    print("Plotseling wordt je aangehouden door de politie")
    print("“we willen je papieren zien”")
    print("Gelukkig was je voorbereid en heb je het een en ander geregeld.")
    print("De politie is niet onder de indruk “dit zijn niet de juiste papieren jongen”.")
    print("Ze willen je oppakken maar je weet dat de politie best corrupt is en je hebt 1000 lira.")
    print("Ga je ze A: omkopen voor 700 lira of B: niet.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal4()
        elif d == "B" or d == "b":
            verhaal21()

def verhaal4():
    print("Nadat je de agent hebt omgekocht heb je nog net genoeg geld voor een reis met de bus naar Istanboel te gaan.")
    print("Eenmaal daar aangekomen moet je weer te voet verder al je geld is nu op gelukkig ben je nu wel weer")
    print("weer een stuk dichter bij de grens en duurt het niet veel langer meer tot dat je Europa binnen komt.")
    print("Je ziet in de verte de grens met Griekenland. Je begint moe te worden.")
    print("Wil je A: doorlopen of B: slapen")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal5()
        elif d == "B" or d == "b":
            verhaal5()

def verhaal5():
    print("Gelukkig je staat samen met je moeder bij de grens nu alleen nog proberen door te komen want er staat een hele rij.")
    print("Na 3 uur gewacht te hebben ben je eindelijk aan de beurt maar je moeder mag er niet door")
    print("“te oud” zeiden de grenswachters.")
    print("Je ziet aan de andere kant een bus staan je past er nog bij.")
    print("laat je A: je moeder alleen die weer terug gestuurd gaat worden of B: ga je met je moeder mee.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal6()
        elif d == "B" or d == "b":
            verhaal20()

def verhaal6():
    print("Met pijn in je hart en verdriet ga je over de grens en je hoort je moeder nog zeggen “het komt goed”.")
    print("Je stapt de bus in en die vertrekt naar een kamp voor asielzoekers.")
    print("Daar krijg je te horen dat je je reis moet doorzetten omdat je daar niet kan blijven.")
    print(" Eenmaal buiten het kamp sta je met wat land genoten te praten")
    print("en zie je uit je ooghoek een paar mysterieuze figuren staan,")
    print("1 van de landgenoten loopt naar hen toe.")
    print("“Ze hebben een geweldig aanbod” zegt hij,")
    print("“als we met ze meegaan dan zijn we in no time in Duitsland”.")
    print(" A: Vertrouw je de mysterieuze mannen of B: zet je de reis samen met 1 iemand voor die de mannen niet vertrouwd.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal12()
        elif d == "B" or d == "b":
            verhaal7()

def verhaal7():
    print("De dagen duren langer en langer voor je gevoel ben je nu al een jaar op de vlucht,")
    print("al is het pas 2 maanden geleden dat je je huis verlaten hebt.")
    print("Je bent eindelijk na vele dagen lopen bij Niki aangekomen,")
    print("daar word je ontvangen door vrijwilligers die je willen helpen de grens over te gaan van Noord-Macedonië.")
    print("A: Wil over de grens gaan van Noord-Macedonië of B: wil je hier blijven?")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or "a":
            verhaal8()
        elif d == "B" or "b":
            verhaal20()

def verhaal8():
    print("Het is een zware reis door Noord-Macedonië maar je krijgt gelukkig wel wat hulp van lokale groepen en vrijwilligers.")
    print("Na 3 weken door het land gelopen te hebben zie je de grens van Servië.")
    print("“Hoelang denk je dat het nog gaat duren?” vraagt je landgenoot met wie je samen op reis bent.")
    print("“Ik weet het niet maar volgens mij zijn we al verder gekomen dan die andere mensen” zeg je.")
    print("Ineens bedenk je je dat 1 van de vrijwilligers naar Praag moet en je zegt tegen je landgenoot")
    print("“We kunnen die vrijwilligster wel vragen of we met haar mee kunnen rijden naar Praag”,")
    print("“tja, we kunnen het proberen” zegt je landgenoot.")
    print("A: Vraag je de vrijwilligster of B: loop je door?")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal10()
        elif d == "B" or d == "b":
            verhaal9()

def verhaal9():
    print("Het is een zware reis maar je wilt nu in 1 keer door naar Praag het is ongeveer 21 dagen lopen.")
    print("Het is een zware reis je wordt minder goed geholpen dan in andere landen,")
    print("mensen kijken je met de nek aan het is een klote gevoel.")
    print("Het zijn de zwaarste nachten je kan nauwelijks slapen en het begint herfst te worden en dat maakt de reis niet beter.")
    print(" Je landgenoot heeft de moed nog niet in de schoenen laten zakken en Servië ligt al snel achter jullie.")
    print("Hongarije is ook niet al te zwaar en slowakije en oostenrijk ook niet en je ziet praag al snel dichtbij komen.")
    print("A: Wil je nog even door zetten of B: wil je slapen?")
    while True:
        d = input("wat is jouw keuze? A of B")
        if d == "A" or d == "a":
            verhaal10()
        elif d == "B" or d == "b":
            verhaal10()

def verhaal10():
    print("Aangekomen in Praag kijken jullie hoe de reis verder te zetten, uiteindelijk komen er twee keuzes op jullie pad.")
    print(" Een aardige duitser die naar A: hannover moet en")
    print("B: iemand die naar munchen moet bieden jullie een ritje aan maar met wie ga je mee?")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal17()
        elif d == "B" or d == "b":
            verhaal18()

def verhaal11():
    print("Eenmaal bij de grens van libanon aangekomen klimmen jij en je moeder over de muur")
    print("gelukkig ongezien want anders was de kans groot dat je werd neer geschoten")
    print("maar je wordt wel aangesproken door een mysterieuze man hij vraagt of je snel naar duitsland zou willen?")
    print("A: Neem je het aanbod aan of B: sla je het af")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal12()
        elif d == "B" or d == "b":
            verhaal12()

def verhaal12():
    print("Je wordt knock-out geslagen en je wordt wakker midden om zee.")
    print("Je ziet dat je niet als eerste wakker bent geworden en vraagt aan iemand anders waar jullie zijn.")
    print("“Ik zou het niet weten” zegt de jonge vrouw aan wie je het hebt gevraagd.")
    print("Na lang varen worden jullie opgepikt door de zeemacht van Italië en veilig naar het vaste land gebracht.")
    print("A: Je kan asiel krijgen in Italië of B: wil je verder gaan naar nederland?")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal20()
        elif d == "B" or d == "b":
            verhaal13()

def verhaal13():
    print("Je zit in de stad napels hier hoor je dat je het beste naar de grote stad rome kan, dat is ongeveer 3 dagen lopen.")
    print("Je moeder zegt dat dit voor haar het einde van de reis is, je bent erg verdrietig maar accepteert het.")
    print("Je zet samen met 4 andere asielzoekers je reis voort en het is zwaar je moet oppassen voor de politie")
    print("anders wordt je terug gestuurd en dat wil je absoluut voorkomen.")
    print("Na 3 dagen lopen kom je dan eindelijk in rome aan.")
    print("1 van de anderen waarmee je op pad bent begint ziek te worden A: houden jullie haar bij je groep of B: laat je haar achter")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal22()
        elif d == "B" or d == "b":
            verhaal14()

def verhaal14():
    print("Je zet nu met z’n drieën verder richting florance, de reis duurt 5 dagen voor dat je aankomt.")
    print("Je ziet in de verte aankomen wat doe je?")
    print("Ga je A: je ergens verstoppen of B: loop je door?")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal15()
        elif d == "B" or d == "b":
            verhaal21()

def verhaal15():
    print("e komt steeds dichter bij nederland en je reist met z’n drieën verder door italië")
    print("tot je bij de grens komt en je die moet passeren")
    print("het lukt jou en 1 ander om de grens te passeren de laatste komt de grens niet over.")
    print("De reis naar zurich duurt nu al vijf dagen en om in zurich te komen duurt het zeker nog vijf à zes dagen om daar te komen.")
    print(" Na je lange reis kom je dan eindelijk aan in zurich. Je bent opgelucht ondanks dat je nog zolang moet.")
    print("A: Wil je een paar nachten rusten of B: wil je verder.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal16()
        elif d == "B" or d == "b":
            verhaal16()

def verhaal16():
    print("Je reist verder en je komt de grens van duitsland.")
    print("Het is een zware reis maar met z’n drieën kom je terecht in een vluchtelingen kamp.")
    print("Het zijn een paar zware nachten en je krijgt te horen dat je de mogelijkheid hebt om naar")
    print(" hannover of munchen te gaan om verder te reizen naar nederland.")
    print("Waar kies je voor A: Munchen of B: Hannover.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal17()
        elif d == "B" or d == "b":
            verhaal18()

def verhaal17():
    print("Aangekomen in Hannover is het niet super ver meer")
    print("en je hebt zoals je van mensen hebt begrepen nog maar hoog uit 3 dagen doorlopen naar Nederland.")
    print("Dit zijn de dagen dat je elkaar nodig hebt merken jullie")
    print("en het is niet zo vreemd dat jullie steeds positiever worden over dat jullie het hebben gehaald.")
    print("Tot dat jullie over de grens komen en zien hoe het eraan toe gaat in ter Apel.")
    print(" Jullie asielprocedure kan wel snel van start gaan omdat jullie goede papieren hebben")
    print("maar verdraag je het dat andere buiten in de regen en kou moeten slapen.")
    print("Het is aan jou A: wil je verder gaan en een ander land zoeken of B: wil je hier gaan wonen.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal19()
        elif d == "B" or d == "b":
            verhaal20()

def verhaal18():
    print("Aangekomen in Munchen is het niet super ver meer")
    print("en je hebt zoals je van mensen hebt begrepen nog maar hoog uit 9 dagen doorlopen naar Nederland.")
    print("Dit zijn de dagen dat je elkaar nodig hebt merken jullie")
    print("en het is niet zo vreemd dat jullie steeds positiever worden over dat jullie het hebben gehaald.")
    print("Tot dat jullie over de grens komen en zien hoe het eraan toe gaat in ter Apel.")
    print(" Jullie asielprocedure kan wel snel van start gaan omdat jullie goede papieren hebben")
    print("maar verdraag je het dat andere buiten in de regen en kou moeten slapen.")
    print("Het is aan jou A: wil je verder gaan en een ander land zoeken of B: wil je hier gaan wonen.")
    while True:
        d = input("wat is jouw keuze? A of B: ")
        if d == "A" or d == "a":
            verhaal19()
        elif d == "B" or d == "b":
            verhaal20()

def verhaal19():
    print("Je reist verder en het is nog niet zeker waar je nu echt heen wilt.")
    print("kies A om opnieuw te spelen kies B om te stoppen")
    while True:
        d = input("wat is jouw keuze?")
        if d == "A" or d =="a":
            verhaal1()
        elif d == "B" or d == "b":
            print("bedankt voor het spelen!")
            STOP

def verhaal20():
    print("je bent veilig en je hoeft je niet meer druk te maken")
    print("kies A om opnieuw te spelen kies B om te stoppen")
    while True:
        d = input("wat is jouw keuze?")
        if d == "A" or d =="a":
            verhaal1()
        elif d == "B" or d == "b":
            print("bedankt voor het spelen!")
            STOP

def verhaal21():
    print("Je wordt teruggestuurd naar je eigen land")
    time.sleep(.5)
    print("kies A om opnieuw te spelen kies B om te stoppen")
    while True:
        d = input("wat is jouw keuze?")
        if d == "A" or d =="a":
            verhaal1()
        elif d == "B" or d == "b":
            print("bedankt voor het spelen!")
            STOP

def verhaal22():
    print("Je gaat dood, dit was misschien toch geen verstandige keuze geweest.")
    time.sleep(.5)
    print("kies A om opnieuw te spelen kies B om te stoppen")
    while True:
        d = input("wat is jouw keuze?")
        if d == "A" or d =="a":
            verhaal1()
        elif d == "B" or d == "b":
            print("bedankt voor het spelen!")
            STOP

verhaal1()