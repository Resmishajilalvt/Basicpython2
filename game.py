number = 23 
running = True
while running:
    guess = int(input('enter the number'))
    if guess == number: 
        print 'congrates'
        running == False
    elif guess < number:
         print 'number is little bit greater'
    else:
          print 'number is little bit lesser'
print 'while loop is over'

