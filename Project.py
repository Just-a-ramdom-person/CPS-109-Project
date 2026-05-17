#Poker Game

import random

def start_game():
    
    cardn = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    cardh = ["Diamond","Heart","Spade","Club"]
    deckn = []
    hands = ["High_Card","One_Pair","Two_Pair","Three_of_a_Kind","Straight","Flush","Full_House,","Four_of_a_Kind","Straight_Flush","Royal_Flush"]
    bits = 1000
    
    pcard = []
    for i in range(4):
        for j in range(13):
            deckn.append([cardn[j],cardh[i]])
    
    def suffle_deck(deck):
        temp1 = []
        temp2 = deck
        for i in range(52):
            rand = random.randint(0,51-i)
            temp1.append(temp2[rand])
            deck.pop(rand)
        return temp1
    
    deckS = suffle_deck(deckn.copy())

    player_hand = []
    computer_hand = []

    for i in range(2):
        player_hand.append(deckS[0])
        computer_hand.append(deckS[1])
        deckS.pop(0)
        deckS.pop(0)
    

    def get_handtype(list1,com_card,nums):
        combine = list1 + com_card
        num_combine = []
        house_combine = []
        for i in range(len(combine)):
            num_combine.append(combine[i][0])
            house_combine.append(combine[i][1])
        if (('A'and'K'and'Q'and'J'and'10') in num_combine): # Royal Flush
            newcardlist1 = []
            newcardlist2 = []
            for j in range(len(num_combine)):
                if num_combine[j] in ['A','K','Q','J','10']:
                    newcardlist1.append(num_combine[j])
                    newcardlist2.append(house_combine[j])
            
            if ((newcardlist2.count('Diamond') == 5) or (newcardlist2.count('Heart') == 5) or (newcardlist2.count('Spade') == 5) or (newcardlist2.count('Club')== 5)):
                return "Royal_Flush"
        
        

        
        def check_straight(listi):
            newcardlist3 = []
            for i in range(len(listi)):
                newcardlist3.append(nums.index(listi[i]))
                newcardlist3.sort()
                newcardlist3 = set(newcardlist3)
                newcardlist3 = list(newcardlist3)

            count = 1
            max = 0
            for i in range(len(newcardlist3)-1):
                if newcardlist3[i+1] - newcardlist3[i] == 1:
                    count += 1
                    max = count
                else:
                    count = 1
            if max >= 5 or ((9 in newcardlist3) and (10 in newcardlist3) and (11 in newcardlist3) and (12 in newcardlist3) and (0 in newcardlist3)):
                return True


        if ((house_combine.count('Diamond') >= 5) or (house_combine.count('Heart')>= 5) or (house_combine.count('Spade')>= 5) or (house_combine.count('Club')>= 5)):
            newcardlist4 = []
            if (house_combine.count('Diamond')) >= 5:
                for i in range(len(num_combine)):
                    if house_combine[i] == 'Diamond':
                        newcardlist4.append(num_combine[i])
                if check_straight(newcardlist4):
                    return "Straight_Flush"
                else:
                    return "Flush"
            elif (house_combine.count('Heart')) >= 5:
                for i in range(len(num_combine)):
                    if house_combine[i] == 'Heart':
                        newcardlist4.append(num_combine[i])
                if check_straight(newcardlist4):
                    return "Straight_Flush"
                else:
                    return "Flush"
            if (house_combine.count('Spade')) >= 5:
                for i in range(len(num_combine)):
                    if house_combine[i] == 'Spade':
                        newcardlist4.append(num_combine[i])
                if check_straight(newcardlist4):
                    return "Straight_Flush"
                else:
                    return "Flush"
            if (house_combine.count('Club')) >= 5:
                for i in range(len(num_combine)):
                    if house_combine[i] == 'Club':
                        newcardlist4.append(num_combine[i])
                if check_straight(newcardlist4):
                    return "Straight_Flush"
                else:
                    return "Flush"
        else:
            if check_straight(num_combine):
                return "Straight"

        newlist = set(num_combine)
        newlist = list(newlist)
        newlist2 = []
        for i in range(len(newlist)):
            newlist2.append(num_combine.count(newlist[i]))

        if 4 in newlist2:
            return "Four_of_a_Kind"
        elif 3 in newlist2 and 2 in newlist2:
            return "Full_House"
        elif 3 in newlist2:
            return "Three_of_a_Kind"
        elif newlist2.count(2) >= 2:
            return "Two_Pair"
        elif 2 in newlist2:
            return "One_Pair"
        else:
            return "High Card"
    
    community_cards = deckS[0:5]

    def g1():
        playing = True
        while playing == True:
            turn = 0
            if turn == 0:
                print("---------------------------------------------------------------------------------------")
                print("Gamemode: RANDOM [The rankings of the poker hands is random :) ]")
                print(f"PLayer Hand: {player_hand}")
                choice = 0
                comp_bet = 0
                check = 0
                pall_in = 0
                while choice < 1 or choice > 4:
                    try:
                        print("[1:Raise], [2:Call], [3:Check], [4:Fold]")
                        choice = int(input("What would you like to do: "))
                    except:
                        pass
                if comp_bet == 0 and choice == 2:
                    while (choice < 1 or choice > 4) or choice == 2:
                        try:
                            print("[1:Raise], [2:Call], [3:Check], [4:Fold]")
                            choice = int(input("What would you like to do: "))
                        except:
                            pass
                if choice == 1:
                    bet = 0
                    while bet == 0:
                        try:
                            print(f"You have {bits} bits left!")
                            bet = int(input("How much would you like to bet: "))
                        except:
                            pass
                    if bet == bits:
                        print("ALL IN !!!!")
                elif choice == 2:
                    bet = comp_bet
                    print("You have matched the computer's bet.")
                elif choice == 3:
                    check += 1
                else:
                    print("Bye!!! Have a great time!!")
                    break
                turn += 1

            if turn == 1:
                if choice == 1:
                    print("Computer Calls")
                    comp_bet = bet
                elif choice == 2:
                    pass
                


    
    def g2():
        pass

    def g3():
        pass

    def g4():
        pass

    def g5():
        pass


    def select_gamemode():
        print("Gamemodes: [1:Random] [2:Easy] [3: Hard] [4:New :)] [5: Reverse]")
        try: 
            gamemode = int(input("Choose your gamemode: "))
        except:
            while type(gamemode) != int or gamemode < 1 or gamemode > 5:
                print("Gamemodes: [1:Random] [2:Easy] [3: Hard] [4:New :)] [5: Reverse]")
                gamemode = int(input("Choose your gamemode: "))
        while type(gamemode) != int or gamemode < 1 or gamemode > 5:
                print("Gamemodes: [1:Random] [2:Easy] [3: Hard] [4:New :)] [5: Reverse]")
                print("Type the number")
                gamemode = int(input("Choose your gamemode: "))

        if gamemode == 1:
            g1()
        elif gamemode == 2:
            g2()
        elif gamemode == 3:
            g3()
        elif gamemode == 4:
            g4()
        elif gamemode == 5:
            g5()
            
        


    select_gamemode()


start_game()



