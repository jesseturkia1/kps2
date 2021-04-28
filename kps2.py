# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 19:46:24 2021

@author: JesseTurkia
"""


import numpy as np
import sys
import random
import pickle
import pyautogui
from imgs import images
import os

alku = images.alku()
winning = images.winning()
losing = images.losing()

voittajat = {'Rock':'Scissors', 'Paper':'Rock', 'Scissors':'Paper'}


def voitto():
    return voitot >= 3 and (voitot - tappiot) > 1
def tappio():
    return tappiot >= 3 and (tappiot - voitot) > 1

def print_img():
    if kone == 'Scissors':
        print(images.scissors())
    elif kone == 'Paper':
        print(images.paper())
    elif kone == 'Rock':
        print(images.rock())
    

def pisteet(oma, kone):
    if voittajat[oma] == kone:
        global voitot
        voitot += 1
        print('\n\nPoint for you!!')
    elif voittajat[kone] == oma:
        global tappiot
        tappiot += 1
        print('\n\nDamn, computer got this one')
        
    print('\nWins: {}, Losses: {}'.format(voitot, tappiot))
    print_img()
    print("Machine chose {}".format(kone))
    
    if voitto():
        print('\n\n\nWell done!\nYou won!\nThe dogs can now return to their business.')
        print(winning)

    elif tappio():
        print('\n\n\nYou lost ;(\nThe dogs will never see their families again. Well done...')
        print(losing)



#%% Play


print(alku)
openinng_message = '\n\n**Welcome to play kps2!**\n\nParticipate in a perverted game of Rock-Paper-Scissors against a DOG KIDNAPPING psycopath\nto FREE THE PUPPIES!!!\n\nFirst give yourself a player nick\nThen type your selection "Rock", "Paper" or "Scissors"\n\nOne game is best of five with difference of 2\nGood luck!\n\nEnd game by typing "Exit"'
print(openinng_message)

voitot = 0
tappiot = 0

#Insert player name
player = pyautogui.prompt('Type your player name')
player = player[:12]
#Game commands are not accepted as player name
while player in ['Rock', 'Paper', 'Scissors', 'Exit', '']:
    if player == 'Exit':
        exit()
    error_text = '\n"{}" is not accepted player name\n                   Give a valid nick'.format(player)
    print(error_text)
    player = pyautogui.prompt(error_text)    

  
while not voitto() and not tappio():
    kone = random.choice(['Rock', 'Paper', 'Scissors'])
    #Player choice prompt
    valinta = pyautogui.prompt('Type your selection: Rock, Paper or Scissors') 
    if valinta in ['Rock', 'Paper', 'Scissors']:
        pisteet(valinta, kone)
    elif valinta == 'Exit':
        exit()
    else:
        print('\nEnter "Rock", "Paper" or "Scissors"\nSelections are case sensitive')



#Scoreboard
#haetaan scoreboard file jos löytyy
try:
    scoreboard = pickle.load( open( os.path.join('Gamefiles', 'scoreboard.pkl'), "rb" ) )
except:
      scoreboard ={}

#Tehdään player rivi, jos ensimmäinen, kerta, niin [0, 0, 0]
try:
    scoreboard_player = scoreboard[player]
except:
    scoreboard_player = [0, 0, 0, 0]


if voitto():
    voitot_log = scoreboard_player[0] + 1
    tappiot_log = scoreboard_player[1]

elif tappio():
    tappiot_log = scoreboard_player[1] + 1
    voitot_log = scoreboard_player[0]


log = [voitot_log, tappiot_log, voitot_log/(voitot_log+tappiot_log), voitot_log * (voitot_log/(voitot_log+tappiot_log))**2]

#scoreboard = log
scoreboard[player] = log

#Save updated scoreboard
pickle.dump(scoreboard, open (os.path.join('Gamefiles', 'scoreboard.pkl'), 'wb') )


#Printit
#Make scoreboard prints
#Current player scores
print('Your record is:\nPoints: {}, Victories: {}, Defeats: {}\n\n'.format( round( voitot_log * (voitot_log/(voitot_log+tappiot_log))**2, 2), voitot_log, tappiot_log ) )


#All time score
print('----All time scores----')
print('\n    Player        Points   (Victories - Defeats)')

#Järejestään socoreboard  
scoreboard_jarjestetty = {k: v for k, v in sorted(scoreboard.items(), key=lambda item: item[1][3], reverse=True)}
#Make iterators
itervals= iter(scoreboard_jarjestetty.values())
iterkeys = iter(scoreboard_jarjestetty.keys())
for i in range(min(9, len(scoreboard))):
    values = next(itervals)
    keys = next(iterkeys)

    print('{}.  {}:{}{} {}({} - {})'.format(i+1, keys, (13 - len(keys))  * ' ' , round(values[3], 2), (8 -len(str(round(values[3], 2))) ) * ' ' , values[0], values[1] ) )









