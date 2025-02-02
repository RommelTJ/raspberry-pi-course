if __name__ == "__main__":
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(number_list) # Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
    print(number_list[0]) # Prints "1"
    print(number_list[-1]) # Prints "10"
    number_list.append(11)
    print(number_list[-1]) # Prints "11"
    print(len(number_list)) # Prints "11"

    # You can mix types in a list, but you shouldn't do it.
    bad_list = [1, "2", 3.2]
    print(bad_list)

    # You can also loop with a list
    [print(i) for i in number_list]
