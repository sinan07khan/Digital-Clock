# Digital Clock using Python and Tkinter

A simple digital clock application built with Python and Tkinter. It displays the current time in real time and allows users to switch between 12-hour and 24-hour formats using the keyboard.

## Features

- Displays the current time in hours, minutes, and seconds.
- Supports both 12-hour and 24-hour time formats.
- Shows AM/PM in 12-hour mode.
- Updates automatically every second.
- Simple graphical user interface using Tkinter.
- Black background with white text.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/sinan07khan/YOUR-REPOSITORY.git
```

**2. Open the project folder**

```bash
cd YOUR-REPOSITORY
```

**3. Run the Python script**

```bash
python main.py
```

Replace `main.py` with your actual Python filename if it is different.

## How to Use

1. Run the program.
2. The digital clock will display the current time.
3. Press the **H** key to switch between 12-hour and 24-hour formats.
4. Press **H** again to switch back.

## Customization

You can customize the clock by changing these values in the code:

| Setting | Purpose |
|---|---|
| `window.title()` | Window title |
| `font=("Comic Sans MS", 40)` | Font style and size |
| `fg="white"` | Text color |
| `bg="black"` | Background color |
| `use_24_hour_format = False` | Default time format |
| `after(1000, update_clock)` | Update interval in milliseconds |

## How It Works

1. Tkinter creates the graphical window and clock label.
2. Python's `time` module retrieves the current system time.
3. The `strftime()` function formats the hours, minutes, seconds, and AM/PM.
4. The `after()` method updates the clock every 1,000 milliseconds.
5. A keyboard event switches between 12-hour and 24-hour formats.

## Technologies Used

- **Python** — Programming language
- **Tkinter** — Graphical user interface
- **Time Module** — Current time and formatting

## Author

**Sinan Khan**

GitHub: [@sinan07khan](https://github.com/sinan07khan)

---

If you find this project useful, consider giving the repository a star!

