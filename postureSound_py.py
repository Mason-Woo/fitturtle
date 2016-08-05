import os,sys
import time

PATH = 'C:/Users/Keen/Documents/SkeletonBasics-D2D/'

def playWav(sound):
    os.system("start " + PATH + sound)


while True:

    f = open(sys.argv[1],'r')
    s = f.read()
    print(s)
    
    if s[0] == '0':       
        playWav('badPosture.wav')
    elif s[0] == '1':
        playWav('goodPosture.wav')
    # else:
    #     assert(False and "Error !!!")
    
    time.sleep(5)
