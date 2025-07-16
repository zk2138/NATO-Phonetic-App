# NATO Phonetic Alphabet App

A simple Python GUI application that converts typed words into the NATO Phonetic Alphabet and speaks them aloud using text-to-speech.

## 🔤 What It Does

This app takes a word entered by the user and translates each letter into its corresponding NATO phonetic alphabet word.  
For example:  
**HELLO** → `H - Hotel | E - Echo | L - Lima | L - Lima | O - Oscar`

## 🔤 Features

- Converts any word to its NATO phonetic representation
- Speaks the converted words using built-in TTS (`pyttsx3`)
- Volume control with a slider (default 50%)
- Press **Enter** or click **Convert** to translate the word
- Click **Speak** to hear the phonetic version
- **Clear** button resets input and output

## 🧩 How It Works

Each letter of the input is mapped to its NATO phonetic equivalent using a predefined dictionary. Only alphabetic characters are processed, and the formatted result is displayed within the GUI window. 

## ✅ Requirements

- Python 3.6+
- `pyttsx3` for offline text-to-speech
- Tkinter (usually included by default)


Install required dependencies with:

```bash
pip install pyttsx3
```


## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/zk2138/NATO-Phonetic-App.git
   cd NATO-Phonetic-App
   ```

2. **Run the application:**
   ```bash
   python nato_phonetic_alphabet_app_gui.py
   ```

> Make sure Python 3 is installed on your system. Tkinter comes pre-installed with most standard Python distributions.

## 📂 File Structure

```
NATO-Phonetic-App/
├── nato_phonetic_alphabet_app_gui.py      # Main GUI application
├── README.md                              # Project documentation
└── LICENSE                                # Project license (MIT)
```

## 📸 Screenshot

<img width="502" height="362" alt="image" src="https://github.com/user-attachments/assets/a0715401-e610-4db6-a963-d3ec898ebb59" />


## 🗺️ NATO Phonetic Alphabet Reference

| Letter | Code Word |
|--------|-----------|
| A      | Alpha     |
| B      | Bravo     |
| C      | Charlie   |
| D      | Delta     |
| E      | Echo      |
| F      | Foxtrot   |
| G      | Golf      |
| H      | Hotel     |
| I      | India     |
| J      | Juliett   |
| K      | Kilo      |
| L      | Lima      |
| M      | Mike      |
| N      | November  |
| O      | Oscar     |
| P      | Papa      |
| Q      | Quebec    |
| R      | Romeo     |
| S      | Sierra    |
| T      | Tango     |
| U      | Uniform   |
| V      | Victor    |
| W      | Whiskey   |
| X      | X-ray     |
| Y      | Yankee    |
| Z      | Zulu      |


## 🔧 Customization

Speech speed: Adjust via `engine.setProperty('rate', 170)`

Default volume: Set by `volume_slider.set(50)`

## 🙌 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with improvements or new features.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Made with 💻 by [zk2138](https://github.com/zk2138)
