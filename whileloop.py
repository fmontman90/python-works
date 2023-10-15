count = 1
while count <=3:
    print("I enjoy work.. or do I?")
    count += 1

count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1

    #range example
print("This is the range of 5")
for i in range(5):
    print(i)
