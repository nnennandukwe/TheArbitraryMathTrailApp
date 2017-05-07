import random

print 'Welcome to the Arbitrary Math Quiz Game!'
print 'I am Nnenna, the computer. Follow the instructions carefully to keep up.'
print 'Get a single answer wrong and you lose. No pressure, though.'
print 'Alright, happy Python-ing!'      

person = input('Want to roll the dice? ')
if person == 'yes':
  dice_roll = random.randrange(1,7)
  print dice_roll
  person = int(input('What number did you get? '))
  if person == 1:
    person = int(input('Multiply it by the # of sides (faces) a dice has \n and enter your answer: '))
    if person == 6:
      print 'Did you get to 6? Thought so.'
      print 'You win! Congrats. Play again.'
    else:
      print 'You lose. Start over, buddy.'
  elif person == 2:
    person = int(input('How many people are in a quadruplet? Add that # to your answer above: '))
    if person == 6:
      print 'Did you get to 6? Thought so.'
      print 'You won! Game over :)'
    else:
      print 'You snooze, you lose...'
  elif person == 3:
    person = int(input('What is the square root of 81? Now subtract your previous answer from your new one: '))
    if person == 6:
      print 'Did you get to 6? Thought so.'
      print 'You won! Congrats & game over.'
    else:
      print 'Boo.. start over.'
  elif person == 4:
    person = int(input('What is the square root of that number? Add your two answers together: '))
    if person == 6:
      print 'Did you get to 6? Thought so.'
      print 'You won! Congrats, play again.'
    else:
      print 'Yikes.. brush up on your math. Start over.'
  elif person == 5:
    person = int(input('How many glass slippers did Cinderalla leave behind \n when the clock struck 12? Add that # to your previous answer: '))
    if person == 6:
      print 'Did you get to 6? Of course you did...'
      print 'Congrats, you win. Play again, shall we?'
    else:
      print 'Bloop. Wrong answer. Play again.'
  elif person == 6:
    person = int(input('Is Pluto in our solar system? \'5\' for yes, \'6\' for no: '))
    if person == 6:
      print 'Clever hobbit! You got 6, right? You win. Play again.'
    else:
      print 'SMH. Try again...'
  else:
    print 'That was not your #. Game over.'
if person == 'no':
  print 'Well then the game surely ended before it even started...Bye now.'
  
  
  
  