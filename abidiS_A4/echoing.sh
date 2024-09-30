#!/bin/bash

# Activity 1: Displaying Messages
echo "The time and date are: $(date)" 
echo "Let's see who is logged into the system: $(who)"
echo "For $USER, the home directory is $HOME"

# Activity 2: Working w Positional Args
NAME=$1
MONEY=$2

echo "My name is $NAME and I have \$$MONEY in my wallet." 

# Activity 3: Math Time
MATHVAR1=$((1+5))
MATHVAR2=$((MATHVAR1*20))
MATHVAR3=10
MATHVAR4=$((MATHVAR1*(MATHVAR2+MATHVAR3)))

echo "Variable 1 is $MATHVAR1. Variable 2 is $MATHVAR2. Using $MATHVAR3 for variable 3, our final variable 4 is $MATHVAR4"
# Activity 4: More Math
FLOATING=$(echo "scale=4; 4.5/1.7" | bc)
echo "Our floating point variable is $FLOATING"
