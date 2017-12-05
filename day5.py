#The message includes a list of the offsets for each jump. Jumps are relative:
#-1 moves to the previous instruction, and 2 skips the next one. Start at the
#first instruction in the list. The goal is to follow the jumps until one 
#leads outside the list.

#In addition, these instructions are a little strange; after each jump, the
#offset of that instruction increases by 1. So, if you come across an offset
#of 3, you would move three instructions forward, but change it to a 4 for
#the next time it is encountered.

import sys

#return the number of jumps required to escape the maze
def main():

   if(len(sys.argv) != 2):
      print("Need cmd line arg for the file containing jump instructions.")
      return

   jumpFile = sys.argv[1]

   jumps = []

   with open(jumpFile, 'r') as file:
      for line in file:
         jumps.append(int(line, 10))
   
   index = 0
   jumpCount = 0
   while True:
      lastIndex = index #remember current index
      index += jumps[index]
      jumps[lastIndex] += 1 #increment last index
      jumpCount += 1
      #if we go out of bounds, we are done
      if index >= len(jumps):
         break
      
      

   return jumpCount



print("Number of jumps:", main())