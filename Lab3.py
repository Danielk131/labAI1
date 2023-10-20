from faker import Faker
import pandas as pd
from faker.providers.credit_card import Provider as CreditCardProvider

#Lager en falsk liste med norske verdier
fake = Faker(['no_NO'])

"Lager en panda liste med Disse under som kolonner"
df = pd.DataFrame(columns=["Navn", "Adresse", "PersonNr", "CreditCard", "ipv4"])

"Lager en liste med 100 elementer med falske navn"
for i in range(100):
    row = fake.name(), fake.address(), fake.ssn(), fake.credit_card_number(), fake.ipv4()
    df.loc[i]=row

textArray = [] #Create a empty array
# Do a for loop, and assign values to name and adress
for i in range(10):
    row = df.iloc[i]
    name = row[0]
    adress = row[1]
    ssn = row[2]
    cc = row[3]
    #Using f string we can now create a new string with the values, and
    #append (add) that string to the text array
    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {adress}. My credit card nr is {cc} and my ssn is {ssn}')

for index, row in df.iterrows():
    name = row[0]
    address = row[1]
    ssn = row[2]
    cc = row[3]
    #Using f string we can now create a new string with the values, and
    #append (add) that string to the text array
    textArray.append(f'Hi, my name is {name}. I wonder if you deliver to {address}')

print(textArray)