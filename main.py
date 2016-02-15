def generate_first_number(value):
    znaleziona = False
    i = value + 1
    while not (znaleziona):
        pierwsza = True
        for n in range(2, i):
            if i % n == 0:
                pierwsza = False
                break
        if i % 4 == 3:
            znaleziona = True
        else:
            i += 1
    return i


def generate_next_number(value, m):
    return value ** 2 % m


def seryjnyTest(bitArray):
    x = 1
    prev = ' '
    nexte = ' '
    first = 0
    second = 0
    third = 0
    fourth = 0
    for i in range(len(bitArray)-1):
        prev = bitArray[i]
        nexte = bitArray[x]
        if prev == '0' and nexte == '0':
            first += 1
        if prev == '0' and nexte == '1':
            second += 1
        if prev == '1' and nexte == '0':
            third += 1
        if prev == '1' and nexte == '1':
            fourth += 1
        x += 1
    print "Seryjny test:", first, second, third, fourth


def pokerowyTest(bitArray):
    m = 4
    max = 0
    ile = 0
    secondBitArray = bitArray[50:50+m]
    for i in range(len(bitArray)-m):
        yes = True
        for x in range(len(secondBitArray)):
            if bitArray[i+x] != secondBitArray[x]:
                yes = False
        if yes == True:
            ile += 1
    if max < ile:
        max = ile
    print "Pokerowy test:", max


def seriiTest(bitArray, bit):
    ileJeden = 0
    ileDwa = 0
    ileTrzy = 0
    ileCztery = 0
    ilePiec = 0
    ileSzesc = 0
    max = 0
    for i in range(len(bitArray)):
        if bitArray[i] == bit:
            max += 1
        else:
            if max == 0:
                max = 0
            elif max == 1:
                ileJeden += 1
            elif max == 2:
                ileDwa += 1
            elif max == 3:
                ileTrzy += 1
            elif max == 4:
                ileCztery += 1
            elif max == 5:
                ilePiec += 1
            else:
                ileSzesc += 1
            max = 0
    print bit, ":", ileJeden, ileDwa, ileTrzy, ileCztery, ilePiec, ileSzesc


    return bitArray


def main():
    p = generate_first_number(1499)
    q = generate_first_number(p)
    m = p * q
    number = 32562359
    bitArray = []
    outputArray = []
    howManyZero = 0
    howManyOne = 0
    print p, q
    for i in range(20000):
        number = generate_next_number(number, m)
        bitArray = list('{0:0b}'.format(number))
        if bitArray[len(bitArray) - 1] == '0':
            howManyZero += 1
        if bitArray[len(bitArray) - 1] == '1':
            howManyOne += 1
        outputArray.append(bitArray[len(bitArray) - 1])
    print outputArray
    print "Zero:", howManyZero
    print "One:", howManyOne
    seryjnyTest(outputArray)
    pokerowyTest(outputArray)
    seriiTest(outputArray, '0')
    seriiTest(outputArray, '1')


main()
