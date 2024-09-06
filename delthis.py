'''
Created on Feb 18, 2018

@author: geomatics
'''


import subprocess, time
browser = subprocess.Popen(['firefox', 'https://www.youtube.com/watch?v=C7ogubcmF4Y'])
# browser now points to the instance of firefox I just opened
time. sleep(10)
browser.terminate()


