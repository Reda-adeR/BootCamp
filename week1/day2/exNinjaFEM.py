MORSE_CODE = {
    'A': '.-',    'B': '-...',  'C': '-.-.', 'D': '-..',  'E': '.',    'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',   'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',  'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---','3': '...--','4': '....-',
    '5': '.....', '6': '-....', '7': '--...','8': '---..','9': '----.',
    ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE.items()}

def to_morse(text):
    return ' '.join(MORSE_CODE[c.upper()] for c in text if c.upper() in MORSE_CODE)


def from_morse(code):
    return ''.join(REVERSE_MORSE[c] for c in code.split())


msg = "hello world"
morse = to_morse(msg)
print("To Morse:", morse)

text = from_morse(morse)
print("From Morse:", text)
