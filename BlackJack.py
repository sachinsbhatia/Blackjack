import random

Card_faces = [ '2','3','4','5','6','7','8','9','10','J','Q','K','A']
Card_suits = [ 'Hearts','Spades','Diamonds','Clubs']
deck =[]
Cards_value = {'2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'10','J':'10','Q':'10','K':'10','A':'11'}
Player1_Cards =[]
Dealer_Cards =[]

def Deck_of_Cards():
    global Card_faces,Card_suits,deck
    for i in range(0, 13):
        for j in range(0, 4):
            cards = Card_faces[i] + ' of '+ Card_suits[j]
            deck.append(cards)
    random.shuffle(deck)

def Distribute():
    global Player1_Cards,Dealer_Cards,deck
    #poping the single card from the stack of cards
    Player1_Cards = [ deck.pop(0), deck.pop(0)]
    Dealer_Cards = [ deck.pop(0), deck.pop(0)]
    print ('Player 1 Cards are:', Player1_Cards)
    print ("Dealer's 1st Card is:",  Dealer_Cards[0])
    print ("Temporary score of Player 1 Hand is:", Total())  

def Will():    
    global Player1_Cards,deck
    while True:
        choice = input("Press H for 'Hit' and S for 'Stand': ").upper()   
        if choice == 'H':
            Player1_Cards.append(deck.pop(0))
            print ('Player 1 Cards are:', Player1_Cards)
            k = Total()
            if k <= 21:
                print ("Temporary score of Player 1 Hand is:", k)
            else:
                print("Player 1 is 'BUSTED' with the of score of",k ,"\nDealer WINS!" )
                return True
        else:
            print ('You Choose to stand ,So final Player 1 Cards are:', Player1_Cards)
            print ("and Final score of Player 1 Hand is:", Total())
            return False
    
def Total():
    global Player1_Cards,Cards_value
    sum=0
    for i in Player1_Cards:
        sum = sum + int(Cards_value[i.split()[0]])
    if sum > 21:
        for i in Player1_Cards:
            if i.split()[0] == 'A':
                sum = sum - 10
                if sum <= 21:
                    break
    return sum   

def Dealer():
    global Dealer_Cards,deck
    sum=0
    for i in Dealer_Cards:
        sum = sum + int(Cards_value[i.split()[0]])
    if sum > 21:
        for i in Dealer_Cards:
            if i.split()[0] == 'A':
                sum = sum - 10
                if sum <= 21:
                    break
    return sum

def DIFFICULTY():
    
    global Dealer_Cards,deck,Difficulty
    sum = Dealer()
    for i in range(0,3):
        if (Difficulty == 1):
            if sum < 16:
                Dealer_Cards.append(deck.pop(0))
        elif (Difficulty == 2):
            if sum < Total():
                Dealer_Cards.append(deck.pop(0))
        elif (Difficulty == 3):
            sum = random.randint(20,21)
        sum = Dealer()
    return sum

Deck_of_Cards()
print ("Deck of Card is prepared and well Shuffle.")
call = True
while call:
    Difficulty =  int(input("Choose Difficulty Level Between 1 to 3: "))
    Distribute()
    check = Will()
    if (check == False):
        dl = DIFFICULTY()
        if(dl > 21):
            print("Dealer is 'BUSTED' with the of score of",dl ,"\nPlayer 1 WINS!" )
        else:
            print ("Dealer score is", dl)
            if(Total()==dl):
                print (Dealer_Cards)
                print("DRAW")
            elif (Total()>dl):
                print (Dealer_Cards)
                print ("Player 1 WINS!")
            else:
                print (Dealer_Cards)
                print ("Dealer WINS!")
    call = input("Would you like to Play again, Y or N :").upper()
    if (call == "Y"):
        call = True
    else:
        call = False
        print ("Thank You for Playing")
