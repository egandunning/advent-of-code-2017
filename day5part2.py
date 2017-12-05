#The message includes a list of the offsets for each jump. Jumps are relative:
#-1 moves to the previous instruction, and 2 skips the next one. Start at the
#first instruction in the list. The goal is to follow the jumps until one 
#leads outside the list.

#Now, the jumps are even stranger: after each jump, if the offset was three
#or more, instead decrease it by 1. Otherwise, increase it by 1 as before.

#Using this rule with the above example, the process now takes 10 steps,
#and the offset values after finding the exit are left as 2 3 2 3 -1.

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
      if jumps[lastIndex] >= 3:
         jumps[lastIndex] -= 1
      else:
         jumps[lastIndex] += 1 #increment last index
      jumpCount += 1
      #if we go out of bounds, we are done
      if index >= len(jumps):
         break
      
      

   return jumpCount



print("Number of jumps:", main())