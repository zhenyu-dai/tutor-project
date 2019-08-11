# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 18:50:21 2019

@author: daizh
庄家要牌规则：
如果庄家点数小于17，必学要牌
如果庄家点数大于等于17，则停止要牌

Push 表示平局

"""

import random

class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

class numCard(Card):
    def __init__(self,rank,suit):
        super().__init__(rank,suit)
        self.hard = self.soft = self.rank

class aceCard(Card):
    def __init__(self,rank,suit):
        super().__init__('A',suit)
        self.hard = 1
        self.soft = 11

class faceCard(Card):
    def __init__(self,rank,suit):
        super().__init__( rank , suit )
        self.hard = self.soft = 10

# somecard = [numCard('2','club'),aceCard('A','diamond'),faceCard('J','spade')]
# for i in somecard:
#     print( i.rank,i.suit,i.hard,i.soft)

"""
   --------------------------------------------- 第二部分：生成多副牌----------------------------------------------------
    一个名为Decks的列表，其元素为一张张牌
"""
def card4( rank, suit ):
    class_= {1: aceCard, 11: faceCard, 12: faceCard,13: faceCard}.get(rank, numCard)
    return class_( rank, suit )

class Decks(list):
    def __init__(self,num):
        super().__init__()
        for i in range(num):
            self.extend( card4(rank,suit) for rank in range(1,14) for suit in ['Club','Heart','Diamond','Spade'] )
        random.shuffle(self)

decks = Decks(3) #生成3副牌

"""
    -----------------------------------------------第三部分：手牌--------------------------------------------------------
"""
class Hand:
    dieFlag = False
    
    def __init__(self,*mycards):
        self.mycards = []
        self.mycards.extend(mycards)
        print('your beginning cards are: ',mycards[0].suit,mycards[0].rank,mycards[1].suit,mycards[1].rank)
        print('sum of your cards is:',self.count())

    def askcard(self,acard):
        nowpoint = self.count()
        if Hand.dieFlag:
            print('sum of your card is ',nowpoint,'you died')
        else:
            print('you get card:',acard.suit,acard.rank)
            self.mycards.append(acard)
            nowpoint = self.count()
            print('sum of your card is ',nowpoint)

    def count(self):
        sumpoint = sum( c.hard for c in self.mycards)
        if sumpoint < 21:
            sumpoint = sum( c.soft for c in self.mycards)
            if sumpoint > 21:
                sumpoint = sum( c.hard for c in self.mycards)
        elif sumpoint > 21:
            Hand.dieFlag = True
        return sumpoint

class DHand:
    dieFlag = False
    def __init__(self,*Dcards):
        self.Dcards = []
        self.Dcards.extend(Dcards)
        print('dealer beginning cards are: ',Dcards[0].suit,Dcards[0].rank,Dcards[1].suit,Dcards[1].rank)
        print('sum of dealer cards is:',self.count())

    def askcard(self,acard):
        nowpoint = self.count()
        if DHand.dieFlag:
            print('sum of dealer card is ',nowpoint,'you win')
        else:
            print('dealer get card:',acard.suit,acard.rank)
            self.Dcards.append(acard)
            nowpoint = self.count()
            print('sum of dealer card is ',nowpoint)

    def count(self):
        sumpoint = sum( c.hard for c in self.Dcards)
        if sumpoint < 21:
            sumpoint = sum( c.soft for c in self.Dcards)
            if sumpoint > 21:
                sumpoint = sum( c.hard for c in self.Dcards)
        elif sumpoint > 21:
            Hand.dieFlag = True
        return sumpoint

if __name__=="__main__":
    hands = Hand(decks.pop(),decks.pop())                #你的手牌
    dealer_hands = DHand(decks.pop(),decks.pop())        #荷官手牌
    while hands.dieFlag + dealer_hands.dieFlag != 1:
        if hands.count()==21 & dealer_hands.count()==21:
            print ('Push!')
            break
        if hands.count()==21:
            print ('finally,your get %d points. You Win!'%hands.count())
            break
        if dealer_hands.count()==21:
            print ('finally,your get %d points. You Lose!'%hands.count())
            break
        wt2askc = input('ask card?<y/n>: ')
        if wt2askc == 'y' and not hands.dieFlag:
                hands.askcard(decks.pop())
                if hands.count()>21:
                    print ('finally,your get %d points. You Lose!'%hands.count())
                   
                    break
                if hands.count()==21:
                    print ('finally,your get %d points. You Win!'%hands.count())
                    break
                if dealer_hands.count()>= 17:
                    continue
                else:
                    dealer_hands.askcard(decks.pop())
                    if dealer_hands.count()>21:
                        print ('finally,your get %d points. You Win!'%hands.count())
                        break
                    if dealer_hands.count()==21:
                        print ('finally,your get %d points. You Lose!'%hands.count())
                        break
        else:
            if dealer_hands.count() < 17:
                dealer_hands.askcard(decks.pop())
                if dealer_hands.count()>21:
                    print ('finally,your get %d points. You Win!'%hands.count())
                    break
                elif dealer_hands.count()<21:
                    continue
                else:
                    print ('finally,your get %d points. You Lose!'%hands.count())
                    break
            else:
                if dealer_hands.count()>21:
                    print ('finally,your get %d points. You Win!'%hands.count())
                    break
                if dealer_hands.count()==21:
                    print ('finally,your get %d points. You Lose!'%hands.count())
                    break
               
                if dealer_hands.count()>hands.count():
                    print ('finally,your get %d points. You Lose!'%hands.count())
                    break
                elif dealer_hands.count()<hands.count():
                    print ('finally,your get %d points. You Win!'%hands.count())
                    break
                else:
                    print ('Push!')   #平局
                    break