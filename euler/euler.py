import math
def thres_and_fives():
    threesAndFives = []
    for num in range (1,1001):
        if num%3 == 0 and num%5 == 0:
            threesAndFives.append(num)
        elif num%3 == 0:
            threesAndFives.append(num)
        elif num%5 ==0:
            threesAndFives.append(num)
        else:
            continue
    print(sum(threesAndFives))

def fibonacci():
    fibonacci = [1,2]
    fibonacciEven = []
    iterator = 2
    while fibonacci[-1] < 4000000:
        fibonacci.append(fibonacci[iterator-1]+fibonacci[iterator-2])
        iterator += 1
    for item in fibonacci:
        if item%2 == 0:
            fibonacciEven.append(item)
    print(sum(fibonacciEven))

def prime_factors():
    task = 13195
    factors = []
    primeFactors = set()
    for a in range(1,task+1):
        for b in range(1,task+1):
            if a*b == task:
                factors.append(a)
    for factor in factors:
        for div in range(2,factor):
            if factor % div == 0:
                break
        else:
            primeFactors.add(factor)
    print(primeFactors)

def palindrome():
    task = 9009
    palindromes = set()
    for a in range (100,1000):
        for b in range (10,1000):
            isPalindrome = False
            listify = list(str(a*b))
            for i in range(0,int(len(listify)/2+1)):
                if listify[i] == listify[-(i+1)]:
                    isPalindrome = True
                    continue
                else:
                    isPalindrome = False
                    break
            if isPalindrome == True:
                palindromes.add(a*b)
    print(max(palindromes))

def highest_power():
    found = False
    iterator = 1
    while found == False:
        isOk = False
        for div in range (1,21):
            if iterator%div == 0:
                isOk = True
                continue
            else:
                isOk = False
                break
        if isOk:
            found = True
            break
        else:
            iterator += 1
            continue
    print(iterator)

def sum_or_squares():
    sumOfSquares = []
    squareOfSum = []
    for num in range(1,101):
        sumOfSquares.append(num**2)
        squareOfSum.append(num)
    result = (sum(squareOfSum)**2)-sum(sumOfSquares)
    print(result)

def thousand_digits():
    kdigit = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450
    stringify = str(kdigit)
    listify = list(stringify)
    products = []
    for i, num in enumerate(listify):
        product = 1
        if i == len(listify)-13:
            break
        for a in range(i,i+13):
            product = product * int(listify[a])
        products.append(product)
    print(max(products))

def sum_and_power():
    target = 1000
    c = 2
    for a in range(1,1001):
        for b in range(1,1001):
            suma = a**2 + b**2
            c = math.sqrt(suma)
            print(a,b,c)
            if a+b+c == target:
                break
            else:
                continue
        if a+b+c == target:
            break
    print(('Gotcha, a={a} b={b} c={c} a+b+c={sum} and a*b*c={power}').format(a=a, b=b, c=c, sum=a+b+c, power=a*b*c))

palindrome()
