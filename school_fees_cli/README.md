# School Fees CLI

A simple command-line application to manage student fee payments, with data stored in JSON.

## Features

- Register new students with name, ID, and required fees
- Record payments for students
- View all students and their payment status

## Requirements

- Python 3.x

## Usage

1. Open a terminal and navigate to the project directory:
    ```bash
    cd ~/Development/phase3/phase-3-project/school_fees_cli
    ```
2. Run the CLI:
    ```bash
    python3 main.py
    ```
3. Follow the menu prompts to add students, view students, or record payments.

## Data Storage

All student data is saved in `school_fees_cli/data/students.json`.

## Project Structure
```
school_fees_cli/
└── data/
    └── students.json
├── fees.py
├── main.py
├── storage.py
├── student.py
```

## Example

```
Menu:
1. Add Student
2. View Students
3. Record Payment
4. Exit
Enter your choice: 1
Enter student name: John Doe
Enter student ID: S001
Enter required fees: 5000
Student John Doe added successfully.
```