import numpy as np

def f(x):
    return x**5

a = 2
h = 1
def forward(f,a,h):

    for i in range(20):
        diffrentation = (f(a+h) - f(a))/h
        h /= 2
    return diffrentation

def backward(f,a,h):
    for i in range(20):
        diffrentation = (f(a) - f(a-h))/h
        h /=2
    return diffrentation

def central(f,a,h):
    for i in range(20):
        diffrentation = (f(a+h) - f(a-h))/(2*h)
        h /= 2
    return diffrentation

print(forward(f,a,h))
print(backward(f,a,h))
print(central(f,a,h))