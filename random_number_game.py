import random
def guess_the_number(rand_num):
	chance = 5
	points = 25
	print("Hello dear player!")
	while(chance > 0):
		print("enter the number")
		num = int(input())
		if num == rand_num:
			print( f"congratulations! you won. You earned {points} points")
			break
		elif num > rand_num:
			print("you entered large number")
			chance-=1
			points-=5
		else:
			print("you entered small number")
			chance-=1
			points -=5
	else:
		print(f"Oops! you loose the game. The number was {rand_num}")
rand_num = random.randint(1,100)
guess_the_number(rand_num)	
