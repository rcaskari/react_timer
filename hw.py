from rx import Observable, Observer

import os
import math


def clearConsole(): # function to clear the console; cross-platform; provided here for convenience
    if os.name == "nt": # windows
        os.system("cls")
    else: # unix
        os.system("clear")


global timer_border
timer_border = 'x' # border of the timer; default is 'x'

class secondObserver(Observer): # class to print a timer every time 'on_next' is called

    def on_next(self, value):

        clearConsole() # clear the console before printing the new timer

        seconds = str("%02d" % (value % 60)) # todo: change this to the number of seconds passed (hint: use value in some way)
        minute =  str("%02d" % (math.floor(value/60))) # todo: change this to the number of minutes passed (hint: use value in some way)



        print(timer_border * 9)
        print(timer_border + " " + minute + ":"+ seconds + " " +timer_border) # todo: change the on_next method to print a timer with the program time
        print(timer_border * 9)

    def on_completed(self):
        print("second stream completed!")

    def on_error(self, error):
        print("second stream errored: " + "'" + str(error) + "'")


class minuteObserver(Observer): # class to change the timer border every minute

    def on_next(self, value):
        global timer_border # need this to modify timer_border

        if value % 2 == 0:
            timer_border = '+'# todo: change the on_next method to alternate the timer border between any two characters (hint: use value in some way)
        else:
            timer_border = 'x'


    def on_completed(self):
        print("minute stream completed!")

    def on_error(self, error):
        print("minute stream errored: " + "'" + str(error) + "'")




# todo: fill in the following lines

second_stream = Observable.interval(1000) # todo: add a stream here that the observer will subscribe to that will print out the timer every second

second_observer = secondObserver() # todo: add an observer here that will subscribe to this stream

second_stream.subscribe(second_observer)# todo: subscribe the second observer to the stream


minute_stream = Observable.interval(60000) # todo: add a stream here that the observer will subscribe to that will change the timer border every minute (global timer_border)

minute_observer = minuteObserver() # todo: add an observer here that will subscribe to this stream

minute_stream.subscribe(minute_observer)# todo: subscribe the minute observer to the stream


input("") # wait until the user hits enter to exit; do not remove
