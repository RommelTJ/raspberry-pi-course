if __name__ == "__main__":
    # Integers
    number = 12
    print(number)  # prints 12
    number = -3
    print(number)  # prints -3

    # Floats
    temperature = 25.3
    print(temperature)  # prints 25.3

    # Strings
    name = "Rommel"
    print(name)  # prints Rommel

    # Booleans
    is_raining = True
    print(is_raining)  # prints True

    print(type(number))  # prints <class 'int'>
    print(type(temperature))  # prints <class 'float'>
    print(type(name))  # prints <class 'str'>
    print(type(is_raining))  # prints <class 'bool'>

    # Dynamic typing
    a = 4
    print(type(a))  # prints <class 'int'>
    a = "hello"
    print(type(a))  # prints <class 'str'>

    wifi_name: str = "your wifi"
    print(wifi_name)  # prints 'your wifi'
