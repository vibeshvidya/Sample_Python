#loops

# For loop
for i in range(5):
    print("Iteration:", i)

# While loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# Nested loops
for i in range(3):
    for j in range(2):
        print("i:", i, "j:", j)

# Loop with break
for i in range(10):
    if i == 5:
        break
    print("Breaking at:", i)
# Loop with continue
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i) 

