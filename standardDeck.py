import itertools
import random
import math

def createDeck():
    """
    This creates a single list containing tuples which have the values
    (suit, numerical value)
    """
    deck = []
    suits = ['Heart', 'Diamond', 'Spade', 'Club']
    numbers = [i for i in range(1, 14)]
    for c in itertools.product(suits,numbers):
        deck.append(c)
    random.shuffle(deck)
    return deck

def dealHand(deck):
    """
    draws 5 cards and modifies the deck.
    I was told to instead use indexing to draw, instead of modifying the list
    """
    hand = [] 
    for i in range(5): 
        hand.append(deck.pop())
    return hand
def isStraight(hand):
    """
    takes in an ordered input
    determines if the hand is a type of straight
    """
    if hand == [1, 10, 11, 12, 13]:
        return True
    if hand[0] + 1 == hand[1] and hand[1] + 1 == hand[2]\
       and hand[2] + 1 == hand[3] and hand[3] + 1 == hand[4]:
        return True
    else:
        return False
#This evalHand function currently returns only the value of said hand
#E.G.: "Full House", "Straight", ... but perhaps it should also return
#orderedVals and valuesDict in order to function in my whoWins()

def evalHand(hand):
    """
    first take the hand and create two seperate lists,
    one containing all the suits and one containing all
    of the values. 
    """
    suits = []
    orderedVals = []
    valuesDict = {}
    for index in hand:
        suits.append(index[0])
    for index in hand:
        orderedVals.append(index[1])
    orderedVals.sort()
    """
    The following for loop counts the instances of said value
    """
    for theSuit, theNumericalValue in hand:
        if theNumericalValue not in valuesDict:
            valuesDict[theNumericalValue] = 1
        else:
            valuesDict[theNumericalValue] += 1
    """
    Now I start running checks on the hands themselves.
    First, I'll take care of all the cases in which the hand
    returns a flush
    """
    if len(set(suits)) == 1:
        if orderedVals == [1, 10, 11, 12, 13]:
            return "Royal Flush"
        elif isStraight(orderedVals):
            return "Straight Flush"
        else:
            return "Flush"
    """
    If there are two different kinds of numbers in any given
    five card hand, then the hand must either be a four of a kind
    or a full house.
    """
    if len(set(orderedVals)) == 2:
        for key in valuesDict:
            if valuesDict[key] == 4 or valuesDict[key] == 1:
                return "Four Of A Kind"
            elif valuesDict[key] == 3 or valuesDict[key] == 2:
                return "Full House"
    """
    If there are three different kinds of numbers in any given
    five card hand, then the hand must either be a three of a kind
    or two pair.
    """
    if len(set(orderedVals)) == 3:
        for key in valuesDict:
            if ([key] == 3 or valuesDict[key] == 1) and not valuesDict[key] == 2:
                return "Three Of A Kind"
            elif valuesDict[key] == 2 or valuesDict[key] == 1:
                return "Two Pair"
    """
    If there are four different kinds of numbers in any given
    five card hand, then the hand must be a pair.
    """
    if len(set(orderedVals)) == 4:
        return "One Pair"
    """
    If there are five different kinds of numbers
    then the hand must be whatever high or a straight
    """
    if len(set(orderedVals)) == 5:
        if isStraight(orderedVals):
            return "Straight"
        if not isStraight(orderedVals):
            return "High Card"


#Okay, so my whoWins function uses a lot of repetition. I feel like I should
#have at the very least had it return True or False instead of all this text
#and have a main() function that deals with the printing seperately.
    
