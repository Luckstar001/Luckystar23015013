source = input("Enter name of the source file: ")
with open("text.txt","r")as file:
    content = file.read()
    destination = input("Enter the name of the destination file: ")
    with open(destination,"w")as file:
        copied = file.write(content)
        print("copied Successful ")