import sys

CHAR_TO_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-',
    'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', ' ': '/',
}

def encode_to_morse(input_text):
    try:
        if not isinstance(input_text, str):
            raise AssertionError("Invalid input. Usage: python3.10 morse_encoder.py <text>")

        if not input_text.strip():
            return ""

        morse_text = []
        for char in input_text.upper():
            if char in CHAR_TO_MORSE:
                morse_text.append(CHAR_TO_MORSE[char])
            
        return ' '.join(morse_text)
    
    except KeyError as e:
        raise AssertionError(f"Unsupported character: {str(e)}")

def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("Invalid number of arguments. Usage: python3.10 morse_encoder.py <text>")
        
        input_text = sys.argv[1]
        morse_result = encode_to_morse(input_text)
        print(morse_result)
    
    except AssertionError as error:
        print(error)

if __name__ == "__main__":
    main()