def whoWins(firsthand, secondhand):
    hand1 = evalHand(firsthand)
    hand2 = evalHand(secondhand)
    orderedHand1 = []
    orderedHand2 = []
    valuesDict1 = {}
    valuesDict2 = {}
    for index in firsthand:
        orderedHand1.append(index[1])
    for index in secondhand:
        orderedHand2.append(index[1])
    orderedHand1 = orderedHand1.sort()
    orderedHand2 = orderedHand2.sort()
    for theSuit, theNumericalValue in firsthand:
        if theNumericalValue not in valuesDict:
            valuesDict1[theNumericalValue] = 1
        else:
            valuesDict1[theNumericalValue] += 1
    for theSuit, theNumericalValue in secondhand:
        if theNumericalValue not in valuesDict:
            valuesDict2[theNumericalValue] = 1
        else:
            valuesDict2[theNumericalValue] += 1
        
    handRank = {
        'Royal Flush': 9,
        'Straight Flush': 8,
        'Four Of A Kind': 7,
        'Full House': 6,
        'Flush': 5,
        'Straight': 4,
        'Three Of A Kind': 3,
        'Two Pair': 2,
        'One Pair': 1,
        'High Card': 0
        }
    """
    The cases in which the hands evaluate to different types of hands:
    """
    if handRank[hand1] > handRank[hand2]:
        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
    elif handRank[hand1] < handRank[hand2]:
        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)

    #We test to see if the hand rankings are the same. If they are, then make checks
    
    elif handRank[hand1] == handRank[hand2]:
        if hand1 == 'Royal Flush':
            return "The result is a tie!"
        if hand1 == 'Straight Flush':
            #first check to see if its the same values
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #check the highest value
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
        if hand1 == 'Four Of A Kind':
            #first check to see if its the same values
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #if the four of a kind set is the same, then check for the high card
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[0] > orderedHand2[0]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[0] < orderedHand2[0]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            #if the four of a kind set is not the same, then the higher set wins
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' + str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            
        if hand1 == 'Full House':
            #I can use the same checks used in 'Four Of A Kind'
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #if the three set is the same, then check for the high pair
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[0] > orderedHand2[0]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[0] < orderedHand2[0]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            #if the three set is not the same, then the higher set wins
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' + str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            
        if hand1 == 'Flush':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #continue checking for high card and if equal keep checking the lower card
            #surely this can be made simpler... perhaps using recursion?
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[3] > orderedHand2[3]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[3] < orderedHand2[3]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[3] == orderedHand2[3]:
                    if orderedHand1[2] > orderedHand2[2]:
                        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[2] < orderedHand2[2]:
                        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[2] == orderedHand2[2]:
                        if orderedHand1[1] > orderedHand2[1]:
                            return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                        if orderedHand1[1] < orderedHand2[1]:
                            return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                        if orderedHand1[1] == orderedHand2[1]:
                            if orderedHand1[0] > orderedHand2[0]:
                                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                            if orderedHand1[0] < orderedHand2[0]:
                                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                            


        if hand1 == 'Straight':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #This special case is for the ace high straight. Ace high straights autowin versus non ace high straights
            if orderedHand1 == [1, 10, 11, 12, 13] and orderedhand2 != [1, 10, 11, 12, 13]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1 != [1, 10, 11, 12, 13] and orderedhand2 == [1, 10, 11, 12, 13]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                    
        if hand1 == 'Three Of A Kind':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #A similar check to Full House and Four Of A Kind, with checks on the single cards similar to straight.
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[1] == orderedHand2[1]:
                    if orderedHand1[0] > orderedHand2[0]:
                        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[0] < orderedHand2[0]:
                        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[1] > orderedHand2[1]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' + str(secondhand)
                if orderedHand1[1] < orderedHand2[1]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] > orderedHand2[4]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
           
        if hand1 == 'Two Pair':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #A similar check to Full House and Four Of A Kind, with checks on the single cards similar to straight.
            #I can pretty much use the same exact code I did with three of a kind as I have first done a
            #check on the type of hand, and the hand is ordered
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[1] == orderedHand2[1]:
                    if orderedHand1[0] > orderedHand2[0]:
                        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[0] < orderedHand2[0]:
                        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[1] > orderedHand2[1]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' + str(secondhand)
                if orderedHand1[1] < orderedHand2[1]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] > orderedHand2[4]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
        if hand1 == 'One Pair':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #continue checking for high card and if equal keep checking the lower card
            #surely this can be made simpler... perhaps using recursion?
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[2] > orderedHand2[2]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[2] < orderedHand2[2]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[2] == orderedHand2[2]:
                    if orderedHand1[1] > orderedHand2[1]:
                        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[1] < orderedHand2[1]:
                        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[1] == orderedHand2[1]:
                        if orderedHand1[0] > orderedHand2[0]:
                            return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                        if orderedHand1[0] < orderedHand2[0]:
                            return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                        

        if hand1 == 'High Card':
            if orderedHand1 == orderedHand2:
                return "The result is a tie!"
            #continue checking for high card and if equal keep checking the lower card
            #surely this can be made simpler... perhaps using recursion?
            if orderedHand1[4] > orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] < orderedHand2[4]:
                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
            if orderedHand1[4] == orderedHand2[4]:
                if orderedHand1[3] > orderedHand2[3]:
                    return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[3] < orderedHand2[3]:
                    return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                if orderedHand1[3] == orderedHand2[3]:
                    if orderedHand1[2] > orderedHand2[2]:
                        return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[2] < orderedHand2[2]:
                        return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                    if orderedHand1[2] == orderedHand2[2]:
                        if orderedHand1[1] > orderedHand2[1]:
                            return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                        if orderedHand1[1] < orderedHand2[1]:
                            return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                        if orderedHand1[1] == orderedHand2[1]:
                            if orderedHand1[0] > orderedHand2[0]:
                                return str(hand1) + ', ' + str(firsthand) + " beats " + str(hand2) +', ' +str(secondhand)
                            if orderedHand1[0] < orderedHand2[0]:
                                return str(hand1) + ', ' + str(firsthand) + " loses to " + str(hand2) +', ' +str(secondhand)
                            

            
 
theDeck = createDeck()
theHand = dealHand(theDeck)
royalFlush = [('Club', 1), ('Club', 10), ('Club', 11), ('Club', 12), ('Club', 13)]
straightFlush = [('Club', 9), ('Club', 10), ('Club', 11), ('Club', 12), ('Club', 13)]
aFlush = [('Club', 1), ('Club', 3), ('Club', 11), ('Club', 12), ('Club', 13)]
fourOfAKind = [('Club', 4), ('Heart', 4), ('Diamond', 4), ('Spade', 4), ('Club', 13)]
fullHouse = [('Club', 4), ('Heart', 4), ('Diamond', 4), ('Spade', 13), ('Club', 13)]
aStraight = [('Club', 2), ('Club', 3), ('Club', 4), ('Club', 5), ('Diamond', 6)]
threeOfAKind = [('Club', 4), ('Heart', 4), ('Diamond', 4), ('Spade', 2), ('Club', 13)]
twoPair = [('Club', 4), ('Heart', 4), ('Diamond', 5), ('Spade', 5), ('Club', 13)]
aPair = [('Club', 4), ('Heart', 4), ('Diamond', 5), ('Spade', 6), ('Club', 13)]
highCard = [('Club', 4), ('Heart', 1), ('Diamond', 5), ('Spade', 6), ('Club', 13)]
