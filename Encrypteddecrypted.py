def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# User Input
message = input("Enter Message: ")
shift = int(input("Enter Shift Value: "))

encrypted_text = encrypt(message, shift)
decrypted_text = decrypt(encrypted_text, shift)

print("\nEncrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
