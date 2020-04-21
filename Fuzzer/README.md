# Fuzzer
I made this fuzzer about 2 years ago and I am in the process of improving it.

## Description and Deliverables
Hunting for bugs is a common task for all programmers, but especially those concerned about cybersecurity. While bugs may be a nuisance to typical users (i.e., people get annoyed when programs crash or don't behave as expected), bugs are a vital resource for malicious actors. Finding bugs in a program is the first step towards isolating exploitable bugs that can be leveraged for attacks against that program.

A fuzzer is a program that tries to find bugs in other programs. This fuzzer will take two inputs: (1) a program specification in XML format, and (2) the path to the target program. It then repeatedly executes the target program with different command line arguments in an attempt to make the target program crash. It reports which command line inputs caused the target program to crash. In the real world, the developer of the target program would then use this information to find and patch the bugs in their program.

Each of these deliverables is described in greater detail below.

## Background
There are many tools and frameworks that help programmers find bugs. Some, like unit tests, are developed by the programmer, included in source code, and are tightly integrated with a given program. This project was a chance to draw on those test development skills. 

Other bug finding tools are more general, and are designed to help find bugs in any program. Fuzz testing, or simply fuzzing, is a black-box technique for attempting to find bugs in programs. This technique is often implemented in a program called a fuzzer. The goal of a fuzzer is repeatedly execute a target program and attempt to crash it by supplying it with a variety of strange inputs. In other words, the goal of the fuzzer is to find bugs in the target, where the programmer has failed to deal with corner-cases in input handling code. Fuzzing is a black-box technique because it does not depend on the source code of the target. Any program that accepts external input (and almost all do) can be fuzzed.

## Motivating Example
Let's imagine that someone wrote a very simple, command line calculator app. The calc program works like this:

$ ./calc
Usage: $ ./calc [number] [operation (+, -, *, /)] [number]
$ ./calc 1 + 1
2
$ ./calc 10 / 5
2

calc takes exactly three command line arguments: a number, a string that signifies a simple mathematical operation, and another number.

The examples above demonstrate that calc works as expected... when the command line inputs conform to the program specification. However, take a moment and speculate about all the ways that calc might crash if it was supplied with unexpected, or carefully crafted, command line inputs. Think about all the corner cases that the developer of calc may have forgotten to handle in their code. For example:

    What if the user supplies less than three arguments? What if they supply more than three arguments?
    What if the user doesn't input a number for argument one or three?
    What if the user doesn't input "+", "-", "*", or "/" for argument two?
    What if the user inputs a negative number?
    What if the user inputs a really, really large number?
    What if the user inputs zero for the third argument when argument two is set to division?

The idea behind a fuzzer is that it will automatically run a target program, like calc, over and over again with different combinations of command line inputs, to try and trigger bugs and expose them, so they can be fixed.

## Fuzzer Specification and Design
A command line program named fuzzer that performs model-based checking of other command line programs. 

$ ./fuzzer [path to XML configuration file] [path to the target program]

The fuzzer program takes exactly two command line arguments, each of which is a file path. The first path will point to an XML-formatted configuration file that describes the model for fuzz testing the target program. The second path points to the target program itself. It uses the given model to construct a variety of command line arguments for the target program, and will execute the target program repeatedly to see if it crashes. The fuzzers then outputs all command lines that caused the target program to crash. Returning to our calc example, the fuzzer might generate the following output:

$ ./fuzzer calc_model.xml calc
./calc A B C
./calc 1 A B
./calc 1 / 0

Each of these sets of command line arguments causes calc to crash. For example, ./calc A B C and ./calc 1 A B cause it to crash because one or more arguments that are supposed to be numbers are not.

$ ./calc A B C
Traceback (most recent call last):
    File "./calc", line 9, in <module>
    n1 = int(sys.argv[1])
ValueError: invalid literal for int() with base 10: 'A'

Note that fuzzer tried to run calc with many other sets of command line arguments that did not result in crashes, thus they were not printed out. Some other example command lines that it might have tried include:

    ./calc A, doesn't crash because the program makes sure exactly three command line arguments are supplied
    ./calc A B C D, doesn't crash for the same reason as above
    ./calc 1 A 1, doesn't crash, or print anything, because argument two isn't a valid mathematical operator

## Model Specification
My fuzzer program is able to test a wide variety of command line programs. 

This is where the model comes into play. The fuzzer reads a model, specified in XML, that describes the command line arguments of the target program. The general XML format of models is as follows:

<spec>
    <options>
        <option>
            <name>Name of the optional argument</name>
            <type>Type of the optional argument</type>
        </option>
        ...other options...
    </options>
    <positional>
        <arg>
            <type>Type of the positional argument</type>
        </arg>
        ...other positional arguments...
    </positional>
</spec>

The model specification is divided into two sections: optional arguments and positional arguments. Optional arguments are command line arguments that are typically prefaced with - or --, and as their name implies, they are optional. The <name> of an optional argument is literally its name on the command line. Positional arguments are the command line arguments that must be passed into the target program, in a specific order, for it to function. Both optional and positional arguments have a <type>, which is the data type of that argument. For the purposes of this project, the only types I dealt with are integers, strings, and null, which is a special case for optional arguments.

Returning to our calc example, this program takes exactly three positional command line arguments. The model specification for calc would be:

<spec>
    <positional>
        <arg>
            <type>integer</type>
        </arg>
        <arg>
            <type>string</type>
        </arg>
        <arg>
            <type>integer</type>
        </arg>
    </positional>
</spec>

This model captures our understanding of how calc should work: it takes three arguments, the first and third are integers, and the second is a string.

Here is a slightly more complex example:

$ ./buy-food
usage: buy-food [-h] [--organic] [--quantity QUANTITY] [--store STORE] food area
buy-food: error: the following arguments are required: food, area
$ ./buy-food -h
usage: buy-food [-h] [--organic] [--quantity QUANTITY] [--store STORE] food area

Buy food online by typing what you want and the city to deliver it to.
Currently only supports Boston area deliveries.

positional arguments:
  food                  The name of the food you want
  area                  The name of the area to deliver to

optional arguments:
  -h, --help            show this help message and exit
  -o, --organic         Make sure the food is organic. Default=False
  -q QUANTITY, --quantity QUANTITY
                        How many pieces of food do you want? Default=1
  -s STORE, --store STORE
                        Deliver from the given store. Default=Trader Joes
$ ./buy-food taco roslindale
Great, we're delivering your taco to roslindale!
$ ./buy-food --organic "clam juice" "harvard square"
Great, we're delivering your organic clam juice to harvard square!

This program has three optional command line arguments (four if you count --help, but we don't care about that), and two required positional arguments. The XML specification for buy-food is:

<spec>
    <options>
        <option>
            <name>--organic</name>
            <type>null</type>
        </option>
        <option>
            <name>--quantity</name>
            <type>integer</type>
        </option>
        <option>
            <name>--store</name>
            <type>string</type>
        </option>
    </options>
    <positional>
        <arg>
            <type>string</type>
        </arg>
        <arg>
            <type>string</type>
        </arg>
    </positional>
</spec>

The data types of --quantity and --store make intuitive sense. --organic has a data type of "null" because it does not accept any additional data on the command line. This type of command line argument is often referred to as a flag, and it typically turns some program functionality on or off (in this case, the desire for organic food).
