"""
PART A: Theory (18 Questions)
Section 1: Installation & Environment (5 Qs)

1.Explain one key difference in Python installation on Windows, Mac, and Linux.
A.Windows → Python is not preinstalled. You must download it from python.org or use the Microsoft Store.
           During installation, you also need to check "Add Python to PATH" manually.
  Mac → macOS comes with an older version of Python 2.x preinstalled (mainly for system tools).
           You usually install a newer Python 3.x version via Homebrew or python.org.
  Linux → Most Linux distros already have Python 3 preinstalled and integrated into the system.
           You can install/update it easily via your package manager (apt, dnf, etc.)

2.What is the purpose of a virtual environment (venv)?
A.virtual environment (venv) is a self-contained directory that contains a Python installation for a particular version of Python,
  plus several additional packages. It allows you to create isolated environments for different projects,
  ensuring that dependencies and packages do not interfere with each other. This is particularly useful when working on multiple projects that may require different versions of libraries or Python itself.    

3.Compare venv vs conda in two points.
A. venv is a built-in module in Python that allows you to create lightweight virtual environments,
   while conda is a package manager that can create isolated environments and manage packages across different languages (Python, R, etc.).

4.Write the command to create and activate a venv on:
    -Windows
    -Linux/Mac  
A.
   - Windows:
        python -m venv myenv
        myenv\Scripts\activate
    - Linux/Mac:
        python3 -m venv myenv
        source myenv/bin/activate 

5.Why is isolating dependencies important when working on multiple projects?
A.Isolating dependencies is important because it prevents conflicts between different projects that may require different versions of the same library or package.
  This ensures that each project runs with its specific dependencies without affecting others, leading to more stable and predictable development environments.
   
Section 2: IDE, Jupyter & CLI Basics (5 Qs)

1.List two advantages of using Jupyter Notebook over a standard IDE.  
A. Jupyter Notebook allows for interactive data visualization and exploration, enabling users to run code in cells and see immediate results.
   It also supports rich media outputs (like images, videos, and LaTeX) directly within the notebook, making it ideal for data analysis and reporting.   
   
2.What is the main difference between VS Code and Jupyter Notebook for Python development?
A.VS Code is a full-fledged code editor with extensive features for software development, including debugging, version control, and extensions.
   Jupyter Notebook is primarily designed for data analysis and exploration, allowing users to write and execute code in a cell-based format with rich media outputs.

3.Write two CLI commands to:Check Python version and Install a package using pip
A. To check the Python version:
   python --version or python3 --version
   To install a package using pip:
    pip install package_name or pip3 install package_name

4.Explain the use of pip freeze > requirements.txt.
A.The command `pip freeze > requirements.txt` generates a list of all installed Python packages in the current environment along with their versions,
  and saves this list to a file named `requirements.txt`. This file can be used to recreate the environment later by running `pip install -r requirements.txt`.

5.What are shell shortcuts? Give two examples.
A.Shell shortcuts are command-line shortcuts that allow users to perform common tasks more efficiently. Examples include:
   - `cd ..` to move up one directory level.
   - `ls -l` to list files in the current directory with detailed information (on Unix-like systems).

Section 3: Debugging & Workflow (4 Qs)
1.Name two common debugging techniques in Python.
A. Two common debugging techniques in Python are:
   - Using print statements to output variable values and program flow at different points in the code.
   - Utilizing a debugger tool (like pdb or the built-in debugger in IDEs) to step through the code line by line, inspect variables, and set breakpoints.

2.What are dot-files? Give two examples and their purpose.
A.Dot-files are configuration files in Unix-like operating systems that start with a dot (.) and are typically hidden by default.
  They store user-specific settings for applications or the system. Examples include:
   - `.bashrc`: Contains user-specific configurations for the Bash shell, such as aliases and environment variables.
   - `.gitconfig`: Stores user-specific Git configurations, such as username, email, and preferred editor.

3.Explain the difference between hard coding and using variables.
A.Hard coding refers to embedding fixed values directly into the code, making it inflexible and difficult to change.
  Using variables allows for dynamic values that can be easily modified without changing the code structure, enhancing maintainability and readability.

4.Why are keyboard shortcuts important for a developer’s productivity? Give two examples.
A.Keyboard shortcuts are important for a developer's productivity because they allow for faster navigation and execution of commands without relying on a mouse,
  reducing the time spent on repetitive tasks. Examples include:
   - `Ctrl + C` to copy selected text or code.
   - `Ctrl + V` to paste copied text or code.

Section 4: Coding Workflow & Best Practices

1.What is the purpose of refactoring code? Give an example scenario.
A.Refactoring code is the process of restructuring existing code without changing its external behavior to improve readability, maintainability, and performance.
  For example, if a function is too long and complex, it can be refactored into smaller, more manageable functions that each handle a specific task, making the code easier to understand and modify in the future.

2.Mention two VS Code shortcuts that improve coding efficiency.
A. Two VS Code shortcuts that improve coding efficiency are:
   - `Ctrl + P`: Quickly open files by typing their names.
   - `Ctrl + Shift + F`: Search for text across all files in the project, allowing for quick navigation to specific code sections.

3.Why should developers maintain code snippets or templates?
A.Developers should maintain code snippets or templates to save time on repetitive tasks, ensure consistency across projects, and promote best practices.
  Snippets can be reused in different projects, reducing the need to write common code from scratch and allowing developers to focus on more complex tasks.

4.Name one commonly used dot-file for Python environment setup and its function.
A.One commonly used dot-file for Python environment setup is `.pythonrc.py`. Its function is to execute Python code automatically when the interactive Python shell starts, allowing users to set up custom configurations, import frequently used modules, or define functions that enhance their interactive Python experience.

"""
# PART B: Coding Questions (22 Questions)
# Section 5: Easy Level (10 Qs)

