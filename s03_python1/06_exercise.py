def concatenate_strings(str1, str2):
    return f"{str1} {str2}".upper()

if __name__ == "__main__":
    result = concatenate_strings("Hello", "World")
    print(result)  # prints 'HELLO WORLD'
