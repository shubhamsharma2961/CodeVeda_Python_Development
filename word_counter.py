try:
    filename = input("Enter the file name: ")
    f = open(filename, "r")
    text = f.read()
    f.close()

    words = text.split()
    print("Number of words in the file:", len(words))

except FileNotFoundError:
    print("Error: File not found. Please check the file name.")
