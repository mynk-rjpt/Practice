from pygame import mixer

def playsound(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True :
        a = input()
        if a == stopper :
            mixer.music.stop()
            break

playsound("cold.mp3", "stop")   
playsound("pullmeapart.mp3","stop")