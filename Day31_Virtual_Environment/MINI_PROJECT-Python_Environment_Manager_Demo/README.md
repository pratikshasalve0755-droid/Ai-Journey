# 🐍 Python Environment Manager Demo

## 📌 Project Description

This project demonstrates how to organize a professional Python project using a Virtual Environment.

It shows how to:

- Create and activate a virtual environment
- Install external packages
- Display Python version
- Display the current working directory
- Use the Colorama package for colored output
- Generate a requirements.txt file
- Use a .gitignore file

---

## 📂 Project Structure

```
Python_Environment_Manager_Demo/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

## 📦 Requirements

- Python 3.x
- requests
- colorama

---

## 🔹 What is a Virtual Environment?

A Virtual Environment is an isolated Python environment created for a specific project.

It keeps project dependencies separate from the global Python installation, allowing different projects to use different package versions without conflicts.

---

## ▶️ How to Create a Virtual Environment

```
py -m venv venv
```

---

## ▶️ How to Activate the Virtual Environment

### Windows

```
venv\Scripts\activate
```

After activation, your terminal should display:

```
(venv)
```

---

## 📥 How to Install Required Packages

```
pip install requests
pip install colorama
```

---

## ▶️ How to Run the Project

```
python main.py
```

---

## 📄 Generate requirements.txt

```
pip freeze > requirements.txt
```

This creates a file containing all installed packages and their versions.

---

## 🔄 Recreate the Environment

After downloading this project from GitHub:

### Step 1

Create a virtual environment

```
py -m venv venv
```

### Step 2

Activate it

```
venv\Scripts\activate
```

### Step 3

Install all required packages

```
pip install -r requirements.txt
```

---

## 🚫 .gitignore

The following files and folders are ignored:

```
venv/
__pycache__/
*.pyc
```

These files are automatically generated and should not be uploaded to GitHub.

---

## 📚 Concepts Learned

- Virtual Environment
- Package Installation
- pip
- requirements.txt
- .gitignore
- os module
- sys module
- colorama package

---

## 👩‍💻 Author

Pratiksha Salve

AI & Data Science Student

Learning Python | Git | GitHub | Artificial Intelligence