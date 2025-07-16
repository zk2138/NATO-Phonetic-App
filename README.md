# 🗣️ NATO Phonetic Alphabet Converter (GUI)

A Python GUI application that converts user input into the NATO Phonetic Alphabet and speaks it aloud with full control over speech playback and volume.

---

## 🔤 What It Does

This app lets users enter any word or phrase and translates each letter into its NATO phonetic equivalent.  
Then, it speaks the translation aloud using offline text-to-speech (via `pyttsx3`).

> **Example:**  
**HELLO** → `H - Hotel | E - Echo | L - Lima | L - Lima | O - Oscar`

---

## ✨ Features

- ✅ Converts input to NATO phonetic alphabet
- 🗣️ Speaks results aloud using offline TTS (`pyttsx3`)
- 🎚️ Real-time volume control (0%–100%)
- ⏹️ Stop button interrupts speech instantly
- ↩️ Press **Enter** or click **Convert** to process input
- ▶️ Click **Speak** to start reading the phonetic version
- 🧹 **Clear** resets all fields

---

## 🧩 How It Works

1. The app maps each alphabetic character in the input to its NATO phonetic equivalent.
2. The formatted output is displayed in the GUI.
3. When **Speak** is pressed:
   - Each phonetic word is spoken aloud.
   - Volume can be adjusted in real time.
   - If **Stop** is pressed, playback halts and resets cleanly.
4. The next **Speak** always starts from the beginning.

---

## 🖥️ Requirements

- Python 3.6+
- [`pyttsx3`](https://pypi.org/project/pyttsx3/) for offline text-to-speech
- `tkinter` (usually included with Python)

Install dependencies with:

```bash
pip install pyttsx3
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/zk2138/NATO-Phonetic-App.git
cd NATO-Phonetic-App
```

### 2. Run the application

```bash
python nato_phonetic_alphabet_app_gui.py
```

> Make sure Python 3 is installed on your system. `tkinter` is included with most standard Python distributions.

---

## 📂 File Structure

```
NATO-Phonetic-App/
├── nato_phonetic_alphabet_app_gui.py   # Main GUI application
├── README.md                           # Project documentation
└── LICENSE                             # MIT License
```

---

## 🎛️ Interface Overview

- **Input Field**: Type your word or phrase
- **Convert**: Display NATO translation
- **Speak**: Read out phonetics aloud
- **Stop**: Immediately stop speaking
- **Clear**: Reset everything
- **Volume Slider**: Live volume adjustment

---

## 📸 Screenshot

<img width="502" height="452" alt="image" src="https://github.com/user-attachments/assets/9d42b191-6d56-41c1-a734-2c758f5a1439" />


---

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

---

## ⚙️ Customization Tips

- **Speech speed**:
  ```python
  engine.setProperty('rate', 170)  # Adjust rate as desired
  ```

- **Default volume**:
  ```python
  volume_slider.set(50)  # Default 50% volume
  ```

---

## ❗ Known Limitation

- If the **Stop** button is used during speech, the next time **Speak** is clicked, playback **starts from the second letter**, skipping the first.
- The **Speak** feature works reliably only when it can finish uninterrupted.

---

## 🙌 Contributing

Contributions welcome!  
Feel free to fork the repository and submit a pull request with improvements, bug fixes, or new features.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

Made with ❤️ by [zk2138](https://github.com/zk2138)
