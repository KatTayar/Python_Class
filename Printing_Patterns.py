#Kathryn Tayar
#Date: Feb 15, 2023


#Write a program named PrintPatterns that prints the following three patterns using nested loops. Each print statement can print at most one character.

#Pattern 1:  1 star than 3 stars, then 5 stars, …, then 21 stars.

#*
#***
#*****
#*******
#*********
#***********
#*************
#***************
#*****************
#*******************


#Pattern 2:  Same as pattern 1 except stars are centered. Assume the bottom line starts at the margin.
#*
#***
#*****
#*******
#*********
#***********
#*************
#***************
#*****************
#*******************

 

# Pattern 3:  Assume lines starts at the margin.

##########*#########
#########***########
########*****#######
#######*******######
######*********#####
#####***********####
####*************###
###***************##
##*****************#
#*******************

# Pattern 1
for i in range(1, 12, 2):
    for j in range(i):
        print('*', end='')
    print()

# Pattern 2
for i in range(1, 12, 2):
    for j in range((11-i)//2):
        print(' ', end='')
    for j in range(i):
        print('*', end='')
    print()

# Pattern 3
for i in range(9, 0, -1):
    for j in range(i):
        print('#', end='')
    for j in range((9-i)*2+1):
        print('*', end='')
    for j in range(i):
        print('#', end='')
    print()
