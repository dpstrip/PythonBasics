def average(a,b):
    return (a+b)/2

def squareRoot(num, low, high):
    '''find the square root of a num
    by playing the Number gussing game
    strategy by gussing over the range
    from low to high '''

    for i in range(50):
        guess = average(low, high)
        #print('The average is: ',  guess, ' High: ', high, ' Low: ', low)
        if guess**2 == num:
            print(guess)
        elif guess**2 > num: #"guess lower."
            high = guess
        else: #Guess higher."
            low = guess
        print(guess)

    return guess

guess = squareRoot(1000, 1, 1000/2)
print('1000 Final answer is: ', guess, ", ", guess**2)

guess = squareRoot(60, 7,8)
print('60 Final answer is: ', guess, ", ", guess**2)
guess = squareRoot(200, 10, 20)
print('200 Final answer is: ', guess, ", ", guess**2)

guess = squareRoot(50000, 1, 50000/2)
print('50000 Final answer is: ', guess, ", ", guess**2)

'''The idea is that give a number I use the
gussing game to find the sq root by
guessing.  I compare the guess * guess to
the number.  High and low reassigned by result
of the guess. '''

