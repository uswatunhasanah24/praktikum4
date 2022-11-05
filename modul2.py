print("modul2 praktikum2")

A = int (input("masukkan bilangan pertama:"))
B = int (input("masukkan bilangan kedua:"))
C = int (input("masukkan bilangan ketiga:"))

if A > B > C :
    print("\nBilangan pertama adalah bilanagn terbesar = %s" % A)
elif B > C :
    print("\nBilangan kedua adalah bilangan terbesar = %s" % B)
else :
    print("\nBilangan ketiga adalah bilangan terbesar = %s" % C)