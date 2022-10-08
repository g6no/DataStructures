# Name: Ahmad Alqattan      ID:2192131011

n = int(input("Please enter the number of rows:"))
num = 1
for i in range(1,n+1):
    for j in range(i):
        print(f"{num}", end=" ");
        num += 1
    print()



# Please enter the number of rows:6
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21