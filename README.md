# Automated Testing Demo

This is a simple Python-based demonstration project designed to showase basic *automated testing* practices. It includes foundational scripts and tests to practice function validation, input handling, & test structuring. 

---

## Project Structure
 - 'app.py': Main application code, additional logic or utility functions.
 - 'test_app.py': Tests for 'app.py'. 
 - 'calculator.py': Arithmetic functions (add, subtract, multiply, divide. 
 - 'test_calculator.py': Unit tests for the 'calculator.py' scrip.
 - 'README.md': Project Documentation

---

## What You'll Learn
- How to write Python functions that are easy to test
- How to use 'unittest' for automation testing.
- How to check edge cases like dividing by zero
- How to create clear and maintainable testing logic. 

---

## Getting Started

### 1. Clone the Respository

```bash
git clone https://github.com/HCBrooks-lab/Automated-Testing-Demo.git
cd Automated-Testing-Demo
```
### 2. Create a Virtual Environment - Optionally

python3 -m venv venv
source venv/vin/activate *Mac/Linux*
venv\Scripts\activate  *Windows*

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Application

python app.py

### 5. Run the Tests

- python -m unittest test_app.py *tests the original application code.*
- python3 test_calculator.py *tests the added calulator module.*

---

## Features

- Basic Python app for demonstration
- Unit testing with unittest
- Example of clean repo structure
- .gitignore excluding virtual environments & cache.

### Test Report

This project includes automated unit tests written using pytest. The tests validate basic arithmetic functionality using assert statements. An HTML test report is also generated using the pytest-html plugin, providing a summarty of all test cases executed. 

**Preview of Test Report**
To generate this report, run:

pytest --html=report.html --self-contained-html

---

## Project Status

This repository is part of a growing hands-on automation testing demo. It is actively being expanded with new scrips, test cases, and documentation to demonstrate foundational & intermediate Python testing skills. 

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 
