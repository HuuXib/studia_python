# Napisz program, który pobiera dwie liczby A i B (A musi być < od B). Następnie 
# wyświetla wszystkie wartości od A do B, czyli wartości A, A+1, A+2, ..., B. 

A = int(input('Podaj A:'))
B = int(input('Podaj B:'))
# while True:
#     print(A)
#     if A>=B:
#         break
#     A += 1

for i in range(B):
    print(A)
    if A >=B:
        break
    A += 1