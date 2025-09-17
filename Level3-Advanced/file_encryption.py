def encrypt(text, shift=3):
    result = ""
    for char in text:
        if char.isalpha():
            base = 'A' if char.isupper() else 'a'
            result += chr((ord(char) - ord(base) + shift) % 26 + ord(base))
        else:
            result += char
    return result

def decrypt(text, shift=3):
    return encrypt(text, -shift)

def encrypt_file(input_file, output_file, shift=3):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        encrypted = encrypt(content, shift)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(encrypted)
        print(f"File '{input_file}' encrypted → '{output_file}'")
    except FileNotFoundError:
        print("Error: File not found.")

def decrypt_file(input_file, output_file, shift=3):
    try:
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        decrypted = decrypt(content, shift)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(decrypted)
        print(f"File '{input_file}' decrypted → '{output_file}'")
    except FileNotFoundError:
        print("Error: File not found.")

choice = input("Enter 'e' to encrypt or 'd' to decrypt: ").lower()
if choice == "e":
    infile = input("Enter file to encrypt: ")
    outfile = input("Enter output file name: ")
    encrypt_file(infile, outfile)
elif choice == "d":
    infile = input("Enter file to decrypt: ")
    outfile = input("Enter output file name: ")
    decrypt_file(infile, outfile)
else:
    print("Invalid choice")
