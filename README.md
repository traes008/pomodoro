# Pomodoro Study Timer

A study timer application built with Python and Tkinter. Track your study sessions and manage breaks effectively.

![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Features

- Study timer with break management
- Session statistics tracking
- Simple and clean interface
- Color-coded status indicators

## Installation

1. Clone the repository:
```bash
git clone https://github.com/traes008/pomodoro.git
cd pomodoro
```

2. Create a virtual environment:
```bash
# On Windows
python -m venv pomodoro_venv
pomodoro_venv\Scripts\activate

# On Linux/macOS
python3 -m venv pomodoro_venv
source pomodoro_venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start a study session by clicking "Start Timer"
2. Take breaks using the "Take Break" button
3. End your session with the "Stop" button to view a summary of:
   - Total study time
   - Total break time
   - Average study session length

## Running the Application

```bash
python main.py
```

## 🎯 How to Use

1. **Start a Study Session**
   - Click the "Start Timer" button to begin tracking your study time
   - The timer will display your current study duration

2. **Managing Breaks**
   - Click "Take Break" when you need a pause
   - The break timer will start automatically
   - Click "End Break" to resume studying

3. **Ending a Session**
   - Click "Stop" to end your study session
   - A summary window will show your:
     - Total study time
     - Total break time
     - Average study session length

4. **Viewing History**
   - Click the "History" button to view past sessions
   - See daily summaries and detailed session breakdowns
   - Track your study patterns over time

## 📊 Features in Detail

### Study Timer
- Real-time study duration tracking
- Color-coded status indicators
- Clear session progress visibility

### Break Management
- Flexible break system
- Break time tracking
- Easy session resumption

### Session Statistics
- Comprehensive session summaries
- Break time analysis
- Study pattern insights

## 🛠️ Building from Source

To create a standalone executable:

### Windows
```bash
.\build.bat
```

### Linux/macOS
```bash
./build.sh
```

The executable will be created in the `dist` directory.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
*Note: This project was developed with assistance from generative AI tools to ensure best practices and clean code structure.*
