import re
import os  # import the os module

def urls(file_path): 
    urls = []
    url_regex = r"(https?://(?:www\.)?\w+\.\w+)"
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(url_regex, line)
            urls.extend(matches)
    return urls

def main():
    file_path = input("Enter the path to the text file: ")
    if os.path.exists(file_path):  # Check file existence
        found_urls = urls(file_path)
        if found_urls:
            print("URLs found in the file:")
            for url in found_urls:
                print(url)
        else:
            print("No URLs found in the file.")
    else:
        print("File not found. Please enter a valid file path.")  # Notify if file not found

if __name__ == "__main__":
    main()