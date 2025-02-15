
PYTHON INTRODUCTION
----------------------------------------------------------------------------------------

1. PYTHON FEATURES

   --1.easy to learn
     2.easy to read
     3.easy to maintaince
     4.a broad standard library
     5.interactive mode
     6.portable
     7.python is intrepreted
     8.python is object oriented
-------------------------------------------------------------------------------------------
2. ADVANTAGES AND DISADVANTAGES
  
   -- Advantages of python

     1.It is easy to learn and use,and it has an extensive library.	   
     2.Python increases productivity.	          
     3.It is very flexible.	                          
     4.It has a very supportive community.
	        
   -- Disadvantages of python

     1.Because of its elementary programming, users face difficulty while working with other programming languages.
     2.Python is a time-consuming language. It has a low execution speed.	                        
     3.There are many issues with the design of  the language, which only gets displayed during runtime.	        
     4.It is not suited for memory-intensive programs and mobile applications.
---------------------------------------------------------------------------------------------------------------------
3. COMPILE TINE VS RUN TIME

     --- compile time is the period when the programming code is converted to machine code.
    ---  Runtime is the when a program is running and generally occurs after compile time 
 ------------------------------------------------------------------------------------------------------------------
4. WHY PYTHON IS CALLED INTREPRETTED PROGARMMING LANGUAGE

   -- python is called intrepretted langauge because it goes through an intrepreter ,which turns the code you
      write into the language understood by computers proccessor
---------------------------------------------------------------------------------------------------------------------
5. TOKENS IN PYTHON

  -- A token is the smallest individual unit in python program.all statements and instructions in a
     program are built with tokens
---------------------------------------------------------------------------------------------------------------------
6.MEMORY MANAGEMENT IN PYTHON

   -- Memory management in Python involves a private heap containing all Python objects and data structures. 
      The management of this private heap is ensured internally by the Python memory manager.
------------------------------------------------------------------------------------------------------------------
7.GARBAGE COLLECTION HOW IT WORKS

  --- python deletes unwanted objects automatically to free the memory space.the process by which periodically
      frees and reclaims the blocks of memory that no longer are in use is called garbage collection
----------------------------------------------------------------------------------------------------
8. .PY VS .PYC FILE

   -- .py files contain the source code of a program.where as .pyc file contains the byte code of your program.
--------------------------------------------------------------------------------------------------------------------------------
9.HOW PYTHON PROGRAM EXECUTES INTERNALLY

  --Step 1:  The python compiler reads a python source code or instruction. Then it verifies that the instruction is well-formatted,
             i.e. it checks the syntax of each line. If it encounters an error, it immediately halts the translation and 
             shows an error message.

  --Step 2: If there is no error, i.e. if the python instruction or source code is well-formatted then the
           compiler translates it into its equivalent form in an intermediate language called “Byte code”.

  --Step 3: Byte code is then sent to the Python Virtual Machine(PVM) which is the python interpreter.
            PVM converts the python byte code into machine-executable code.
            If an error occurs during this interpretation then the conversion is halted with an error message
--------------------------------------------------------------------------------------------------------------------------
10.PYTHON IS DYNAMICALLY PROGRAMMING LANGUAGE.WHY?

  -- We don't have to declare the type of variable while assigning a value to a variable in Python.
    Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.
    It states the kind of variable in the runtime of the program. So, Python is a dynamically typed language
