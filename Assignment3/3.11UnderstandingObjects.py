'''
1.Write a class called Address that has two attributes: number and street name. Make sure you have an init method that initializes the object appropriately.
'''
class Address:
    def __init__(self,number,streetName): # Parameterized constructor
        self.number=number
        self.streetName=streetName
        print("Number :",number,"\nStreetName :",streetName)
a=Address(20,"Umiya Campus")    # Creation ob Instance

