n = 100000000
sum = 0
u = 0
laba = [int(0), int(0), int(n) * 0.01, int(n) * 0.01, int(n) * 0.05, int(n) * 0.05, int(n) * 0.02]
for i in laba:
    sum = sum+i
    u +=1
    print('total bulan ke-', u, 'sebesar : ', i)
print('total laba adalah : ',sum)