from enum import Enum

"""input = 32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

f = open("input_emi.txt","r")
input = f.read()

class Type(Enum):
    Five = 6
    Four = 5
    House = 4
    Three = 3
    TwoPair = 2
    OnePair = 1
    Card = 0

class Hand:
    def __init__(self, hand_string):
        self.bid = int(hand_string.split()[1])
        self.hand = Hand.get_hand(hand_string.split()[0])
        self.hand_type = Hand.get_hand_type(self.hand)

    def get_hand_type(hand_values):
        if PART2:
            joker = hand_values.count(1)
            counts = [hand_values.count(x) for x in set([x for x in hand_values if x != 1])]
            if joker >= 4: return Type.Five
        else:
            joker = 0
            counts = [hand_values.count(x) for x in set(hand_values)]

        counts.sort(reverse=True)
        most = lambda count: (counts[0]==count) | (counts[0]+joker==count)
        if most(5):
            return Type.Five
        if most(4):
            return Type.Four
        if most(3) & (counts[1]==2):
            return Type.House
        if most(3):
            return Type.Three
        if most(2) & (counts[1]==2):
            return Type.TwoPair
        if most(2):
            return Type.OnePair
        if most(1):
            return Type.Card
        
    def get_hand(hand_string):
        hand_string = hand_string.replace(""," ").strip()
        cs = ["T","J","Q","K","A"]
        for i,c in enumerate(cs):
            if PART2 & (c == "J"):
                hand_string = hand_string.replace(c,str(1))
            else:
                hand_string = hand_string.replace(c,str(i+10))
        return list(map(int,hand_string.split(" ")))
        
    def __lt__(self,other):
        if self.hand_type != other.hand_type:
            return self.hand_type.value < other.hand_type.value
        
        for c_this, c_other in zip(self.hand,other.hand):
            if c_this != c_other:
                return c_this < c_other
        raise Exception("SameHandException")
    
    def __repr__(self):
        return f"Type: {self.hand_type}, Hand: {self.hand}, Bid: {self.bid}\n"

#Part 1
PART2 = False
hands = [Hand(line) for line in input.splitlines()]
hands.sort()
res = sum([(place+1)*hand.bid for place,hand in enumerate(hands)])
print("Final sum part1:",res)

#Part 2
PART2 = True
hands = [Hand(line) for line in input.splitlines()]
hands.sort()
res = sum([(place+1)*hand.bid for place,hand in enumerate(hands)])
print("Final sum part2:",res)
