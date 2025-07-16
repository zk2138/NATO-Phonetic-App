import tkinter as tk
import pyttsx3
import threading
import time

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

# Globals
current_phonetics = []
speaking = False
stop_signal = False


# Convert Text to NATO and display
def convert_to_nato(event=None):
    global current_phonetics
    input_text = entry.get().upper()
    current_phonetics = []
    formatted_output = []

    words = input_text.split()
    for word in words:
        phonetic_word = []
        formatted_word = []
        for letter in word:
            if letter.isalpha():
                phonetic = NATO_ALPHABET[letter]
                phonetic_word.append(phonetic)
                formatted_word.append(f"{letter} - {phonetic}")
        if phonetic_word:
            current_phonetics.append(phonetic_word)
            formatted_output.append(" | ".join(formatted_word))

    result_label.config(text="\n".join(formatted_output))


# Speak using a thread
def speak_worker():
    global speaking, stop_signal
    speaking = True
    stop_signal = False

    for phonetic_word in current_phonetics:
        if stop_signal:
            break
        for word in phonetic_word:
            if stop_signal:
                break
            # Real-time volume control
            # Get volume from Slider (0-100 mapped to 0.0-1.0)
            volume = volume_slider.get() / 100
            engine.setProperty('volume', volume)
            engine.say(word)

            engine.startLoop(False)
            while engine.isBusy():
                if stop_signal:
                    engine.stop()
                    break
                engine.setProperty('volume', volume_slider.get() / 100)
                engine.iterate()
                time.sleep(0.05)
            engine.endLoop()
        time.sleep(0.3)  # Pause between words

    speaking = False
    stop_signal = False


# Speak current NATO words using text-to-speech
def speak_nato():
    if speaking or not current_phonetics:
        return
    threading.Thread(target=speak_worker, daemon=True).start()


def stop_speaking():
    global stop_signal
    stop_signal = True


# Clear input, result and stored phonetics
def clear_all():
    global current_phonetics
    stop_speaking()
    entry.delete(0, tk.END)
    result_label.config(text="")
    current_phonetics = []


# Create the GUI window
root = tk.Tk()
root.title("NATO Phonetic Converter")
root.geometry("500x420")

# Create input field
label = tk.Label(root, text="Enter a word or phrase:")
label.pack(pady=5)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)
entry.bind("<Return>", convert_to_nato)  # Bind Return (Enter)  key to convert

# Button frame (side-by-side Convert, Speak and Stop)
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

convert_button = tk.Button(button_frame, text="Convert", command=convert_to_nato)
convert_button.pack(side="left", padx=10)

speak_button = tk.Button(button_frame, text="Speak", command=speak_nato)
speak_button.pack(side="left", padx=10)

stop_button = tk.Button(button_frame, text="Stop", command=stop_speaking)
stop_button.pack(side="left", padx=10)

# Clear button below the Clear and Speak buttons
clear_button = tk.Button(root, text="Clear", command=clear_all)
clear_button.pack(pady=5)

# Display result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=480, justify="left")
result_label.pack(pady=10)

# Volume control
volume_label = tk.Label(root, text="Volume")
volume_label.pack()

volume_slider = tk.Scale(root, from_=0, to=100, orient="horizontal")
volume_slider.set(50)
volume_slider.pack(pady=5)

# Start GUI
root.mainloop()
