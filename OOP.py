
from pickle import FALSE, TRUE
from Pes import Pes
from VesnickyPodvratak import VesnickyPodvratak

#definovani bez konstruktoru
alik = Pes()
alik.vaha = 10
alik.rasa = "Kokspanel"
alik.bouda = True

print(alik,alik.vaha,alik.rasa,alik.bouda)

#konstruktor
Abby = Pes(3, "cinsky pinc")
Kessie = Pes(3, "jorksir", FALSE)
Brumbal = Pes(10 , "ovcak" , TRUE)

print(Abby.bouda,Kessie.bouda,Brumbal.bouda)

print(str(Abby))

print(str(Kessie))

print(Brumbal)


Rony = VesnickyPodvratak(12, "chuchelnak", True,3)
print(rony.stekni())


