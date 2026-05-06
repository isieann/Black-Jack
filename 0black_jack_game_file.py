
############################################################
#                        BLACK JACK                       #
############################################################

import pygame
import random
import sys
import cardClass as card
import playerClass as player
import buttonClass as button

pygame.init()
wn = pygame.display.set_mode((1000,600))
pygame.display.set_caption("Black Jack")
clock = pygame.time.Clock()

deck = []

hands = [] 

dealing = False
playing = False
done = False

eventCt = 0

hit = button.Button(550,400,'hit.png','hit_down.png')
hitDisplay = hit.file
stay = button.Button(780,400,'stay.png','stay_down.png')
stayDisplay = stay.file

play = button.Button(400,250,'play.png','play_down.png')
playDisplay = play.file

dealerWin = pygame.Rect((50,50),(100,50))
playerWin = pygame.Rect((50,100),(100,50))

quitt = button.Button(225,200,'quit.png','quit_down.png')
quitDisplay = quitt.file
cont = button.Button(15,200,'cont.png','cont_down.png')
contDisplay = cont.file

display = "na"
dislayDealer = "na"
th = False
ch = False
dealerOnly = False

winnerVal = 0
winner = 'na'

reset = True

############################################################
#                      GAME WHILE LOOP                     #
############################################################

while True:
    eventCt += 1
    x,y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:

            if (x > hit.x) and (x < (hit.x+200)) and (y > hit.y) and (y < (hit.y+100)) and playing:
                hitDisplay = hit.downFile
                dealing = True

            if (x > stay.x) and (x < (stay.x+200)) and (y > hit.y) and (y < (hit.y+100)) and playing:
                stayDisplay = stay.downFile
                dealerOnly = True

            if (x > play.x) and (x < (play.x+200)) and (y > play.y) and (y < (play.y+100)) and not playing:
                playDisplay = play.downFile

            if (x > cont.x) and (x < (cont.x+200)) and (y > cont.y) and (y < (cont.y+100)) and done:
                contDisplay = cont.downFile

            if (x > quitt.x) and (x < (quitt.x+200)) and (y > quitt.y) and (y < (quitt.y+100)) and done:
                pygame.quit()
                sys.exit()

        elif event.type == pygame.MOUSEBUTTONUP:

            if (x > hit.x) and (x < (hit.x+200)) and (y > hit.y) and (y < (hit.y+100)) and playing:
                hitDisplay = hit.file     

            if (x > stay.x) and (x < (stay.x+200)) and (y > hit.y) and (y < (hit.y+100)) and playing:
                stayDisplay = stay.file
                
            if (x > play.x) and (x < (play.x+200)) and (y > play.y) and (y < (play.y+100)) and not playing:
                playDisplay = play.file
                playing = True
                dealing = True

            if (x > cont.x) and (x < (cont.x+200)) and (y > cont.y) and (y < (cont.y+100)) and done:
                contDisplay = cont.file
                reset = True
            

############################################################
#                        -->DEAL<--                       #
############################################################

    def deal():
        return deck.pop(0)

############################################################
#                  -->UPDATE HAND VALUE<--                 #
############################################################

    def update_hand_value(hand,dealt):
        hand.hand.append(dealt)
        if not dealt.card.startswith('Ace'):
            hand.handVal += int(dealt.val)
        elif hand.handVal > 10:
            hand.handVal += int(dealt.val) 
        else: 
            hand.handVal += 11

    if reset:
        eventCt = 0
        display = "na"
        displayDealer = "na"
        th = False
        ch = False
        dealerOnly = False

        winnerVal = 0
        winner = 'na'

        dealing = False
        playing = False
        done = False

        cardFiles = ['ace_of_spades.png','king_of_spades.png','queen_of_spades.png','jack_of_spades.png','two_of_spades.png','three_of_spades.png',
                'four_of_spades.png','five_of_spades.png','six_of_spades.png','seven_of_spades.png','eight_of_spades.png','nine_of_spades.png','ten_of_spades.png',
                'ace_of_hearts.png','king_of_hearts.png','queen_of_hearts.png','jack_of_hearts.png','two_of_hearts.png','three_of_hearts.png',
                'four_of_hearts.png','five_of_hearts.png','six_of_hearts.png','seven_of_hearts.png','eight_of_hearts.png','nine_of_hearts.png','ten_of_hearts.png',
                'ace_of_clubs.png','king_of_clubs.png','queen_of_clubs.png','jack_of_clubs.png','two_of_clubs.png','three_of_clubs.png',
                'four_of_clubs.png','five_of_clubs.png','six_of_clubs.png','seven_of_clubs.png','eight_of_clubs.png','nine_of_clubs.png','ten_of_clubs.png',
                'ace_of_diamonds.png','king_of_diamonds.png','queen_of_diamonds.png','jack_of_diamonds.png','two_of_diamonds.png','three_of_diamonds.png',
                'four_of_diamonds.png','five_of_diamonds.png','six_of_diamonds.png','seven_of_diamonds.png','eight_of_diamonds.png','nine_of_diamonds.png','ten_of_diamonds.png']

        deck = []
        suits = ['Spades','Hearts','Clubs','Diamonds']
        special_values = {'Ace':1, 'King':10, 'Queen':10, 'Jack':10}
        numbers = ['Ace', 'King', 'Queen', 'Jack']
        for i in range(2,11):
            numbers.append(str(i))
        for suit in suits:
            for num in numbers:
                if num.isnumeric(): 
                    c = card.Card(num,suit,num)
                else:
                    c = card.Card(num,suit,special_values[num])
                deck.append(c)
            
        for paper in deck:
            spot = deck.index(paper)  
            paper.file = cardFiles[spot]

        random.shuffle(deck)

        hands = [] 
        player1 = player.Player()
        hands.append(player1)
        dealer = player.Dealer()
        hands.append(dealer)

        reset = False

    wn.fill("white")
    wn.blit(pygame.image.load('bg2.png'),(0,0))
    if playing:
        wn.blit(pygame.image.load('bg1.png'),(0,0))

   

