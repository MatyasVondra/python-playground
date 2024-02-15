# Use for, .split(), and if to create a Statement that will print out words that start with 's':
print('\n1\n')
st = 'Print only the words that start with s in this sentence'
words = st.split()

for word in words:
    if (word[0] == 's'):
        print(word)

# Use range() to print all the even numbers from 0 to 10.
print('\n2\n')
print(list(range(0,11,2)))

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('\n3\n')
myList = [num for num in range(1,51) if (num%3 == 0)]
print(myList)

# Go through the string below and if the length of a word is even print "even!"
print('\n4\n')
st = 'Print every word in this sentence that has an even number of letters'
words = st.split()
for word in words:
    if len(word)%2 == 0:
        print(word +' even!')
    continue

# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz"
# instead of the number, and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".
print('\n5\n')
for num in range (1,101):
    if num%3 == 0 and num%5 == 0:
        print('FizzBuzz')
    elif num%3 == 0:
        print('Fizz')
    elif num%5 ==0:
        print('Buzz')
    else:
        print(num)

# Use List Comprehension to create a list of the first letters of every word in the string below:
print('\n6\n')
st = 'Create a list of the first letters of every word in this string'
words = st.split()
firstLetters = [word[0] for word in words]
print(firstLetters)