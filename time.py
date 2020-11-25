# In this program, i have used a class method as well as init function together, making the code very short.
class Time() :
    def __init__(self, hours, minutes, seconds) :
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds    
    def printTime(self) :
        print(f"{self.hours} : {self.minutes} : {self.seconds}")

time1 = Time(11, 56, 12)
time1.printTime()        
