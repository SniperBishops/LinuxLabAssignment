import sys

def caesar_cipher(message, shift):
    # Convert message to uppercase
    message = message.upper()
    # Initialize an empty string to hold the encoded message
    encoded_message = ""
    # Iterate over each character in the message
    for char in message:
        # If the character is a letter
        if char.isalpha():
            # Shift the character by the specified amount
            encoded_char = chr((ord(char) - 65 + shift) % 26 + 65)
            # Append the encoded character to the encoded message
            encoded_message += encoded_char
    # Group the encoded message into blocks of 5 letters, 10 blocks per line
    blocks = [encoded_message[i:i+5] for i in range(0, len(encoded_message), 5)]
    lines = [blocks[i:i+10] for i in range(0, len(blocks), 10)]
    # Print the encoded message
    for line in lines:
        for block in line:
            print(block, end=" ")
        print()

if __name__ == '__main__':
    # Read in the shift amount from the command line
    shift = int(sys.argv[1])
    # Read in the message from stdin
    message = input()
    # Encode the message using the Caesar Cipher
    caesar_cipher(message, shift)
