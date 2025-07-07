class BMW():
    def mileage(self):
        print("BMW mileage: 18")
    def models(self):
        print("There are several BMW models, few good ones.")
    def publicview(self):
        print("BMWs are deemed above satisfactory by the general public.")

class ferrari():
    def mileage(self):
        print("Ferrari mileage: 23")
    def models(self):
        print("There are few Ferrari models, all are good.")
    def publicview(self):
        print("Ferraris are deemed fancy and unattainable by the general public.")

obj_bmw = BMW()
obj_ferrari = ferrari()

for car in (obj_bmw, obj_ferrari):
    car.mileage()
    car.models()
    car.publicview()