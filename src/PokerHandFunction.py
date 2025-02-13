cardValue = {
        'A' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5, 
        '6' : 6, 
        '7' : 7, 
        '8' : 8,
        '9' : 9, 
        '10': 10, 
        'J' : 11,
        'Q' : 12,
        'K' : 13
    }

def CheckStraight(cards):
    count = 1
    for index in range(1, 5):
        if int(cardValue[cards[index]]) - 1 == int(cardValue[cards[index - 1]]):
            count += 1
        else:
            count = 1
    
    if count == 5:
        return True
    return False

def SortedCardDetection(pokerHand):
    cards = []
    suits = []
    
    for card in pokerHand:
        if len(card) == 3:
            cards.append(card[:2])
            suits.append(card[-1])
        else:
            cards.append(card[0])
            suits.append(card[-1])
            
    sortedCard = sorted(cards, key=lambda x: int(cardValue[x]))
    return sortedCard, suits

def CheckOtherKinds(cards):
    numOfEachCards = {}
    pokerHandName = ""
    for card in cards:
        if (card not in numOfEachCards):
            numOfEachCards[card] = 1
        else:
            numOfEachCards[card] += 1
    
    if len(numOfEachCards) == 2:
        for numCards in numOfEachCards:
            if numOfEachCards[numCards] == 4:
                pokerHandName = "Four of a kind"
                break
            if numOfEachCards[numCards] == 3:
                pokerHandName = "Full house"
                break
    else:
        countPairs = 0
        countThree = 0
        for numCards in numOfEachCards:
            if numOfEachCards[numCards] == 2:
                countPairs += 1
            if numOfEachCards[numCards] == 3:
                countThree += 1
        if countPairs == 2:
            pokerHandName = "Two pairs"
        elif countPairs == 1:
            pokerHandName = "Pair"
        elif countThree == 1:
            pokerHandName = "Three of a kind"
        else:
            pokerHandName = "High card"
    
    return pokerHandName
    
                

def PokerHandDetection(pokerHand):
    cards, suits = SortedCardDetection(pokerHand)
    pokerHandName = ""
    
    ### Check royal flush
    
    if suits.count(suits[0]) == 5:
        if 'A' in cards and 'K' in cards and 'Q' in cards and 'J' in cards and '10' in cards:
            pokerHandName = "Royal Flush"
        elif CheckStraight(cards):
            pokerHandName = "Straight Flush"
        else:
            pokerHandName = "Flush"
    else:
        if CheckStraight(cards) or ('A' in cards and 'K' in cards and 'Q' in cards and 'J' in cards and '10' in cards):
            pokerHandName = "Straight"
        else:
            pokerHandName = CheckOtherKinds(cards)
    
    return pokerHandName


def main():
    pokerHand1 = ["AH", "KH", "QH", "JH", "10H"]
    pokerHand2 = ["AC", "7H", "2H", "5H", "4H"]
    pokerHand3 = ["4H", "5H", "3H", "8H", "9H"]
    pokerHand4 = ["9H", "9C", "9D", "9S", "KH"]
    pokerHand5 = ["9H", "9C", "9D", "QS", "KH"]
    pokerHand6 = ["9H", "9C", "8D", "8S", "KH"]
    pokerHand7 = ["9H", "9C", "5D", "6S", "7H"]

    pokerHandName = PokerHandDetection(pokerHand2)
    print(pokerHandName)
    
if __name__ == "__main__":
    main()