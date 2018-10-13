# Reactive Programming Assignment

Repository to hold the code for the reactive programming homework.

# Setup

1. Make sure you have `python3` and `pip` for python3 (`pip3`) installed.

2. Install ReactiveX for python 3 with the command:

`pip3 install rx`

3. Run `test.py` with python 3. If it runs successfully, you should see the following output:

`Imported all objects and libraries successfully!`

and you can continue to the assignment.

# The Assignment

In this assignment, you will program a timer using the observer-observable architecture central to reactive systems.

The timer will count the number of seconds and minutes since the program started, and it will look like the following:

    xxxxxxxxx
    x 00:05 x
    xxxxxxxxx


Every minute, the timer will alternate its border between `x` and `+`:

    +++++++++
    + 01:02 +
    +++++++++

    xxxxxxxxx
    x 02:30 x
    xxxxxxxxx

    +++++++++
    + 03:07 +
    +++++++++
    
To do so, the program will use two classes from ReactiveX's python implementation: `Observable` and `Observer`. An `Observable` is essentially a stream of data over time, and an `Observer` is component that may subscribe to an `Observable` and react to data from the `Observable` stream. 

The following code shows an example of coding the `Observable` / `Observable` paradigm with ReactiveX in python:

```python
from rx import Observable, Observer

class exampleObserver(Observer): # inherit from Observer, define a new class

    def __init__(self, name):
        self.name = name

    def on_next(self, value):
        print(str(self.name) + ": observed " + str(value))

    def on_completed(self):
        print(str(self.name) + ": stream completed!")

    def on_error(self, error):
        print(str(self.name) + ": encountered an error '" + str(error) + "'")


# Observer/Observable example
 
example_source = Observable.of("Event A", "Event B", "Event C", "Event D")
 
example_observer = exampleObserver("example observer")
 
example_source.subscribe(example_observer)
```

The output of this would be:

    example observer: observed Event A
    example observer: observed Event B
    example observer: observed Event C
    example observer: observed Event D
    example observer: stream completed!


In this code, `example_source` is an `Observable` populated with events `A`, `B`, `C`, and `D`.When `example_observer` is subscribed to `example_source`, it reacts to all of the events in the way defined in its `on_next` method. Changing code in `on_next` changes the way `example_observer` reacts.

For this assigment, you will use the method `interval` of `Observable`, which produces a stream of consecutive integers at the given interval (in milliseconds). For example, if you change the lines after `# Observer/Observable example` to the following:

```python
example_source = Observable.interval(2000)
                            
example_observer = exampleObserver("example observer")
                            
example_source.subscribe(example_observer)

input("Press Enter to end program\n") # needed to keep program running
```
Then you will get a consecutive integer printed out every 2 seconds (2000 milliseconds):

    Press Enter to end program
    example observer: observed 0
    example observer: observed 1
    example observer: observed 2
    example observer: observed 3
    example observer: observed 4
    example observer: observed 5
    example observer: observed 6

The program will continue until you press Enter.

For this assignment, you will use the `interval` method of `Observable` and a predefined `secondObserver` class (in `hw.py`) to print a timer every second with the number of seconds and minutes passed since the program started. Additionally, a second `Observable` will use  the `interval` method to alternate the timer border between `x` and `+` every minute, using the predefined `minuteObserver` class (in `hw.py`). The global variable `timer_border` is provided for convenience, and it will need to be changed in the `on_next` method of minuteObserver.


The code for the assignment is located in `hw.py`, and all of the places to add code are marked with `todo: `. When you add the required code to `hw.py`, your output should look like this:

    xxxxxxxxx
    x 00:05 x
    xxxxxxxxx

and the border should alternate every minute like this:

    +++++++++
    + 01:02 +
    +++++++++

    xxxxxxxxx
    x 02:30 x
    xxxxxxxxx

    +++++++++
    + 03:07 +
    +++++++++


**Note:** to format an integer to a width of 2 with leading 0's, use the following:

```python
"%02d" % (number)
```