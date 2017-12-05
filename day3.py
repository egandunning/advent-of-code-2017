#You come across an experimental new kind of memory stored on an infinite
#two-dimensional grid.

#Each square on the grid is allocated in a spiral pattern starting at a
#location marked 1 and then counting up while spiraling outward. For example,
#the first few squares are allocated like this:

#17  16  15  14  13
#18   5   4   3  12
#19   6   1   2  11
#20   7   8   9  10
#21  22  23---> ...

#While this is very space-efficient (no squares are skipped), requested data
#must be carried back to square 1 (the location of the only access port for
#this memory system) by programs that can only move up, down, left, or right.
#They always take the shortest path: the Manhattan Distance between the
#location of the data and square 1.

#For example:

#    Data from square 1 is carried 0 steps, since it's at the access port.
#    Data from square 12 is carried 3 steps, such as: down, left, left.
#    Data from square 23 is carried only 2 steps: up twice.
#    Data from square 1024 must be carried 31 steps.

#How many steps are required to carry the data from the square identified in
#your puzzle input all the way to the access port?

#Your puzzle input is 347991.

import sys

#returns the manhattan distance described above for numbers greater
#than 3.
def main():

   if(len(sys.argv) != 2):
      print("Need cmd line arg for the number to find in the grid.")
      return

   inputNum = int(sys.argv[1], 10)

   inputSqrt = inputNum**(1 / 2)

   #Cool pattern for square numbers!!
   if(inputSqrt == int(inputSqrt)):
      return int(inputSqrt) - 1

   #Get list of squared odd numbers: Numbers that end a square are odds squared
   oddsSquared = [i**2 for i in range(int(inputNum)) if i % 2 == 1]

   #find the two elements of the list of odds squared that the input number
   #falls in between: x < inputNum < y where x, y are consecutive elements in
   #oddsSquared
   x = 0
   y = 0
   for i in range(len(oddsSquared)):
      if oddsSquared[i] > inputNum:
         x = oddsSquared[i-1]
         y = oddsSquared[i]
         break

   #Use square root trick from above to jump to the manhattan distance
   manhattanSum = int(x**(1 / 2))

   #The length of repeating patterns. Note: guaranteed to be even.
   cycle = int(y**(1 / 2)) - 1

   halfCycle = cycle // 2

   i = x + 1
   while True:
      #first half of cycle, manhattan distances get shorter
      for _ in range(halfCycle):
         if(i != x + 1):
            manhattanSum -= 1
         i += 1
         if i > inputNum:
            break
      if i > inputNum:
         break
      #second half of cycle, manhattan distances get longer
      for _ in range(halfCycle):
         manhattanSum += 1
         i += 1
         if i > inputNum:
            break
      if i > inputNum:
         break
   return manhattanSum


print(main())