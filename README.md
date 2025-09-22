# CodeVeda Python Development

A collection of **9 Python projects/tasks** completed during my internship at **Codveda Technology**.  
They are organized into three levels — **Basic, Intermediate, Advanced** — demonstrating step-by-step growth in Python programming.

---

## 📑 Table of Contents
1. [Overview](#overview)  
2. [Projects / Task List](#projects--task-list)  
3. [Technologies & Tools](#technologies--tools)  
4. [Setup & Usage](#setup--usage)  
5. [Structure & Organization](#structure--organization)  
6. [Future Improvements](#future-improvements)  
7. [Author](#author)  
8. [License](#license)  

---

## 📌 Overview
This repository reflects my journey in **Python development** during my internship.  
Each project explores a different area of Python — from fundamentals and CLI tools to **web scraping, APIs, Django web apps, encryption, and algorithms**.

**Learning goals:**
- Strengthen Python fundamentals  
- Practice error handling, file I/O, and modular design  
- Work with external libraries and APIs  
- Develop algorithmic problem-solving skills  
- Build a functional Django authentication app  

---

## 🗂 Projects / Task List

| Level | Project | Description |
|-------|---------|-------------|
| **Basic** |Calculator | CLI calculator supporting basic arithmetic operations |
| | Guessing Game | Random number guessing game with user feedback |
| | Word Counter | Counts words from input or text file |
| **Intermediate** |To-Do App | Task manager (CLI/GUI) with persistent storage |
| | Web Scraper | Scrapes data from websites using requests/BeautifulSoup |
| | API Integration | Fetches and processes data from external APIs |
| **Advanced** | Django Authentication App | Web app with user sign-up/login and session handling |
| | File Encryption Tool | Encrypts and decrypts files using Python libraries |
| | N-Queens Solver | Backtracking algorithm to solve the N-Queens puzzle |

---

## 🛠 Technologies & Tools
- **Python 3.x**  
- Standard library modules (`os`, `sys`, `json`, `random`, etc.)  
- **Requests**, **BeautifulSoup** (web scraping)  
- **Django Framework** (web app development)  
- **Cryptography libraries** (for file encryption)  
- Git & GitHub for version control  

---

## ⚙️ Setup & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/shubhamsharma2961/CodeVeda_Python_Development.git
   cd CodeVeda_Python_Development
   
2. **(Optional) Create a virtual environment**
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3. **Run individual projects**
Navigate to the desired folder and run the script. Example:

cd Level1-Basic\Calculator
python calculator.py

For the Django app:
cd Level3-Advanced\Django-app\taskmanager
python manage.py migrate
python manage.py runserver

4.📂 **Structure & Organization**
CodeVeda_Python_Development/
│── Level1-Basic/
│   ├── Calculator/
│   ├── GuessingGame/
│   └── WordCounter/
│
│── Level2-Intermediate/
│   ├── ToDoApp/
│   ├── WebScraper/
│   └── APIIntegration/
│
│── Level3-Advanced/
│   ├── DjangoAuthenticationApp/
│   ├── FileEncryption/
│   └── NQueens/

5.🚀 **Future Improvements**
1.Add unit tests for each project.
2.Improve error handling and input validation
3.Enhance documentation and in-code comments
4.Implement CI/CD workflows (GitHub Actions for testing/formatting)
5.Expand Django project with UI features

6.👨‍💻 **Author**
Shubham Sharma
Python & Django Developer | Intern at Codveda Technology
GitHub: https://github.com/shubhamsharma2961
LinkedIn: https://www.linkedin.com/in/shubham-sharma-839961255/

7.📜 **License**
This project is licensed under the MIT License — see the LICENSE file for details.
