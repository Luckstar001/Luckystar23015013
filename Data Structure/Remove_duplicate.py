def remove_duplicates(input_list):
    unique_elements = []
    for item in input_list:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements
user_list = input('please input your listed items: ').split()
result = remove_duplicates(user_list)
print('your list is: ', result)