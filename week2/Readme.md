-- Student Register --

A console app for managing a class list. This, to be able to Add students, list them, search by name or age, and compute the average age — all from a simple menu.

-- FEATURES --

Add student (name, age)

List all students

Search a student by exact name

Search students in a specific age or intervall

Calculate and print average age

Colored output via colorama

In-memory storage (no files/DB)

-- REQUIREMENTS --

Python 3.9+

colorama

pip install colorama

Run python app.py

-- USAGE --

On start you’ll see a menu looks like this:

MAIN MENU

1- Add student
2- List all students
3- Search student
4- Search students with a specific age or in an age intervall
5- Calculate average student-age
6- Exit program

Enter a number (1–6) to perform an action. Prompts will guide you (For example by asking name, age, etc). Output uses color for clarity.

-- NOTES --

Data is stored only in memory; restarting the app resets the register.

Input validation prints helpful error messages on invalid types and an error handling will be handled

Example Choose a number from 1-6 in the menu: 

1 Enter name: Bob

2 Enter age: 20

3 Find a student : "Carl Johan"

4 Average student-age: 18.7

5 Students in age between 18 and 21: 13

6 Exit the program
