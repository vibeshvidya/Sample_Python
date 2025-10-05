employee=dict(name="Anju",age=22,city="Bangalore")
print (employee)
print(len(employee))
print(employee["name"])
print(employee.get("age"))
employee["salary"]=50000
print(employee)
employee["age"]=23
print(employee)
employee.pop("city")
print(employee)
employee.clear()
print(employee)

z=employee.items()
print(z)

employee={"name":"Anju","age":22,"city":"Bangalore"}
print(employee)
employee.update({"age":23})
print(employee)

employee.update({"salary":50000})
print(employee)

employee.popitem()
print(employee)

employee.pop("age")
print(employee)

#del employee["name"]
#print(employee)

#del employee
#print(employee)

employee.clear()
print(employee)

employee={"name":"Anju","age":22,"city":"Bangalore"}
print(employee)

employee.clear()
print(employee)

employee['fname']='Anju'
print(employee)

employee['lname']='Kumar'
employee['age']=22
employee['city']='Bangalore'
print(employee)

employees={
    "emp1":{"name":"Anju","age":22,"city":"Bangalore"},
    "emp2":{"name":"Ravi","age":25,"city":"Chennai"},
    "emp3":{"name":"Sita","age":24,"city":"Mumbai"}
    }
print(employees)
print(employees["emp3"])
print(employees["emp3"]["name"])



