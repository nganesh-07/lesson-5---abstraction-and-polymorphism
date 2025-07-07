class india():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi is the most commonly spoken language in the country.")

    def animal(self):
        print("The national animal of this country is a tiger.")

class america():
    def capital(self):
        print("Washington DC is the capital of the United Stats.")

    def language(self):
        print("The most commonly spoken language in the country is English.")
    
    def animal(self):
        print("The country's national animal is an eagle.")


obj_ind = india()
obj_america = america()


# common interface of both
for country in (obj_ind, obj_america):
    country.capital()
    country.language()
    country.animal()