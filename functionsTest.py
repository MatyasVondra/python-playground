#LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even,
#but returns the greater if one or both numbers are odd
print('\nExercise 1\n')
def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
print(lesser_of_two_evens(2,5))

#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
print('\nExercise 2\n')
def animal_crackers(text):
    splitString = text.split()
    if len(splitString) != 2:
        return "The string contains more than two words"
    else:
        if splitString[0][0] == splitString[1][0]:
            return True
        else:
            return False
print(animal_crackers("Bobby Barracuda"))

#MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20.
# If not, return False
print('\nExercise 3\n')
def makes_twenty(n1,n2):
    if (n1+n2 == 20):
        return True
    elif n1 ==20:
        return True
    elif n2 == 20:
        return True
    else:
        return False
print(makes_twenty(1,19))


#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
print('\nExercise 4\n')
def old_macdonald(name):
    newName = name.replace(name[0],name[0].capitalize())
    newName = newName.replace(newName[3], newName[3].capitalize() )
    name[0] == name[0].capitalize()
    name[3] == name[3].capitalize()
    return newName
print(old_macdonald("macdonald"))

#MASTER YODA: Given a sentence, return a sentence with the words reversed
print('\nExercise 5\n')
def master_yoda(text):
    splitedText = text.split()
    splitedText.reverse()
    return " ".join(splitedText)
print(master_yoda("Hello World"))

#ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200
print('\nExercise 6\n')
def almost_there(n):
    if abs(100-n) <= 10:
        return True
    elif abs(200-n) <= 10:
        return True
    else:
        return False
print(almost_there(300))

#FIND 33: Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
print('\nExercise 7\n')
def find_33(param):
    for item in param:
        if item == 3:
            if param[param.index(item)-1] == 3 or param[param.index(item)+1] == 3:
                return True
            else:
                continue
        else:
            continue
    else:
        return False
print(find_33([1,3,1,3]))

#PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
print('\nExercise 8\n')
def paper_doll(input):
    newString = list()
    for i in range(0,len(input)):
        for x in range(3):
            newString.append(input[i])
    return ''.join(newString)
print(paper_doll("Hello"))

#BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
#If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
print('\nExercise 9\n')
def black_jack(num1, num2, num3):
    totalSum = 0
    containsEleven = False
    numbers = [num1,num2,num3]
    for num in numbers:
        totalSum += num
        if num == 11:
            containsEleven = True
    if totalSum <= 21:
        return totalSum
    elif containsEleven:
        return totalSum-10
    else:
        return "BUST"
print(black_jack(9,9,11))

#SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 9 (every 6 will be followed by at least one 9).
# Return 0 for no numbers.
print('\nExercise 10\n')
def summer_69(input):
    totalSum = 0
    dontCount = False
    for item in input:
        if item == 6:
            dontCount = True
        if dontCount and item == 9:
            dontCount = False
            continue
        if dontCount:
            continue
        if dontCount == False:
            totalSum += item
    return totalSum
print(summer_69([1,6,9,1,1,9,6,1,1,9,1]))

#SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
print('\nExercise 11\n')
def spy_game(param):
    for item in param:
        if item == 0:
            if param[param.index(item)+1] == 0 and param[param.index(item)+2] == 7:
                return True
            else:
                continue
        else:
            continue
    else:
        return False
print(spy_game([1,3,1,0,0,7,0]))

#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
print('\nExercise 12\n')
def count_primes(number):
    numberOfPrimes = 0
    for num in range(2,number):
        for div in range(2, num):
            if num % div == 0:
                break
        else:
            numberOfPrimes+=1
    return numberOfPrimes
print(count_primes(100))

#PRINT BIG: Write a function that takes in a single letter, and returns a 5x5 representation of that letter
print('\nExercise 13\n')
def print_big(input):
    letterDictionary = {"A" : ["  *  ", " * * ", "*****", "*   *", "*   *"],
                        "B" : ["*****", "*   *", "*****", "*   *", "*****"]}
    preparedList = list()
    for i in range(0,5):
        preparedList.append(letterDictionary[input][i])
    return "\n".join(preparedList)
print(print_big("B"))