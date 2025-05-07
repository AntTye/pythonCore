#Python was first created in 1991 by Guido van Rossum, intended to be a general-purpose programming language that is easy to learn, understand, and use. "It has later evolved into one of the most popular languages in the world, widely used in fields such as web development, data science, artificial intelligence, automation, and software engineering, thanks to its readable syntax, large standard library, and an active open-source community" (GPT).

#I entend to entry my entire process for learning starting with types and ending who knows where. Gaining proficiency in being a software devloper and coder. This is right before my graduation in 2025 from UConn as CSE :)

#Python is a high-level programming langauge. That does not mean it take high-skill to start learning and getting good at programming with it. Rather it means many of the low-level details are abstracted away to make it easier to be understood by humans. It is a blueprint for the language; Python is not a program itself but instead we need something that understands and executes it. CPython does that.

# - Abstraction means to be lifted from complexity to a more simplistic system, sheilding the unnecessary deatils to allow developers to work at a "higher" level without needing to know the machine code for example.
# - An abstraction is the IO type/operations. Things like open() and read() are abstracting nuances explaining how files are handled by the OS that exist at a "lower" level.

#CPython is the reference/primary implementation for Python, built with C and used in the interpreter. A interpreter is a program that translates and executes source code line by line rather than being compiled to machine code before execution within the compliler. Generally with smaller programs and scripts the time difference between the two is negligible but compilers are generally much much faster.

#C is a compiler level language and was chosen to the the foundational language for Python as CPython. Becuase it is low level it has access to "more" having more freedom in the structure of memory. "More" freedom with C means direct memory accesses with pointers, and malloc, ideal for interpreters. This allows for efficient memory management and low level operations to apply to Python which it was built for. This is a key reason Python was built upon C for performance, portability (C is portable) and control at a low level. There are others however, Jython, and IronPython.

# - CPython parses the .py file for its code into a Abstract Synatx Tree. It then compiles it into bytecode, .pyc files, and interprets and runs the bytecode on its virtual machine.

### CRUX 1

#In Python everything is known to be an object.

#All Objects live within the heap. The stack is the references to these objects within the heap. 

#When Objects are created, memory is allocated for it on the heap and the reference to that memory location is stored on the stack in blocks. 

#Variables are what reside on the stack to point to values within the heap. If we had x = 5, x would be the reference to the memory location of int 5.

#These Objects includes typical data types such as int, float, complex bool, str. 

"""
In Haskell we have data types and newtypes. In Python types are built in but we cannot implement behaviors of typeclasses like semigroups, monoids, functors, applicatives, monads, foldables by default.

We have to manually implement them. They would have to be initialized by a class whcih is a bundle of attributes and methods, data and behavior associated.

More later in the ###_class.py.
"""

#Objects also Includes more complex data types like lists [], tuples (), sets {}, and dictionaries {}. Also complex numbers where its represented as real + imagj where imag is a float and j is the imaginary unit.

#Local Variables do not possess fixed types themselves, the objects that the variables reference to have the types.

### Crux 2

#Variables are references that bind names to objects, any mutation towards that heap object is applicable to all other variables binded to that same memory location. Only affects mutable objects such as a list but tuples are not, you can't modify the tuple after creation.
