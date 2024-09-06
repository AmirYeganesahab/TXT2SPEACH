'''
Created on Feb 18, 2018

@author: geomatics
'''
import os
#os.system('echo {}|sudo -S sudo apt-get install python-pygame'.format('geomatics1985'))
#os.system('echo {}|sudo -S sudo apt-get install python3-pygame'.format('geomatics1985'))
import numpy as np
import webbrowser
#import new
import time, pygame
from gtts import gTTS

fAdress = '/home/geomatics/Dropbox/text2speech/words'
pygame.init()
fo = open(fAdress,'r')
lineNum=0
lastLine = 1
for line in fo:
    lineNum += 1
    if lineNum < lastLine-1: continue
    thisline = line.rstrip('\n')
    all = thisline.split('\t')
    
    try:
        word = gTTS(text=all[0], lang='en')
    except:
        word = gTTS(text='No word', lang='en')
    
    word.save("word.mp3")
    
    try:
        example = gTTS(text=all[1], lang='en')
    except:
        example = gTTS(text='No example sentence', lang='en')
    example.save("example.mp3")

    print(all[0])
    pygame.mixer.music.load('word.mp3')
    pygame.mixer.music.load('word.mp3')
    pygame.mixer.music.play()
    #os.system("mpg321 word.mp3")
    time.sleep(5)
    pygame.mixer.music.fadeout(5)
    
    
    print(all[1])
    #os.system("mpg321 example.mp3")
 
    pygame.mixer.music.load('example.mp3')
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.fadeout(5)
    
    print(lineNum)
    if int(lineNum/45.0) == lineNum/45.0:
        import subprocess, time
        browser = subprocess.Popen(['firefox', 'https://www.youtube.com/watch?v=qwtPuXSVNTY&t=3407s'])
        # browser now points to the instance of firefox I just opened
        time. sleep(480)
        browser.terminate()
