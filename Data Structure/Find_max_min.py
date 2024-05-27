def find_max_min():
    numb = input("Please input your numbers with space not punctuation mark: ").split()
    numb = [int(num) for num in numb]
    if not numb:
        print("No numbers were entered.")
        return None
    max_num = max(numb)
    min_num = min(numb)
    return max_num, min_num
result = find_max_min()
if result:
    max_num, min_num = result
    print(f"Maximum number is: {max_num}")
    print(f"Minimum number is: {min_num}")
    print("thank you")