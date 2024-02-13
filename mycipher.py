import sys

def caesar_cipher(message, shift):
    encrypted_message = ''
    for char in message:
        if char.isalpha():
            encrypted_char = chr(((ord(char) - 65 + shift) % 26) + 65)
            encrypted_message += encrypted_char
    return encrypted_message

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 mycipher.py <shift>")
        return

    shift = int(sys.argv[1]) % 26

    print("Enter your message:")
    message = sys.stdin.readline().strip().upper()

    encrypted_message = caesar_cipher(message, shift)

    block_size = 5
    for i in range(0, len(encrypted_message), block_size):
        print(encrypted_message[i:i+block_size], end=' ')
    print()

if __name__ == "__main__":
    main()

