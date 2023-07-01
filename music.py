import winsound 
from  random import randint


def creat_music():
    count = 10
    while count>0:
        winsound.Beep(randint(50, 2000) , randint(1000 , 5000))
        count -= 1 
creat_music()



