'''
This program is the command line interface for the classic hasbro game Simon.
Created Fall 2016
Final Project
@author Ian Christensen (igc2)
'''

def Simon_CLI():
    ''' This game logic method allows a user to play a game of Simon.'''
    
    # Import libraries
    from random import randint
    import time
    
    # Assign variables
    sequence = ''
    turn = 0
    exit = 0
    
    # Begin loop
    while True:
        
        # Exits loop when user loses
        if exit == -1:
            break
        
        print('\n' * 100)
        
        # Create random color
        color = randint(1, 4)
        if color == 1:
            sequence += 'G'
        if color == 2:
            sequence += 'R'
        if color == 3:
            sequence += 'B'
        if color == 4:
            sequence += 'Y'
        
        # Print the color sequence
        for char in sequence:
            time.sleep(.5)
            print(char)
        
        # Notify user that their turn has begun
        time.sleep(.5)
        print('\n' * 100)
        print('Your turn:')
        
        # Prompt the user for the color sequence
        for char in sequence:
            attempt = input().upper()
            
            # If the user's attempt was incorrect exit the game
            if attempt != char:
                print('You Lost!\nScore: %d' % turn)
                exit = -1
                break
            
        # Iterate the turn value
        turn += 1

Simon_CLI()
