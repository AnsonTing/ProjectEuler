# Project Euler No. 54

number = list('23456789TJQKA')
symbol = list('DCHS')

def compareCard(card1, card2):
    # return 1 if card1 has a higher value than card2, else -1
    n1 = card1[:-1]
    n2 = card2[:-1]
    if number.index(n1) > number.index(n2):
        return 1
    if number.index(n1) < number.index(n2):
        return -1
    s1 = card1[-1]
    s2 = card2[-1]
    if symbol.index(s1) > symbol.index(s2):
        return 1
    if symbol.index(s1) < symbol.index(s2):
        return -1

def isRoyalFlush(cards):
    # return the card with the highest value if the cards are royal flush
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    if numbers == list('TJQKA') and all(symbols[i] == symbols[i+1] for i in range(4)):
        return cards[-1]
    return False

def isStraightFlush(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    if all(number.index(numbers[i+1]) - number.index(numbers[i]) == 1 and symbols[i] == symbols[i+1] for i in range(4)):
        return cards[-1]
    return False

def isFourOfAKind(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    for n in numbers:
        if numbers.count(n) == 4:
            return n + 'S'
    return False

def isFullHouse(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    if any(numbers.count(n) == 3 for n in numbers) and any(numbers.count(n) == 2 for n in numbers):
        for n in numbers:
            if numbers.count(n) == 3:
                if n + 'S' in cards:
                    return n + 'S'
                else:
                    return n + 'H'
    return False

def isFlush(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    if all(symbols[i] == symbols[i+1] for i in range(4)):
        return cards[-1]
    return False

def isStraight(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    if all(number.index(numbers[i+1]) - number.index(numbers[i]) == 1 for i in range(4)):
        return cards[-1]
    return False

def isThreeOfAKind(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    for n in numbers:
        if numbers.count(n) == 3:
            if n + 'S' in cards:
                return n + 'S'
            else:
                return n + 'H'
    return False

def isTwoPairs(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    pairs = []
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 2 and numbers[i] in numbers[:i]:
            pairs.append(numbers[i] + symbols[i])
    if len(pairs) == 2:
        pairs.sort(cmp=compareCard)
        return pairs[-1]

def isOnePair(cards):
    cards.sort(cmp=compareCard)
    numbers = []
    symbols = []
    for card in cards:
        numbers.append(card[:-1])
        symbols.append(card[-1])
    pairs = []
    for i in range(len(numbers)):
        if numbers.count(numbers[i]) == 2 and numbers[i] in numbers[:i]:
            pairs.append(numbers[i] + symbols[i])
    if len(pairs) == 1:
        return pairs[0]

def player1Wins(player1Card, player2Card):
    compareFunctions = [isRoyalFlush, isStraightFlush, isFourOfAKind, isFullHouse, isFlush, isStraight, isThreeOfAKind, isTwoPairs, isOnePair]
    for f in compareFunctions:
        r1 = f(player1Card)
        r2 = f(player2Card)
        if r1 and not r2:
            return True
        if not r1 and r2:
            return False
        if r1 and r2:
            if compareCard(r1, r2) == 1:
                return True
            else:
                return False
    player1Card.sort(cmp=compareCard)
    player2Card.sort(cmp=compareCard)
    if compareCard(player1Card[-1], player2Card[-1]) == 1:
        return True
    else:
        return False

def solution():
    # print isRoyalFlush(['JS', 'TS', 'QS', 'AS', 'KS'])
    # print isStraightFlush(['JS', 'TS', 'QS', '9S', 'KS'])
    # print isFourOfAKind(['AS', '5D', '5H', '5S', '5C'])
    # print isFullHouse(['5D', '5H', '5C', '3S', '3D'])
    # print isFlush(['4D', '6D', '7D', 'TD', 'KD'])
    # print isStraight(['3D', '4H', '5H', '7H', '6D'])
    # print isThreeOfAKind(['3D', '3H', '3C', '4C', '5C'])
    # print isTwoPairs(['5D', '5S', '7H', '3C', '3D'])
    # print isOnePair(['4D', '4C', '6D', '9H', 'KD'])

    f = open('poker.txt')
    player1Cards = []
    player2Cards = []
    line = f.readline()

    while line.strip(' '):
        cards = line.split()
        player1Cards.append(cards[:5])
        player2Cards.append(cards[5:10])
        line = f.readline()

    f.close()

    cnt = 0
    for i in range(len(player1Cards)):
        if player1Wins(player1Cards[i], player2Cards[i]):
            cnt += 1

    return cnt



print solution()
