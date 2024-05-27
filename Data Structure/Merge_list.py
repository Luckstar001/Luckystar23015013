def merge_lists():
    list_1 = input("Please enter list_1 items, with spaces: ").split()
    list_2 = input("Please enter list_2 items, with spaces: ").split()
    merged_list = list(set(list_1 + list_2))
    merged_list.sort()
    return merged_list
print(merge_lists())