# Global Scope, e can be used anywhere in the program
e = 3

def print_e():
    # Local Scope, test can only be used in this function
    test = 10
    print(e)

if __name__ == "__main__":
    print_e()  # prints 3
    # print(test) # NameError: name 'test' is not defined
