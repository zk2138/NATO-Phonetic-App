import tkinter as tk
import pyttsx3

# NATO Phonetic Alphabet Dictionary
NATO_ALPHABET = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike',
    'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

# Init text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 170)  # Adjust speaking rate

# Keep track of the current phonetic words
current_phonetics = []


# Convert Text to NATO and speak it
def convert_to_nato(event=None):
    global current_phonetics
    word = entry.get().upper()
    result = []
    current_phonetics = []

    for letter in word:
        if letter.isalpha():
            phonetic = NATO_ALPHABET[letter]
            result.append(f"{letter} - {phonetic}")
            current_phonetics.append(phonetic)

    result_label.config(text=" | ".join(result))


# Speak current NATO words using text-to-speech
def speak_nato():
    if not current_phonetics:
        return

    # Get volume from Slider (0-100 mapped to 0.0-1.0
    volume = volume_slider.get() / 100
    engine.setProperty('volume', volume)

    for word in current_phonetics:
        engine.say(word)
    engine.runAndWait()


# Clear input, result and stored phonetics
def clear_all():
    global current_phonetics
    entry.delete(0, tk.END)
    result_label.config(text="")
    current_phonetics = []


# Create the GUI window
root = tk.Tk()
root.title("NATO Phonetic Converter")
root.geometry("500x330")

# Create input field
label = tk.Label(root, text="Enter a word:")
label.pack(pady=5)

entry = tk.Entry(root)
entry.pack(pady=5)
entry.bind("<Return>", convert_to_nato)  #Bind enter key to convert

# Button frame (side-by-side Convert and Speak)
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

convert_button = tk.Button(button_frame, text="Convert", command=convert_to_nato)
convert_button.pack(side="left", padx=10)

speak_button = tk.Button(button_frame, text="Speak", command=speak_nato)
speak_button.pack(side="left", padx=10)

# Clear button below the Clear and Speak buttons
clear_button = tk.Button(root, text="Clear", command=clear_all)
clear_button.pack(pady=5)

# Display result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=480, justify="center")
result_label.pack(pady=10)

# Volume control
volume_label = tk.Label(root, text="Volume")
volume_label.pack(pady=5)

volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
volume_slider.set(50)
volume_slider.pack(pady=5)

# Start GUI
root.mainloop()
