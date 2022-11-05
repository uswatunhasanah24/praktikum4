import random
y = int(input("masukkan nilai Y : "))
for u in range(y):
    a = random.uniform(0.0, 0.5)
    print("data ke :", u+1, "=> ", a)
print('selesai')