# 1.Print “Hello, Python World!”.
print("Hello, Python World!")

# 2.Store your name, age, and city in variables and print them in a single line.
name = "pavan ralla"
age = 25
city = "Bengaluru"
print(f"My name is {name}, I am {age} years old, and I live in {city}.")

# 3.Write a program to take user input for name and greet them.
name = input("Enter your name: ")
print(f"Hello, {name}! Welcome to Python programming.")

# 4.Convert temperature from Celsius to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")

# 5.Write a program to swap two numbers without using a third variable.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a, b = b, a
print(f"After swapping: a = {a}, b = {b}")

# 6.Calculate the area of a rectangle given its length and width.
length = float(input("Enter length of the rectangle: "))
width = float(input("Enter width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is {area} square units.")

# 7. Take three numbers as input and print the largest.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number is {largest}.")

# 8. Write a program to calculate the sum of all elements in a list.
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = sum(numbers)
print(f"The sum of the list elements is {sum_of_numbers}.")

# 9. Write a script that checks Python version using sys module.
import sys
print(f"Python version: {sys.version}")

#10.Write a script that takes user input and saves it to a file named output.txt.
user_input = input("Enter some text to save in output.txt: ")
with open("output.txt", "w") as file:
    file.write(user_input)

# Section 6: Medium Level (8 Qs)
# 1.Write a script to count the number of words in a given string.
def count_words(string):
    words = string.split()
    return len(words)
input_string = input("Enter a string to count words: ")
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")    

# 2. Take a sentence from the user and print:Total words and Total characters (excluding spaces)
def count_sentence_details(sentence):
    words = sentence.split()
    total_words = len(words)
    total_characters = len(sentence.replace(" ", ""))
    return total_words, total_characters
input_sentence = input("Enter a sentence: ")
total_words, total_characters = count_sentence_details(input_sentence)
print(f"Total words: {total_words}, Total characters (excluding spaces): {total_characters}")

# 3.Write a program to simulate a simple calculator (add, subtract, multiply, divide).
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = num1 + num2
            operation = "Addition"
        elif choice == '2':
            result = num1 - num2
            operation = "Subtraction"
        elif choice == '3':
            result = num1 * num2
            operation = "Multiplication"
        elif choice == '4':
            if num2 != 0:
                result = num1 / num2
                operation = "Division"
            else:
                return "Error! Division by zero."
        
        return f"{operation} Result: {result}"
    else:
        return "Invalid Input"
print(calculator())

# 4.Take a comma-separated list of integers from input, then print:Sorted list and Sum of numbers
def process_numbers(input_string):
    numbers = list(map(int, input_string.split(',')))
    sorted_numbers = sorted(numbers)
    total_sum = sum(numbers)
    return sorted_numbers, total_sum
input_numbers = input("Enter a comma-separated list of integers: ")
sorted_list, total_sum = process_numbers(input_numbers)
print(f"Sorted list: {sorted_list}, Sum of numbers: {total_sum}")

#5.Write a script that reads a text file and counts how many times the word “Python” appears.
def count_word_in_file(filename, word):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            return content.lower().count(word.lower())
    except FileNotFoundError:
        return "File not found."
filename = input("Enter the filename to search for the word 'Python': ")
word_count = count_word_in_file(filename, "Python")
print(f"The word 'Python' appears {word_count} times in the file.")

# 6.Write a program to generate a multiplication table for a given number up to 10.
def multiplication_table(number):
    table = []
    for i in range(1, 11):
        table.append(f"{number} x {i} = {number * i}")
    return table
number = int(input("Enter a number to generate its multiplication table: "))
table = multiplication_table(number)
for line in table:
    print(line)

# 7.Create a script that prints the current working directory using os module.
import os
def print_current_directory():
    current_directory = os.getcwd()
    return f"Current working directory: {current_directory}"
print(print_current_directory())

# 8.Write a program to generate a cube of the input number N from user
def cube_of_number(n):
    return n ** 3   
n = int(input("Enter a number to find its cube: "))
cube_result = cube_of_number(n)
print(f"The cube of {n} is {cube_result}.")


