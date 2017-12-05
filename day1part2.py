#Now, instead of considering the next digit, it wants you to consider the digit
#halfway around the circular list. That is, if your list contains 10 items,
#only include a digit in your sum if the digit 10/2 = 5 steps forward matches
#it. Fortunately, your list has an even number of elements.

#For example:

#    1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
#    1221 produces 0, because every comparison is between a 1 and a 2.
#    123425 produces 4, because both 2s match each other, but no other digit has a match.
#    123123 produces 12.
#    12131415 produces 4.


#input
#http://adventofcode.com/2017/day/1/input

import sys

def main():
   if(len(sys.argv) != 2):
      print("incorrect number of arguments. enter the number to process as an arg.")
      return False

   digits = sys.argv[1]
   digitsLen = len(digits)
   digitsLenHalved = digitsLen // 2

   lastDigit = "";
   result = 0;

   #loop over all digits, check if the digits halfway around the array match.
   for i in range(digitsLen):
      digit = digits[i % digitsLen]
      halfwayDigit = digits[(i + digitsLenHalved) % digitsLen]
      if halfwayDigit == digit:
         result += int(digit, 10)

   print("result: " + str(result))

main()
