n = 0
r = 5
for m in range(1, r+1):
   for gap in range(0, (r-m)+1):
      print(end=" ")
   while n != (2*m-1):
      print(" *", end="")
      n = n + 1
   n = 0
   print()

