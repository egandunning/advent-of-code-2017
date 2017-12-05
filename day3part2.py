#So, the first few squares' values are chosen as follows:

#    Square 1 starts with the value 1.
#    Square 2 has only one adjacent filled square (with value 1), so it also
#    stores 1.
#    Square 3 has both of the above squares as neighbors and stores the sum of
#    their values, 2.
#    Square 4 has all three of the aforementioned squares as neighbors and
#    stores the sum of their values, 4.
#    Square 5 only has the first and fourth squares as neighbors, so it gets
#    the value 5.

#Once a square is written, its value does not change. Therefore, the first few
#squares would receive the following values:

#147  142  133  122   59
#304    5    4    2   57
#330   10    1    1   54
#351   11   23   25   26
#362  747  806--->   ...

#What is the first value written that is larger than your puzzle input?

#Your puzzle input is still 347991.

import sys
import urllib.request

def main():

   if(len(sys.argv) != 2):
      print("Need cmd line arg for the number to find in the grid.")
      return

   inputNum = int(sys.argv[1], 10)

   #read sequence from oeis.org

   url = "http://oeis.org/A141481/b141481.txt"
   response = urllib.request.urlopen(url)
   data = response.read().decode('utf-8')
   
   sequence = data.split("\n");
   #remove 2 line header
   sequence = sequence[2:]
   
   for entry in sequence:
      entryPair = [int(i, 10) for i in entry.split()]
      if entryPair[1] > inputNum:
         return entryPair[1]

print(main())