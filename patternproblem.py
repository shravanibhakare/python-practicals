def pattern(n):
    num = 1 + n * 2  # for number of iterations of loop

    if n == 0:
        y = 0
    else:
        y = n * 3
      
     

    for i in range(num):
       
        for j in range(num):
            if i == n and j == n:
                print(n, end="")
            
            if (i + j == n) or (i - j == n) or (j - i == n) or (i + j == y):
                print("*", end="")
            else:
                print(" ", end="")
       	
        print()
      #  for i in range(num):
       # 	if( i == num):
        #		for j in range(num):
        	#		print("*", end = " ")
       # for j in range(num):
        #	print("*", end="")
       # print()

n = int(input("Enter the num: "))
pattern(n)

