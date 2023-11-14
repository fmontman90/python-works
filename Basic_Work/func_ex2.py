#creation of funtion
def hello_world():
    print("Hello, there")# body of function what it is intent to do                                                                                                          

#Funtion call executes whatever the body is 
hello_world()

def print_name(name):
    print(f"Name is {name}")

print_name("KIT")

def add_two(num):
    return num + 2

result = add_two(5)
print(result)