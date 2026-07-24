# 📂 File Organizer in Python

## 📖 Description

File Organizer is a Python project that automatically organizes files into different folders based on their file extensions.

The program scans a folder selected by the user, identifies the type of each file, creates folders if they do not already exist, and moves files into their respective categories.

---

## ✨ Features

- Organizes files automatically.
- Creates folders if they do not exist.
- Supports multiple file types.
- Uses a dictionary for file type identification.
- Uses functions to avoid repeated code.
- Displays a summary of moved files.

---

## 📁 Supported Categories

| Category | Extensions |
|----------|------------|
| Images | .jpg, .jpeg, .png |
| Documents | .pdf, .docx, .txt, .pptx |
| Videos | .mp4, .mkv, .avi, .mov |
| Audio | .mp3, .wav, .aac, .flac |
| Archives | .zip, .rar |
| Python | .py |
| Java | .java |
| Others | Any unsupported file |

---

## 🛠 Technologies Used

- Python 3
- os module
- shutil module

---

## ▶️ How to Run

1. Clone the repository

```
git clone https://github.com/jgurupreethi19/file-organizer-python.git
```

2. Open the project folder.

3. Run the program

```
python fileorganizer.py
```

4. Enter the folder path to organize.

Example:

```
C:\Users\Hima\Desktop
```

---

## 📌 Project Workflow

1. User enters a folder path.
2. Program checks whether the folder exists.
3. Reads all files in the folder.
4. Identifies each file using its extension.
5. Creates a destination folder if needed.
6. Moves the file into the correct folder.
7. Displays a summary.

---

## 📚 Concepts Used

- Functions
- Dictionary
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- os Module
- shutil Module

---

## 👩‍💻 Author

**J GURUPREETHI**

GitHub:
https://github.com/jgurupreethi19
