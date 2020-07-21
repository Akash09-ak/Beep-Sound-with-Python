'''This program plays different songs by choosing no. b/w 1-10
   You can add different songs and their path'''
from pygame import mixer         # import mixer class from pygame package
n=int(input("Choose any no. b/w 1-10 \n"))
file=""                                          #empty string
if(n==1):
    file="F:\Mixed songs\Luh_Kel_-_Wrong_(Lyrics)(128k).mp3"              # create a file with path and name of music file same goes for other nine songs          
    mixer.init()
elif(n==2):
    file="F:\Mixed songs\Hosanna.mp3"
    mixer.init()
elif(n==3):
    file="F:\Mixed songs\Jiyen kyun.mp3"
    mixer.init()
elif(n==4):
    file="F:\Mixed songs\Justin_Bieber_-_Baby_(Acoustic_Cover_by_Jonah_Baker)(256kbps).mp3"
    mixer.init()
elif(n==5):
    file="F:\Mixed songs\Marshmello_ft._Bastille_-_Happier_(Official_Lyric_Video).mp3"
    mixer.init()
elif(n==6):
    file="F:\Mixed songs\Maroon_5_-_Memories_(Lyrics)(256k).mp3"
    mixer.init()
elif(n==7):
    file="F:\Mixed songs\See You Again feat Charlie P.mp3"
    mixer.init()
elif(n==8):
    file="F:\Mixed songs\Tera Yaar Hoon Main.mp3"
    mixer.init()
elif(n==9):
    file="F:\Mixed songs\Tera_Fitoor_Song_Video_-_Genius___Utkarsh_Sharma,_Ishita_Chauhan___Arijit_Singh_.mp3"
    mixer.init()
elif(n==10):
    file="F:\Mixed songs\Tere Jaisa Yaar Kahan-Kishore Kumar__Raag.Me__.mp3"
    mixer.init()
else:
    print("")
    
mixer.music.load(file)        # loading music 
mixer.music.play()     # palying music
