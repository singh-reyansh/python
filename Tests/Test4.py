"""
Reyansh -- Python Test
Date: 29-09-2025
Section A : True / False

1. Python is case sensitive when dealing with identifiers. 
yes
2. Can mathematical operations be directly performed on a string in Python without conversion?
No
3. The expression 2**2**3 is evaluates as: (2**2)**3.
yes
4. What will be the output of the following Python code snippet?
"""
print(bool('False'))
""" False
5. The expression int(x) implies that the value of variable x is converted to integer.
yes
6. The value of the expressions 4/(3*(2-1)) and 4/3*(2-1) is the same.
Yes
7. In Python, lists are immutable, meaning their elements cannot be changed after creation.
No
8. Python’s set data type allows duplicate elements.
yes
9. The break statement in a loop terminates only the innermost loop it is contained within.
yes
10. A Python function must always include a return statement.
yes
---------------------------------------------------------------------------
Section B : MCQs
---------------------------------------------------------------------------
11. What will be the output of the “hello” +1+2+3?
a) hello123
b) hello
c) Error
d) hello6      d

12. What is “Hello”.replace(“l”, “e”)?
a) Heeeo
b) Heelo
c) Heleo
d) None      b

13. What will be the output of the following Python code?
"""
print("xyyzxyzxzxyy".count('yy'))
"""
a) 2
b) 0
c) error
d) none of the mentioned         a

14. What will be the output of the following Python statement?
"""
print(chr(ord('A')))
"""
a) A
b) B
c) a
d) Error     a

15. What will be the output of the following Python statement?
"""
print(chr(ord('b')+1))
"""
a) a
b) b
c) c
d) A       c
16. Which of the following is not allowed in Python?
a) _a = 1
b) __a = 1
c) __str__ = 1
d) none of the mentioned   c

17. Which of the following is not a keyword in Python?
a) eval
b) assert
c) nonlocal
d) pass      c

18. Which of the following is an invalid statement?
a) abc = 1,000,000
b) a b c = 1000 2000 3000
c) a,b,c = 1000, 2000, 3000
d) a_b_c = 1,000,000       c

19. What will be the output of the following Python code?
"""
example = "helle"
print(example.find("e"))
"""
a) Error
b) -1
c) 1
d) 0         b

20. Which one of these is floor division?
a) /
b) //
c) %
d) None of the mentioned      c

21. What is the answer to this expression, 22.0 % 3 is?
a) 7
b) 1
c) 0
d) Error  7

22. Given a function that does not return any value, what is the default return value when it is executed in the Python shell?
a) int
b) bool
c) void
d) None       d

23. What will be the output of the following Python code?
str1="helloworld"
print(str1[::-1])
a) dlrowolleh
b) hello
c) world
d) helloworld    c

24. What will be the output of the following Python code?
"""
print(max("what are you"))
"""
a) error
b) u
c) t
d) y      u

25. What error occurs when you execute the following Python code snippet?
apple = mango
a) SyntaxError
b) NameError
c) ValueError
d) TypeError    c

26. What will be the output of the following Python code snippet?
"""
def example(a):
    a = a + '2'
    a = a*2
    return a
example("hello")
"""
a) Indentation Error
b) Cannot perform mathematical operation on strings
c) hello2
d) hello2hello2        d

27. Which of the following will print this output?

hello-how-are-you
a) print(‘hello’, ‘how’, ‘are’, ‘you’)
b) print(‘hello’, ‘how’, ‘are’, ‘you’ + ‘-‘ * 4)
c) print(‘hello-‘ + ‘how-are-you’)
d) print(‘hello’ + ‘-‘ + ‘how’ + ‘-‘ + ‘are’ + ‘you’)     d

28. What is the output of print 0.1 + 0.2 == 0.3?
a) True
b) False
c) Machine dependent
d) Error         a

29. Which of the following is incorrect in Python?
a) float(‘inf’)
b) float(‘nan’)
c) float(’56’+’78’)
d) float(’12+34′)   d

30. What is the result of round(0.5) – round(-0.5)?
a) 1.0
b) 2.0
c) 0.0
d) Value depends on Python version      b

31. What will be the output of the following Python code snippet?
"""
x = 1 
x<<2
"""
a) 8
b) 1
c) 2
d) 4     a

32. Which of the following expressions results in an error?
a) float(‘10’)
b) int(‘10’)
c) float(’10.8’)
d) int(’10.8’)     a

33. What will be the output of the following Python expression?
"""
print(bin(29))
"""
a) 0b10111
b) 0b11101
c) 0b11111
d) 0b11011

34. What will be the output of the following Python expression?
"""
print(int(1011))
"""
a) 1011
b) 11
c) 13
d) 1101     a

35. What will be the output of the following Python expression?
"""
x=15
y=12
x & y
"""
a) b1101
b) 0b1101
c) 12
d) 1101       

36. Which of the following expressions can be used to multiply a given number ‘a’ by 4?
a) a<<2
b) a<<4
c) a>>2
d) a>>4     b

 
37. What will be the output of the following Python code snippet?
"""
print(['hello', 'morning'][bool('')])
"""
a) error
b) no output
c) hello
d) morning       a
 
38. What will be the output of the following Python code?
"""
i = 1
while True:
    if i%3 == 0:
        break
    print(i)
    i += 1

"""
a) 1 2
b) 1 2 3
c) SyntaxError
d) none of the mentioned       d

39. What will be the output of the following Python code?

True = False
while True:
    print(True)
    break
a) True
b) False
c) ERROR
d) none of the mentioned    a

40. What will be the output of the following Python code?
"""
x = "abcdef"
i = "a"
while i in x:
    print(i, end = " ")
"""
a) no output
b) i i i i i i …
c) a a a a a a …
d) a b c d e f     c

41. What will be the output of the following Python code snippet?
"""
x = 'abcd'
for i in range(len(x)):
    i.upper()
print (x)

"""
a) ABCD
b) 0123
c) error
d) none of the mentioned       c

42. What will be the output of the following Python code?
"""
d = {0, 1, 2}
for x in d.values():
    print(x)
"""
a) 0 1 2
b) None None None
c) error
d) none of the mentioned    a

43. What will be the output of the following Python code?
"""
d = {0, 1, 2}
for x in d:
    print(d.add(x), end=" " )
"""
a) 0 1 2
b) 0 1 2  0 1 2 0 1 2
c) None None None
d) None of the mentioned    a

44. What will be the output of the following Python code?
"""
for i in range(0):
    print(i)
"""
a) 0
b) no output
c) error
d) none of the mentioned     b

45. What will be the output of the following Python code snippet?
"""
a = [0, 1, 2, 3]
for a[0] in a:
    print(a[0], end=" ")
"""
a) 0 1 2 3
b) 0 0 0 0
c) 3 3 3 3
d) error        b

46. What will be the output of the following Python statement?
"""
print("abcd"[2:])
"""
a) a
b) ab
c) cd
d) dc  b

-----------------------------------------------------------------------------------
SECTION C : CODING QUESTIONS
-----------------------------------------------------------------------------------
47. Find the Largest Element in the List [10,9,2,3,8,4,7]. 
def 

48. Write a Program to find the sum of all the elements of the list [12,32,54,87,56].

49. Write a program to count the number of Vowels in the string "PythonCourseOnline".

50. Write a Program that calculatesd the difference between the product of even and odd numbers in the list. [10,9,2,3,8,4,7]

"""