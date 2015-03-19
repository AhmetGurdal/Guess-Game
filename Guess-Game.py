#-*- coding: cp1254 -*-
import random
import time
print "Name?"
ad = raw_input(":")
print "OK, ",ad,"! let's play a game I think a number that between 1 and 1000."
while True:
	print "If u can ,guess"
	num = random.randrange(1,1000)
	ts = 1

	while True: 
		ta = input(":")
		
		if num > ta:
			print "up"
			ts = ts + 1
		
		elif num < ta:
			print "down"
			ts = ts + 1
		
		elif num == ta:
			print "True Guess"
			ts = ts + 1
			
			if ts > 10 and ts <= 15:
				print"U guessed true in" ts,"guesses. Not Bad."
			
			elif ts > 15 and ts <= 20:
				print"U guess true in" ts,"guesses. Really Bad Result."
			
			elif ts > 20:	
				print"U guess true in" ts,"guesses. Too Bad for Humanity."
			
			else:
				print"U guess true in" ts,"guesses. Awesome."
		
			break
	
	print "\nIt's my turn. Now U think a numbet between 1-1000 and i will guess.(press Enter)\n"
	raw_input("")
	print "\nIf I have to increase my guess, enter 'i' (press Enter)\n"
	raw_input()
	print "\nIf I've to decrease my guess, enter'd' If my guess is True, enter 't' (press Enter)\n"
	raw_input()
	print "Think Now!"
	time.sleep(2)
	
	a = 1
	b = 1000
	ts2 = 1
	
	while True:
		num2 = random.randrange(a,b)
		while True:
			print num2
			th = raw_input(":")
			
			if th == "i":
				a = num2 + 1
				ts2 = ts2 + 1
				break
				
			elif th == "d":
				b = num2
				ts2 = ts2 + 1
				break
				
			elif th == "t":
				print "I guess true in "ts2," guesses."
				
				if ts2 > ts:
					print "U beat me. Well Done!" 
					
				elif ts2 < ts:
					print "I bear u. U loser"
					
				elif ts2 == ts:
					print "It's tie."
					
				break
		
			else:
				print "\nIf I have to increase my guess, enter 'i' If I've to decrease my guess, enter'd'\n"
				print "\nIf my guess is True, enter 't'\n"
			
	print "If u wanna play again, enter 'r'"
	yeni = raw_input(":")
	
	if yeni != "r":
		print "\nNice game. Bye!!\n"
		time.sleep(3)
		quit()
	
		
