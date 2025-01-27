def triple_number(n):
    return n * 3

def print_triple_number(n):
    print(triple_number(n))

def say_hello():
    print("Hello")

if __name__ == "__main__":
    print(triple_number(5))  # prints 15
    print(triple_number(10))  # prints 30
    print(triple_number(15))  # prints 45

    a = 2
    b = triple_number(a)
    c = triple_number(a)
    d = triple_number(a) + triple_number(c)
    print(d)  # prints 24 (6 + 18)
    print_triple_number(d) # prints 72
    say_hello()  # prints Hello
