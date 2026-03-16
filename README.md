# Turing Machine Sorting Simulation

## 📌 Overview

This project simulates a **sorting algorithm using a Turing Machine model**.
The system demonstrates how a theoretical **Turing Machine can perform sorting operations** by simulating tape movements, state transitions, and swap operations.

The project provides a **web-based interface** where users can input numbers and observe the **step-by-step execution of the sorting process**.

The goal of this project is to help students understand **Automata Theory and Turing Machine operations** through visualization and simulation.

---

# 🎯 Objectives

* Simulate a **sorting algorithm using a Turing Machine**
* Display the **step-by-step execution of sorting**
* Implement a **transition function table**
* Provide a **user-friendly interface** for input and visualization
* Demonstrate how **state transitions mimic sorting operations**

---

# 🛠 Technology Stack

## Frontend Technologies

The frontend is responsible for **user interaction and visualization**.

* **HTML5** – Structure of the web interface
* **CSS3** – Styling and layout design
* **JavaScript** – Handles user input and sends data to backend using AJAX

---

## Backend Technologies

The backend performs the **sorting simulation and state transitions**.

* **Python** – Core logic implementation
* **Flask** – Web framework for handling requests and responses
* **Turing Machine Algorithm** – Custom simulation based on Bubble Sort logic

---

# ⚙️ Working of the Turing Machine Sorting Simulation

## Input Representation

The user enters numbers separated by the `#` symbol.

Example input:

```text
5#3#8#2
```

The backend converts this input into a **Turing Machine tape representation**.

Each number is treated as a symbol on the tape.

---

## Sorting Logic

The sorting mechanism is based on **Bubble Sort**, adapted for a Turing Machine simulation.

The algorithm performs:

* Tape scanning
* Symbol comparison
* Swap operations
* State transitions

Each swap between elements is recorded as a **state transition of the machine**.

---

## Step-by-Step Execution

1. The machine reads **two adjacent numbers** on the tape.
2. If the **first number is greater than the second**, they are swapped.
3. The machine moves to the **next pair of numbers**.
4. This process repeats until the sequence is sorted.
5. The **final sorted sequence** is displayed to the user.

---

# 🔄 Transition Function Table

The transition function represents how the Turing Machine changes states during execution.

Example format:

| Current State | Symbol Read | Action   | Next State |
| ------------- | ----------- | -------- | ---------- |
| q0            | number      | compare  | q1         |
| q1            | greater     | swap     | q2         |
| q2            | move right  | continue | q0         |
| qf            | sorted      | halt     | end        |

This table helps visualize **how the machine processes and sorts the numbers step by step**.

---

# 📂 Project Structure

```
turing-machine-sorting/
│
├── app.py              # Flask backend
├── sorting_logic.py    # Turing machine sorting implementation
│
├── templates/
│   └── index.html      # Web interface
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# 🚀 How to Run the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/AnshuKumar25/turing-machine-sorting.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install flask
```

---

## 3️⃣ Run the Flask Server

```bash
python app.py
```

---

## 4️⃣ Open the Application

Open your browser and go to:

```
http://localhost:5000
```

Enter numbers like:

```
7#2#5#1
```

The system will show the **step-by-step sorting simulation**.

---

# 📊 Example

### Input

```
5#3#8#2
```

### Sorting Steps

```
5 3 8 2
3 5 8 2
3 5 2 8
3 2 5 8
2 3 5 8
```

### Output

```
2 3 5 5
```

---

# 📚 Concepts Demonstrated

* Turing Machine Model
* State Transitions
* Tape Representation
* Automata Theory
* Sorting Algorithms
* Web-based Simulation

---

# 🚀 Future Improvements

* Visual **tape animation**
* Graphical **state diagram**
* Support for **more sorting algorithms**
* Real-time **state transition visualization**

---

# 👨‍💻 Author

**Anshu Kumar**

Computer Engineering Student

---

# 📜 License

This project is developed for **educational purposes related to Automata Theory and Turing Machines**.
