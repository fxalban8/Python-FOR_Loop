countries=["Argelia","Argentina","Antigua y Barbuda", "Bruselas","Belgica","Costa Rica", "Chipre","Dinamarca"]
#let's create another list only with the countries starting with the letter B
countries_starting_with_B=[]
for element in countries: #for each element in the list countries
    if "B" in element:
        countries_starting_with_B.append(element) #append allows to incorporate another element
        

print(countries_starting_with_B)
