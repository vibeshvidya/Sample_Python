acc_balance=5000
withdra=2000
if withdra<=acc_balance:
    balance=acc_balance-withdra
    print(f"Transaction successful.{withdra} has beed debited from your account. Balance amount in your account is {balance}")
else:
    print("Insufficient balance")

user="admin"
password="admin123"
if user=="admin" and password=="admin123":
    print("Login successful")
else:
    print("Invalid credentials")

a=40
if a>30:
    print("a is greater than 30")
elif a>20:
    print("a is greater than 20")
elif a>10:
    print("a is greater than 10")
elif a==10:
    print("a is equal to 10")
else:
    print("a is less than 10")

#check-in-time on/before 9-> "ON TIME"
#check-in-time after 9 and on/before 9:15-> "LATE"
#check-in-time after 9:15-> "PENALTY"
#check-in-time after 10-> "ABSENT"

check_in_time=input("Enter your check-in time:")
check_in_time=float(check_in_time)
if check_in_time<=9:
    print("ON TIME")
elif check_in_time>9 and check_in_time<=9.15:
    print("LATE")
elif check_in_time>9.15 and check_in_time<=10:
    print("PENALTY")
else:
    print("ABSENT")






