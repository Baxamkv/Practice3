def summa(*args):
    sm = 0
    for i in args:
        sm+=i
    return sm

print(summa(1,2,3,4))

def student(**kwargs):
    for i, j in kwargs.items():
        print(i, j)

student(name="Alex",age = 30, GPA = 3.5)

