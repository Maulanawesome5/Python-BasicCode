# Function dengan argument / parameter / input


# Function 1
def hello_world(nama):
    print(f"Halo saudara {nama}")

hello_world("Ucup")

# Function 2
def tambah(number1, number2):
    result = number1 + number2
    print(f"{number1} + {number2} = {result}")

tambah(5, 3)

# Function 3
def say_hello(person):
    result = person.copy()
    for people in result:
        print(f"Yang Terhormat {people}")

member = ["Ucup", "Denis", "Adit"]
say_hello(member)
