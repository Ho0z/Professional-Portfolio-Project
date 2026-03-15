morse_code = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", "\"": ".-..-.",
    "$": "...-..-", "@": ".--.-.",

    " ": "/" 
}
reverse_morse = {v: k for k, v in morse_code.items()}

game= True
while game is True:
    start = input("What would you like to convert? \nMorse Code or text?").lower()
    
    if start == "text":
        text = input("Please enter the text you want to convert: ").upper()
        morse_sentence = ""
        for char in text:
            if char in morse_code:
                morse_sentence += morse_code[char] + " "
        print(morse_sentence)

    elif start == "morse":
        code = input("Enter Morse code (use spaces between letters): ")
        decoded_sentence = ""
        for morse_char in code.split(" "):
            decoded_sentence += reverse_morse.get(morse_char, "?")
        print(decoded_sentence)
        
    else:
        print("Sorry worng input")