############################################################
#                        NOT PLAYING                       #
############################################################

    if not playing:
        wn.blit(pygame.image.load(play.file),(play.x,play.y))

############################################################
#                          PLAYING                         #
############################################################

    if playing:
        
        wn.blit((pygame.image.load('button_block.png').convert_alpha()),
                                            (500,380))
        wn.blit((pygame.image.load(hitDisplay).convert_alpha()),
                                            (hit.x, hit.y))
        wn.blit((pygame.image.load(stayDisplay).convert_alpha()),
                                            (stay.x, stay.y))
        
        if player1.hand != []:
            th = False
            for paper in player1.hand:
                paper.cor((10 + player1.hand.index(paper)*50))
            
            for paper in player1.hand:
                    if (x > paper.x) and (x < (paper.x+50)) and (y > paper.y) and (y < (paper.y+300)):
                        paper.y = 360
                        display = paper
                        th = True
                    else:
                        paper.y = 380         
                
            if th:
                for paper in player1.hand:
                    if paper != display:
                        pap = wn.blit((pygame.image.load(paper.file).convert_alpha()),
                                            (paper.x, paper.y))
                
                pap = wn.blit((pygame.image.load(display.file).convert_alpha()),
                                            (display.x, display.y))
                    
            else:
                for paper in player1.hand:
                    pap = wn.blit((pygame.image.load(paper.file).convert_alpha()),
                                        (paper.x, paper.y))
            
            ch = False
            for paper in dealer.hand:
                paper.y = 50
                paper.cor((500  + dealer.hand.index(paper)*50))

            for paper in dealer.hand:
                    if (x > paper.x) and (x < (paper.x+50)) and (y > paper.y) and (y < (paper.y+300)):
                        paper.y = 30
                        dislayDealer = paper
                        ch = True
                    else:
                        paper.y = 50

            if ch:
                for paper in dealer.hand:
                    if paper != dislayDealer:
                        if dealer.hand.index(paper) == 0 or done:
                            pap = wn.blit((pygame.image.load(paper.file).convert_alpha()),
                                        (paper.x, paper.y))
                        else:
                            pap = wn.blit((pygame.image.load(paper.back).convert_alpha()),
                                        (paper.x, paper.y))
                    
                if dealer.hand.index(dislayDealer) == 0 or done:
                    pap = wn.blit((pygame.image.load(dislayDealer.file).convert_alpha()),
                                (dislayDealer.x, dislayDealer.y))
                else:
                    pap = wn.blit((pygame.image.load(dislayDealer.back).convert_alpha()),
                                (dislayDealer.x, dislayDealer.y))
            else:
                for paper in dealer.hand:
                    if dealer.hand.index(paper) == 0 or done:
                            pap = wn.blit((pygame.image.load(paper.file).convert_alpha()),
                                        (paper.x, paper.y))
                    else:
                            pap = wn.blit((pygame.image.load(paper.back).convert_alpha()),
                                        (paper.x, paper.y))
                    
            if dealerOnly and not done and (eventCt%100 == 0):
                toDealorNotToDeal = dealer.hit()
                if toDealorNotToDeal:
                    dealt = deal()
                    update_hand_value(dealer, dealt)
                    done = dealer.check()
                else:
                    done = True


############################################################
#                      DEALING                             #
############################################################

        if dealing:
            if player1.hand == []:
                for x in range(2):
                    for hand in hands:
                        dealt = deal()
                        update_hand_value(hand, dealt)
                done = player1.check()
                if not done:
                    done = dealer.check()
            else:
                if not done:
                    dealt = deal()
                    update_hand_value(player1, dealt)
                    done = player1.check()

            dealing = False
        
        if done:
            if (dealer.handVal < 22) and (dealer.handVal == player1.handVal):
                winner = dealer
            if winner == 'na':
                for hand in hands:
                    if (hand.handVal < 22) and (hand.handVal > winnerVal):
                        winner = hand
                        winnerVal = hand.handVal
            if winner == dealer:
                wn.blit(pygame.image.load('you_lose.png'), (15,50))
            else:
                wn.blit(pygame.image.load('you_win.png'), (15,50))
        
        
            wn.blit(pygame.image.load(quitt.file),(quitt.x,quitt.y))
            wn.blit(pygame.image.load(cont.file),(cont.x,cont.y))

            
    pygame.display.flip()
    clock.tick(60)
    
