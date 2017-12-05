#It sounds like the goal is to find the only two numbers in each row where
#one evenly divides the other - that is, where the result of the division
#operation is a whole number. They would like you to find those numbers on 
#each line, divide them, and add up each line's result.

#For example, given the following spreadsheet:
#5 9 2 8
#9 4 7 3
#3 8 6 5

#   -In the first row, the only two numbers that evenly divide are 8 and 2; the
#    result of this division is 4.
#   -In the second row, the two numbers are 9 and 3; the result is 3.
#   -In the third row, the result is 2.


import sys
import io

def calculatedivision(line):
   numList = line.split()

   numList = list(map(int, numList))

   for index in range(len(numList)):
      for index2 in range(len(numList)):
         if index != index2 and numList[index] % numList[index2] == 0:
            return numList[index] // numList[index2]

def main():

   if len(sys.argv) != 2 :
      print("Incorrect number of arguments! Pass the spreadsheet as a command line arg")
      return

   spreadsheetFile = sys.argv[1]

   
   divisionsum = 0

   with open(spreadsheetFile, 'r') as file:
      for line in file:
         divisionsum += calculatedivision(line)
   
   print("sum: {}".format(divisionsum))

   file.close()

main()