# 🐍 OOP Theory - Python Object-Oriented Programming

A comprehensive repository documenting my journey through **Object-Oriented Programming (OOP)** concepts in Python. This repo contains class assignments, exam solutions, self-study materials, and practice problems from my university coursework.

---

## 📁 Repository Structure

```
OOP-Theory/
├── 📄 Root Files (Practice & Examples)
├── 📂 Exams/           # Class tests, midterms, and finals
├── 📂 Problem Set/     # Lab tasks and assignments
├── 📂 Self_study/      # Self-learning resources
└── 📂 Online class/    # Class materials (Pandas)
```

---

## 🎯 Core OOP Concepts Covered

### ✅ Classes & Objects
- Class creation and instantiation
- Instance attributes and methods
- `__init__` constructor method
- `__str__` and `__repr__` magic methods

### ✅ Encapsulation
- Private attributes using name mangling (`__attribute`)
- Getter and setter methods
- Data hiding and protection

### ✅ Inheritance
- Single inheritance
- Method overriding
- `super()` function usage
- Parent-child class relationships

### ✅ Polymorphism
- Method overriding
- Duck typing in Python

### ✅ Abstraction
- Abstract Base Classes (ABC)
- Abstract methods using `@abstractmethod`

---

## 📂 Directory Details

### 🏠 Root Files
| File | Description |
|------|-------------|
| `circular_list.py` | Circular Linked List implementation with Node class |
| `student_management.py` | Student Academic Record Management System |
| `item_class_question.py` | Item class with class variables and methods |
| `hi.py` | Course & Student enrollment system |
| `he.py` | Point3D class with copy and scale methods |

### 📝 Exams/
Contains exam solutions organized by exam type:

- **BB_CT/** - Class Tests (DateVal, TimeVal classes)
- **BC_CT/** - Class Tests (Room, House composition examples)
- **MID/** - Midterm exam solutions (Account class)
- **Final/** - Final exam notebook with comprehensive OOP problems

### 💻 Problem Set/
Lab assignments and practice problems:

- `Swakhar_sir_assing.py` - SavingsAccount & CurrentAccount (Inheritance demo)
- `Tawsif_task_*.py` - Various lab tasks (Element frequency, Running total, Anagrams)
- **Nafiz Problem set/** - Additional practice problems

### 📚 Self_study/
Self-learning materials covering advanced Python concepts:

| Folder | Topics Covered |
|--------|---------------|
| `Class_object/` | Dog, Restaurant, User classes from textbook exercises |
| `Decorator/` | Function & class decorators, `@wraps`, logging, timing |
| `Generator/` | Generator functions, `yield` keyword, lazy evaluation |
| `matplotlib/` | Data visualization dashboards |
| `Tkinter/` | GUI applications (Miles to KM converter, Digital Tasbih) |
| `exception.py` | Exception handling (try/except/else/raise) |

### 📊 Online class/
- **Pandas class/** - Data manipulation with Pandas library

---

## 🔥 Key Implementations

### 1. Student Management System
```python
# Features: Auto-generated IDs, Course enrollment, CGPA calculation
class Student:
    def add_course(self, course): ...
    def get_cgpa(self): ...
```

### 2. Banking System (Inheritance Example)
```python
class SavingsAccount:      # 5% profit, withdrawal limits
class CurrentAccount:      # 3% profit, no withdrawal limits
```

### 3. Circular Linked List
```python
class CircularLinkedList:
    def append(self, data): ...
    def prepend(self, data): ...
    def remove(self, key): ...
```

### 4. Decorators
```python
@my_logger    # Logs function calls
@my_timer     # Times function execution
def some_function(): ...
```

---

## 🛠️ Technologies Used

- **Language:** Python 3.x
- **Libraries:** 
  - `functools` (wraps decorator)
  - `copy` (deep/shallow copy)
  - `abc` (Abstract Base Classes)
  - `tkinter` (GUI)
  - `matplotlib` (Visualization)
  - `pandas` (Data Analysis)
  - `logging` (Logger decorator)

---

## 📖 Learning Resources Referenced

- Python Crash Course (Book exercises)
- Real Python tutorials
- YouTube OOP tutorials
- University lecture materials

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/OOP-Theory.git

# Navigate to directory
cd OOP-Theory

# Run any Python file
python student_management.py
python Self_study/Decorator/decorator.py
```

---

## 📌 Topics for Future Study

- [ ] Multiple Inheritance & MRO
- [ ] Metaclasses
- [ ] Design Patterns (Singleton, Factory, Observer)
- [ ] Dataclasses & Named Tuples
- [ ] Type Hints and Static Typing

---

## 👨‍💻 Author

**Musfique Ahmed**  
Student ID: 0152330101  
Department: Data Science, United International University

---

## 📜 License

This repository is for educational purposes. Feel free to use the code for learning!

---

> *"Programs must be written for people to read, and only incidentally for machines to execute."*  
> — Harold Abelson
