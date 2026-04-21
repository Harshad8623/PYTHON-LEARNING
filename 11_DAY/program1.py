import random
import string

def encode_message(message):
    result1 = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    result2 = ''.join(random.choice(string.ascii_letters) for _ in range(3))

    new = result1 + message[1:] + message[0] + result2
    return new

def decode_message(encoded_message):
    # Remove first 3 and last 3 random characters
    core = encoded_message[3:-3]

    # Last character is original first character
    original = core[-1] + core[:-1]
    return original



if __name__ == "__main__":
    original_message = "HelloWorld"

    encoded = encode_message(original_message)
    print("Encoded Message:", encoded)

    decoded = decode_message(encoded)
    print("Decoded Message:", decoded)