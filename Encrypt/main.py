# PART 1

def adjusted_key(text, key):
    adjustedkey = ""
    for i in range(len("".join(i for i in text if i.isalpha()))):
        adjustedkey += key[i % len(key)]
    return adjustedkey

def encrypt_vigenere():
    text = input("Enter text: ").lower()
    key = input("Enter key: ").lower()
    encrypted_text = ""
    index = 0
    for character in text:
        if character.isalpha():
    	    encrypted_text += chr((ord(character) + ord(adjusted_key(text, key)[index]) - 194) % 26 + 97)
    	    index += 1
        else:
    	    encrypted_text += character
    return encrypted_text
    
print(encrypt_vigenere())
