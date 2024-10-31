MORSE_Ronit = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

# Function to encrypt the String data
def encrypt(message):
    cipher = ''
    for letter in message:
        if letter != ' ':
            cipher += MORSE_Ronit.get(letter, '') + ' '  # Get Morse code for each letter
        else:
            cipher += ' '  # Space between words
    return cipher.strip()

# Function to decrypt the string
def decrypt(message):
    message += ' '
    decipher = ''
    citext = ''
    space_count = 0

    for letter in message:
        if letter != ' ':
            space_count = 0
            citext += letter
        else:
            space_count += 1
            if space_count == 2:  # New word
                decipher += ' '
            else:
                decipher += next((k for k, v in MORSE_Ronit.items() if v == citext), '')
                citext = ''
    return decipher.strip()

def main():
    message = input("Enter text to encode (regular text) or decode (Morse code): ")
    
    # Check if input is Morse code (contains only dots, dashes, and spaces)
    if all(char in ".- " for char in message):
        # Assume it's Morse code and decode it
        result = decrypt(message)
        print("Decoded Message:", result)
    else:
        # Assume it's regular text and encode it to Morse code
        result = encrypt(message.upper())
        print("Encoded Morse:", result)

if __name__ == '__main__':
    main()
