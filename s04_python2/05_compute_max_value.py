def find_max(number_list: list[int]) -> int:
    max_value = number_list[0]
    for i in number_list:
        if i > max_value:
            max_value = i
    return max_value

if __name__ == "__main__":
    number_list = [1, 5, -6, 12, 7]
    print(find_max(number_list))
