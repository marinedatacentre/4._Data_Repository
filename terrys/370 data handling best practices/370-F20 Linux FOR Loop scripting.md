---
title: "370-F20 Linux FOR Loop scripting"
source_file: "C:\Users\tchernen\handbook_docx\4_Data_Repository\terrys\370 data handling best practices\370-F20 Linux FOR Loop scripting.docx"
review_period: "3 years"
created_by: "Unknown"
created: "2021-11-06"
modified: "2021-11-06"
---

# Loop Through the Lines of a File: Bash For Loop Explained (https://codefather.tech/blog/bash-loop-through-lines-file/)

[Claudio Sabato](https://codefather.tech/author/sabato-claudio/) [Blog](https://codefather.tech/category/blog/)

I want to loop through the lines of a file with a Bash script and one of the ways to do it is using a **for loop**.

What is a for loop?

**A for loop is one of the most common programming constructs and it’s used to execute a given block of code given a set of items in a list. For instance, let’s say you want to write a program that prints the number of people who live in the 10 biggest european cities. The program can use a for loop to go through each city in the list and print the number of people for that city.**

The logic executed is every time the same and the only thing that changes is the city.

Below you can see the generic syntax for a Bash for loop:

for item in \[LIST\]

do

command1

command2

...

commandN

done

LIST can be, for example:

- a range of numbers.

- a sequence of strings separated by spaces.

- the output of a Linux command (e.g. the ls command).

The N commands between do and done are executed for each item in the list.

## **For Loop in Bash**

In this article you will learn how to use the for loop in Bash and specifically to go through the lines of a file.

But why would you do that? Going through the lines of a file?

For instance, you might need to do that if you have exported data from an application into a file and you want to elaborate that data somehow.

In this example we will use a simple .txt file in which every line contains:

- the name of a city

- the number of people who live in that city.

Below you can see the format of the text file, a colon is used to separate each city from the number of people who live in that city:

Istanbul:15,067,724

Moscow:12,615,279

London:9,126,366

...

So, how can we use a Bash for loop to go through the content of this file?

First we will store the name of the file in a variable

FILENAME="european-cities.txt"

After that, we will use another variable and the **cat** command to get all the [lines in the file:](https://codefather.tech/blog/count-lines-linux/)

LINES=\$(cat \$FILENAME)

Here we are using **command substitution** to assign the output of the cat command to the LINES variables.

Finally the for loop allows to go through each line of the file:

for LINE in \$LINES

do

echo "\$LINE"

done

**Do and done** are used to define the commands to be executed at each iteration of the for loop.

For example, if you have a file with 10 lines the for loop will go through 10 iterations and at each iteration it will read one line of the file.

The echo command can be replaced by any sequence of commands based on what you want to do with each line in the file.

Here is the final script:

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

for LINE in \$LINES

do

echo "\$LINE"

done

And the output of the script is…

./cities.sh

Istanbul:15,067,724

Moscow:12,615,279

London:9,126,366

Saint-Petersburg:5,383,890

Berlin:3,748,148

Kyiv:3,703,100

Madrid:3,223,334

Rome:2,857,321

Paris:2,140,526

Bucharest:2,106,144

We are passing the list to the for loop using the cat command.

This means we can use any commands we want to generate the LIST to be passed to the for loop.

Do you have in mind any other possible commands?

Also, the for loop is not the only option to create a loop in a Bash script, another option is a [while loop](https://codefather.tech/blog/bash-while-loop/).

## What is a Counter in a Bash For Loop?

In a for loop you can also define a variable called counter. You can use a counter to track each iteration of the loop.

The use of a counter is very common in all programming languages. It can also be used to access the elements of a data structure inside the loop (this is not the case for our example).

Let’s modify the previous program and define a counter whose value is printed at every iteration:

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

COUNTER=0

for LINE in \$LINES

do

echo "Counter \$COUNTER: \$LINE"

COUNTER=\$((COUNTER+1))

done

As you can see I have defined a variable called COUNTER outside of the for loop with its initial value set to 0.

Then at each iteration I print the value of the counter together with the line from the file.

After doing that I use the Bash arithmetic operator to increase the value of the variable COUNTER by 1.

And here is the output of the script:

Counter 0: Istanbul:15,067,724

Counter 1: Moscow:12,615,279

Counter 2: London:9,126,366

Counter 3: Saint-Petersburg:5,383,890

Counter 4: Berlin:3,748,148

Counter 5: Kyiv:3,703,100

Counter 6: Madrid:3,223,334

Counter 7: Rome:2,857,321

Counter 8: Paris:2,140,526

Counter 9: Bucharest:2,106,144

## Break and Continue in a Bash For Loop

There are ways to alter the normal [flow](https://en.wikipedia.org/wiki/Control_flow) of a for loop in Bash.

The two statements that allow to do that are **break** and **continue**:

- **break**: interrupts the execution of the for loop and jumps to the first line after for loop.

- **continue**: jumps to the next iteration of the for loop.

Having defined a counter helps us see what happens when we add break or continue to our existing script.

Let’s start with break…

I will add an [if statement](https://codefather.tech/blog/bash-if-else/) based on the value of the counter. The break statement inside the if breaks the execution of the loop if the counter is equal to 3:

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

COUNTER=0

for LINE in \$LINES

do

if \[ \$COUNTER -eq 3 \]; then

break

fi

echo "Counter \$COUNTER: \$LINE"

COUNTER=\$((COUNTER+1))

done

And the output is:

Counter 0: Istanbul:15,067,724

Counter 1: Moscow:12,615,279

Counter 2: London:9,126,366

As you can see the break statement stops the execution of the for loop before reaching the echo command because COUNTER is 3.

After that, let’s **replace break with continue** and see what happens. I will leave the rest of the code unchanged.

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

COUNTER=0

for LINE in \$LINES

do

if \[ \$COUNTER -eq 3 \]; then

continue

fi

echo "Counter \$COUNTER: \$LINE"

COUNTER=\$((COUNTER+1))

done

And here is the output for the script:

Counter 0: Istanbul:15,067,724

Counter 1: Moscow:12,615,279

Counter 2: London:9,126,366

Weird…the output is the same. Why?

That’s because when the value of COUNTER is 3 the continue statement jumps to the next iteration of the loop but it doesn’t increment the value of the counter.

So at the next iteration the value of the COUNTER is still 3 and the continue statement is executed again, and so on for all the other iterations.

To fix this we have to increase the value of the COUNTER variable inside the if statement:

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

COUNTER=0

for LINE in \$LINES

do

if \[ \$COUNTER -eq 3 \]; then

COUNTER=\$((COUNTER+1))

continue

fi

echo "Counter \$COUNTER: \$LINE"

COUNTER=\$((COUNTER+1))

done

This time we see the correct output:

Counter 0: Istanbul:15,067,724

Counter 1: Moscow:12,615,279

Counter 2: London:9,126,366

Counter 4: Berlin:3,748,148

Counter 5: Kyiv:3,703,100

Counter 6: Madrid:3,223,334

Counter 7: Rome:2,857,321

Counter 8: Paris:2,140,526

Counter 9: Bucharest:2,106,144

As you can see “Counter 3: ….” is not printed in the terminal.

## Writing a For Loop in One Line

Before finishing this tutorial, let’s see how we can write a for loop in one line.

This is not a suggested practice considering that it makes your code less readable.

But it’s good to know how to write a loop in one line, it gives more depth to your Bash knowledge.

The generic syntax for a Bash for loop in one line is the following:

for i in \[LIST\]; do \[COMMAND\]; done

Let’s print the content of our text file with a one line for loop:

\#!/bin/bash

FILENAME="european-cities.txt"

LINES=\$(cat \$FILENAME)

for LINE in \$LINES; do echo \$LINE; done

To simplify things I have removed the COUNTER and the if statement. If they were there the one line for loop would be a lot harder to read.

Try to stay away from one-liners if they make your code hard to read.

## **Conclusion**

In conclusion, in this tutorial you have learned how to:

1.  Store the lines of a file in a variable

2.  Use a for loop to go through each line.

3.  Use a counter in a for loop.

4.  Change the flow of a loop with break and continue.

5.  Write a for loop in one line.

Makes sense?

How are you going to use this?

If you want to learn more about loops in Bash scripting have a look at [this](https://codefather.tech/blog/bash-while-loop/) tutorial.
