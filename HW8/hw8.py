from functools import wraps
#_____________________________________________________________________

def log_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"виклик {func.__name__} з args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_args
def add(a, b):
    return a + b

print(add(5, 8))

#виклик add з args=(5, 8), kwargs={}
#13
#_____________________________________________________________________

def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(4)
def greet():
    print("ПуПуПу")

greet()

#ПуПуПу 4 раза каждый с новой строчки
#_____________________________________________________________________

words = ["кіт", "собака", "машина", "дім", "комп'ютер", "сонце"]

long_words = [(i, length) for i in words if (length := len(i)) > 4]

for word, length in long_words:
    print(f"{word} {length} букв")

#собака 6 букв
#машина 6 букв
#комп'ютер 9 букв
#сонце 5 букв
#_____________________________________________________________________

def countdown(n):
    for i in range(n, 0, -1):
        yield i
    yield "Старт!"

# Використання
for step in countdown(3):
    print(step)

#5
#4
#3
#2
#1
#Старт!
#_____________________________________________________________________