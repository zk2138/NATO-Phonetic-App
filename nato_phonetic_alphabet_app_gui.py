import tkinter as tk
from tkinter import messagebox

NATO_ALPHABET = {
    'A': 'Alpha', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett', 'K': 'Kilo', 'L': 'Lima', 'M': 'Mike',
    'N': 'November', 'O': 'Oscar', 'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

def convert_to_nato():
    word = entry.get().upper()
    result = [f"{letter} - {NATO_ALPHABET.get(letter, letter)}" for letter in word if letter.isalpha()]
    result_label.config(text=" | ".join(result))

# Create the GUI window
root = tk.Tk()
root.title("NATO Phonetic Converter")
root.geometry("400x200")

# Create input field and button
label = tk.Label(root, text="Enter a word:")
label.pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
button = tk.Button(root, text="Convert", command=convert_to_nato)
button.pack(pady=5)

# Display result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

root.mainloop()
