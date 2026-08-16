# CodeOrbit Python Programming Internship

This repository contains the projects completed as part of the **Python Programming Internship at CodeOrbit Technologies**.

The projects demonstrate practical implementation of Python programming concepts through simple command-line applications.

---

## Internship Information

**Organization:** CodeOrbit Technologies  
**Program:** Python Programming Internship  
**Duration:** 1 Month  
**Domain:** Python Programming

---

## Projects Completed

### 1. Simple Calculator

A command-line calculator developed using Python to perform basic arithmetic operations.

#### Features

- Addition
- Subtraction
- Multiplication
- Division
- Division-by-zero handling
- Invalid input handling
- Clear display of calculation results
- User input through the command line

#### Python Concepts Used

- Variables
- User input
- Conditional statements
- Functions
- Arithmetic operators
- `try-except` exception handling

**File:** `Simple_Calculator/calculator.py`

---

### 2. Number Guessing Game

A command-line game in which the computer generates a random number between 1 and 100 and the user attempts to guess it.

The program provides hints after each guess to help the user identify the correct number.

#### Features

- Random number generation
- Number range from 1 to 100
- User input for guesses
- "Too High" hint
- "Too Low" hint
- Attempt counter
- Correct guess notification
- Invalid input handling
- Option to play multiple rounds

#### Python Concepts Used

- Variables
- User input
- Conditional statements
- Loops
- Functions
- Random number generation
- Exception handling

**File:** `Number_Guessing_Game/guess_game.py`

---

### 3. To-Do List CLI App

A command-line application for managing tasks using a Python list.

The application allows users to add, view, and remove tasks through a menu-driven interface.

#### Features

- Add new tasks
- View all tasks
- Display numbered tasks
- Remove tasks
- Invalid task number handling
- Empty task validation
- Menu-driven interface
- Exit option

#### Python Concepts Used

- Lists
- Variables
- User input
- Conditional statements
- Loops
- Functions
- `append()`
- `pop()`
- `enumerate()`
- Exception handling

**File:** `To_Do_List/todo.py`

---

## Technologies Used

- Python 3
- Command-Line Interface (CLI)
- Python Standard Library
- Visual Studio Code
- GitHub

---

## Python Concepts Demonstrated

The projects demonstrate practical use of the following Python concepts:

- Variables and data types
- User input and output
- Arithmetic operators
- Conditional statements
- `if`, `elif`, and `else`
- `for` and `while` loops
- Functions
- Lists
- List methods
- `enumerate()`
- Exception handling
- `try-except`
- Random number generation
- Command-line application development

---

## Repository Structure

```text
CodeOrbit_PythonProgramming/
│
├── Simple_Calculator/
│   └── calculator.py
│
├── Number_Guessing_Game/
│   └── guess_game.py
│
├── To_Do_List/
│   └── todo.py
│
└── README.md

Setup Instructions
Step 1: Download or Clone the Repository

Clone the repository using Git:

git clone https://github.com/Rakeshthudum/CodeOrbit_PythonProgramming.git

Then navigate to the project directory:

cd CodeOrbit_PythonProgramming

You can also download the repository as a ZIP file from GitHub and extract it on your computer.

How to Run the Projects
Simple Calculator

Navigate to the calculator folder:

cd Simple_Calculator

Run the program:

python calculator.py

The program accepts user input and performs the selected arithmetic operation.

Number Guessing Game

Navigate to the Number Guessing Game folder:

cd Number_Guessing_Game

Run the program:

python guess_game.py

The program generates a random number between 1 and 100 and asks the user to guess it.

The program provides "Too High" or "Too Low" hints until the correct number is guessed.

The number of attempts is also displayed.

To-Do List CLI App

Navigate to the To-Do List folder:

cd To_Do_List

Run the program:

python todo.py

The program displays the following menu:

===== TO-DO LIST =====


1. Add Task
2. View Tasks
3. Remove Task
4. Exit

Users can select an option and manage their tasks through the command line.

To-Do List Features
Add Task

Users can select option 1 to add a new task.

Example:

Enter your choice (1-4): 1
Enter a new task: Complete internship task
Task added successfully!
View Tasks

Users can select option 2 to view all currently stored tasks.

Example:

===== YOUR TASKS =====
1. Complete internship task
Remove Task

Users can select option 3 to remove a task by entering its task number.

Example:

Enter the task number to remove: 1
Task 'Complete internship task' removed successfully!

The application also validates invalid task numbers.

Exit

Users can select option 4 to exit the application.

Sample Number Guessing Game

Example execution:

===== NUMBER GUESSING GAME =====


I have selected a number between 1 and 100.
Try to guess it!


Enter your guess: 14
Too Low! Try again.


Enter your guess: 45
Too Low! Try again.


Enter your guess: 99
Too High! Try again.


Enter your guess: 75
Congratulations! You guessed the number in 5 attempts.


Do you want to play again? (yes/no): no


Thank you for playing!
Sample Calculator

The Simple Calculator accepts user input and performs basic arithmetic operations including:

Addition
Subtraction
Multiplication
Division

The program also handles invalid inputs such as division by zero.

Error Handling

The projects include input validation and exception handling to improve program reliability.

Examples include:

Invalid numerical input
Division by zero
Invalid menu choices
Invalid task numbers
Empty task input
Learning Outcomes

Through these projects, I gained practical experience in:

Writing Python programs from scratch
Developing command-line applications
Working with user input
Implementing conditional logic
Using loops for repeated operations
Creating and using functions
Managing data using Python lists
Handling invalid user input
Implementing exception handling
Using Python's random number functionality
Organizing Python projects into separate folders
Testing applications using different input scenarios
Using GitHub to maintain and showcase project source code
Internship Task Completion

The 1-month Python Programming Internship includes the following tasks:

Simple Calculator
To-Do List CLI App
Number Guessing Game

The internship requires completion of a minimum of 2 out of 3 tasks for certificate eligibility.

Completed Tasks
 Simple Calculator
 To-Do List CLI App
 Number Guessing Game

Total Completed: 3/3 Tasks

GitHub Repository

Repository Name: CodeOrbit_PythonProgramming

Repository Link:

https://github.com/Rakeshthudum/CodeOrbit_PythonProgramming

Project Demonstration

A project demonstration video can be shared on LinkedIn as part of the internship submission requirements.

The demonstration can include:

Project introduction
Source code overview
Program execution
Key features
Sample output
GitHub repository
Internship Submission

The completed source code for all three projects is maintained in this GitHub repository.

The required internship submission is completed through the submission form provided by CodeOrbit Technologies.

Author

Rakeshthudum

Python Programming Intern
CodeOrbit Technologies

Acknowledgement

I would like to thank CodeOrbit Technologies for providing this internship opportunity and for providing practical Python programming tasks that helped strengthen my programming and problem-solving skills.

License

This project was developed for educational and internship purposes.



**Important:** Copy from `# CodeOrbit Python Programming Internship` all the way down to `This project was developed for educational and internship purposes.` — **don't copy the ```markdown lines themselves**.


This version also avoids claiming that your To-Do List saves tasks to a file, because your actual implementation stores them in a list during runtime; file saving was optional in the task specification. :contentReference[oaicite:1]{index=1}
