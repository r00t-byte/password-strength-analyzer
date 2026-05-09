# Password Strength Analyzer 

A professional Python-based cybersecurity tool that analyzes password strength, detects reused passwords, and suggests stronger alternatives.

---

# Features

- Password strength analysis using `zxcvbn`
- Smart password suggestions
- Password reuse detection
- SHA-256 password hashing
- Colored warning messages
- Command-line help menu
- Modular project structure
- CTRL + C exit support

---



---

# Installation

## Clone Repository

```bash
git clone https://github.com/r00t-byte/password-strength-analyzer.git 
```

## Move Into Project Directory

```bash
cd password-strength-analyzer
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---
---

# Usage

## Run Tool

```bash
python main.py
```

## Show Version

```bash
python main.py -v
```

## Show Help Menu

```bash
python main.py -h
```

---

# Example Output

```text
==========================================
   PASSWORD STRENGTH ANALYZER 
==========================================

Type 'exit' or press CTRL + C to quit

Enter Password : admin123

==========================================
              ANALYSIS RESULT
==========================================

Strength : Weak
Score    : 1/4

Password already used before!

Suggestions :
- Add at least 1 uppercase letter
- Add at least 1 special character
- Use 12+ characters for stronger security

==========================================
      SMART PASSWORD SUGGESTION
==========================================

Admin123@582741#
```

---

# Technologies Used

- Python
- zxcvbn
- SHA-256 Hashing
- Regex
- File Handling

---

# Security Features

- Detects weak passwords
- Detects reused passwords
- Stores only hashed passwords
- Suggests stronger passwords automatically

---
