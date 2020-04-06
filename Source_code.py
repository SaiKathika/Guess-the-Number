import simplegui
import random
import math

count = 0
num_range = 100

secret_number = 0

def new_game():
    global num_range, secret_number
    if num_range==100:
        range100()
        secret_number = random.randrange(0,100)
    elif num_range==1000:
        range1000()
        secret_number = random.randrange(0,1000)
        
def range100():
    global count, num_range
    num_range = 100
    print "New game. Range is [0,100)"
    count = 7
    print "Number of remaining guesses is", count
    
def range1000():
    global count, num_range, secret_number
    num_range = 1000
    secret_number = random.randrange(0,1000)
    print "New game. Range is [0,1000)"
    count = 10
    print "Number of remaining guesses is", count

def input_guess(guess):
    global count
    print
    y = int(guess)
    print "Guess was", y
    
            
    if y > secret_number:
        count-=1
        if count==0:
            print "Number of remaining guesses is", count
            print "You ran out of guesses.  The number was", secret_number
            print
            new_game()
        else:    
            print "Number of remaining guesses is", count
            print "Lower!"
        
        
    elif y < secret_number:
        count-=1
        if count==0:
            print "Number of remaining guesses is", count
            print "You ran out of guesses.  The number was", secret_number
            print
            new_game()
        else:    
            print "Number of remaining guesses is", count
            print "Higher!"
        
        
    elif y == secret_number:
        count-=1
        print "Number of remaining guesses is", count
        print "Correct!"
        print
        new_game()    

frame = simplegui.create_frame("Guess the number", 200, 200)
b1 = frame.add_button("Range[0,100)", range100, 200)
b2 = frame.add_button("Range[0,1000)", range1000, 200)
inp = frame.add_input("Guess number", input_guess, 200)


new_game()
frame.start()

