file_name = input("Enter the file name: ")

try:
    with open(file_name, 'r') as file:
        text = file.read()
        words = text.split()
        print(f"Number of words: {len(words)}")
except FileNotFoundError:
    print("File not found!")
