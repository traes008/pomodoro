# Pomodoro Study Timer

A simple, modern Pomodoro study timer built with Python and Tkinter.

---

## 🚀 How to Get Started

### Option 1: Download the Pre-built Windows Release

- **Go to the `release` directory** in this repository (or the [Releases page](https://github.com/traes008/pomodoro/releases) on GitHub).
- **Download the latest `pomodoro-windows.zip` file.**
- **Extract the zip file** to a folder of your choice.
- **Run `pomodoro.exe`** to start the app.

> **Note:** Currently, only a Windows release is provided. If you are on Linux or macOS, please build from source (see below).

---

### Option 2: Build from Source

#### Requirements

- Python 3.12 or higher
- pip (Python package installer)
- Tkinter (usually included with Python)

All required Python packages are listed in `requirements.txt`.

#### Steps

1. **Clone the repository:**
   ```sh
   git clone https://github.com/traes008/pomodoro.git
   cd pomodoro
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the app from source:**
   ```sh
   python -m pomodoro
   ```

4. **(Optional) Build a standalone executable:**

   - **Windows:**
     ```sh
     cd scripts
     ./build.bat
     ```
   - **Linux/macOS:**
     ```sh
     cd scripts
     ./build.sh
     ```

   The executable will be created in the `dist/` directory.

5. **(Optional) Create a release zip:**
   - **Windows:** `./release.bat`
   - **Linux/macOS:** `./release.sh`
   - The zip file will be in the `release/` directory.

---

## Need Help?

If you have any issues building or running the app, please open an issue on GitHub!

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
