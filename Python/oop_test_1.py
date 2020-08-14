class PartyAnimal:
   x = 0

#__init__ metode tiks izpildīta tikai vienu reizi, veidojot (katru) instanci
   def __init__(self):
     print('I am constructed')
     self.x=0 #šis ir objekta x, tādēļ jāraksta self.
   
   def party(self) :
     self.x = self.x + 1
     print("So far x property of object",\
           "is", self.x)

   def __del__(self):
     print('I am destructed', self.x)
     #kopā ir __init__ nestrādā, jo kopā neattēlo
     
print("Before an = PartyAnimal()")
#print(vars())
an = PartyAnimal()
#an.__init__()
#an2 = PartyAnimal()
print("After an = PartyAnimal()")
#print(vars())
#print("an data type:", type(an))
#print("an methods and properties:", dir(an))
#mantotas no sistēmas
#print("an x property data type:", type(an.x))
#print("an party method data type:", type(an.party))
print(vars(an))
 # tikai ja klase ar __init__ un self.x=..., tad ir {'x': 0}, savādāk ir {}

print("\nBefore first an.party()")
an.party()
print("After first an.party()")
#print(vars(an)) #objekts "aiztikts" {'x': 1}

an.x = 100
an.__init__()

print("\nBefore second an.party()")
an.party()
print("After second an.party()")

an.x = 200

print("\nBefore third an.party()")
an.party()
print("After third an.party()")

print("\nBefore one more party()")
PartyAnimal.party(an)
print("After one more party()")

# Code: http://www.py4e.com/code3/party2.py

#print(an.x)
#print(an2.x)
