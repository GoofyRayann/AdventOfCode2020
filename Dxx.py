import string
import copy
import math
import copy

from collections import defaultdict
import re
import ast
DAY="20"
inputFile = "D:\Dev_Perso\\adventofcode.com\D1\D"+DAY+"_input.txt"
#inputFile = "D:\Dev_Perso\\adventofcode.com\D1\D"+DAY+"_sample.txt"

print("====================================================================================================")

print("- D"+DAY+" ---------------------------------------------------------------------------------")
print(inputFile)

def read_puzzle( file ):
    with open(file) as f:
        puzzle = [ line.rstrip("\n") for line in f.readlines()]
    return puzzle


def Puzzle_1(puzzle):
    res=0

    return res


def Puzzle_2(puzzle):
    res=0
    return res

print("------------------------------------------------------------------------------------------")

puzzle    = read_puzzle(inputFile)
print(puzzle)

value =  Puzzle_1( puzzle )
print( "       PUZZLE_1 : " + str(value) + " " )

puzzle    = read_puzzle(inputFile)
val2 = Puzzle_2( puzzle )
print( "       PUZZLE_2 : " + str(val2) + " " )

print("------------------------------------------------------------------------------------------")
print('END')

