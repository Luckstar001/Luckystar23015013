filename = input("Enter a text Pls: ")
with open("text.txt","w")as file:
    content = file.write(filename)
    print(f"Total words in the file:{content}:")