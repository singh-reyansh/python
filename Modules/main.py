
### 1. What is a Module?
# - A single .py file containing Python code (functions, classes, variables).
# - Purpose: Code reusability, better organization, readability, and independent testing.

# add.py (a module)
'''
def add(a, b):
    return a + b
'''
'''
# main.py
import add                  # whole module
from add import add         # only the function
from add import add as plus # with alias
print(add(5, 3)) # → 8
'''

'''
**Types of Modules**
| Type              | Example                 | How to use                     |
|-------------------|-------------------------|--------------------------------|
| Built-in          | math, random, os, json  | Already available              |
| User-defined      | add.py, sub.py, greet.py| Create yourself                |
| Third-party       | numpy, requests, django | Install via pip                |

'''
### 2. What is a Package?
# - A folder that contains multiple modules + a special file named __init__.py.
# - Turns a normal folder into an importable package.

'''
**Folder structure example**
```
Calculator/
├── __init__.py          # makes this folder a package
├── add.py
├── sub.py
├── mul.py
└── div/
    ├── __init__.py      # sub-package
    └── advanced_div.py

import Calculator.add
from Calculator import add
from Calculator.add import add
from Calculator.div.advanced_div import something

### 3. Role of __init__.py (Very Important!)
| Purpose                                 | Details                                                                 |
|----------------------------------------|-------------------------------------------------------------------------|
| Marks folder as package                | Without it → just a normal folder (except namespace packages in Py 3.3+)|
| Can be completely empty                | Still works!                                                            |
| Can contain initialization code        | Runs when package is imported                                           |
| Makes importing easier (most used trick) | Example inside Calculator/__init__.py                                   |

'''

### 4. What is a Library?
# - A reusable collection of modules & packages that solve a bigger problem.
# - Can be:
#   - Standard Library → comes with Python (math, os, datetime, json…)
#   - Third-party Library → installed via pip (requests, pandas, flask…)


'''

| Term       | What it is                     | Example                     | Contains __init__.py? | Installed with pip? |
|------------|--------------------------------|-----------------------------|-----------------------|---------------------|
| Module     | Single .py file                | add.py, math.py             | No                    | Sometimes           |
| Package    | Folder with __init__.py        | Calculator, numpy           | Yes                   | Sometimes           |
| Library    | Collection of packages/modules | requests, Django, TensorFlow| Usually many          | Yes (third-party)   |
'''
### 5. How to Create Your Own (Step-by-Step)

# Create a Module
# 1. Create mytools.py
# 2. Write functions inside
# 3. Use import mytools anywhere


# Create a Package
# mycalc/
# ├── __init__.py
# ├── addition.py
# └── subtraction.py

# Create a Full Library

# myawesomelib/
# ├── myawesomelib/
# │   ├── __init__.py
# │   ├── core.py
# │   └── utils.py
# ├── setup.py or pyproject.toml
# ├── README.md
# └── tests/
# ```
# Then run pip install . or upload to PyPI.


# Calculator -- Add , Sub , Mul , Div 

# Modules -- .py File 

# Calculator
#      Add
#          add.py
#      Sub
#          sub.py 
#      Mul 
#          mul.py
#      Div 
#          div.py
#      main.py


# Modular 
#  Code reusability 
#  Readbale 


# Module -- Dir -- .py 

# Built in Modules 
# os, json , datetime , math , random 
# import math 

# print(math.sqrt(16))

# import random 
# print(random.randint(1,100))

# User Defined Modules 
# Greet()

# import firstModule
# firstModule.Greet()
# print(firstModule.x)

# 
# from firstModule import Greet
# Greet()

# 
# from math import sqrt
# print(sqrt(26))


# import firstModule as fm
# fm.Greet()


# pip -- python package manager  -- pip install <packagename> 
# importing multiple modules 

# import os,json , math 
# package -- __init__.py