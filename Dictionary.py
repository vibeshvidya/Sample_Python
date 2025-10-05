car={
    "brand": "Toyota",
    "model": "Corolla",   
    "year": 2020
    }
print(len(car))
print(car["brand"])
print(car.get("model")) 
car["color"]="Red"
print(car)
car["year"]=2021
print(car)
car.pop("model")
print(car)
car.clear()
print(car)