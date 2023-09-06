#Command to run: python lab2.py 
print("Shift Cypher")
print("Only alphabetic and white spaces should be used in the message.")
message = input("Enter a message to encrypt: ")
message = message.lower()

while True:
    try:
        key = int(input("Enter an encryption key: "))
        break
    except ValueError:
        print("Enter an integer for the key.")

def encrypt(message, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    updatedKey = key%len(alphabet)
    encodedMessage = ""
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                if (j + updatedKey) >= len(alphabet):
                    tempKey = j + updatedKey - len(alphabet)
                    encodedMessage = encodedMessage + alphabet[tempKey]
                else:
                    encodedMessage = encodedMessage + alphabet[j + updatedKey]
    return encodedMessage

encodedMessage = encrypt(message, key)
print("Encoded Message: " + encodedMessage)

def decrypt(encodedMessage, key):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
    updatedKey = key%len(alphabet)
    decryptMessage = ""
    for i in range(len(encodedMessage)):
        for j in range(len(alphabet)):
            if encodedMessage[i] == alphabet[j]:
                if (j - updatedKey) <= 0:
                    tempKey = len(alphabet) + (j - updatedKey)
                    decryptMessage = decryptMessage + alphabet[tempKey]
                else:
                    decryptMessage = decryptMessage + alphabet[j - updatedKey]
    return decryptMessage

decodedMessage = decrypt(encodedMessage, key)
print("Decrypted Message: " + decodedMessage)