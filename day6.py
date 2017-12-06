
import sys

def getMaxBank(mem):
   maxVal = 0
   maxIndex = 0
   for index in range(len(mem)):
      if mem[index] > maxVal:
         maxVal = mem[index]
         maxIndex = index

   return maxIndex, maxVal


def main():

   if(len(sys.argv) != 2):
      print("Need cmd line arg for the file containing jump instructions.")
      return

   memFile = sys.argv[1]

   mem = []

   with open(memFile, 'r') as file:
      for line in file:
         mem = [int(i, 10) for i in line.split()]
   
   pastBanks = []

   #loop until match is found
   match = False
   count = 0
   while not match:
      pastBanks.append(mem[:])
      maxBank, maxBankVal = getMaxBank(mem)
      mem[maxBank] = 0
      for i in range(maxBank + 1, maxBankVal + maxBank + 1):
         mem[i % 16] += 1

      count += 1
      for pastBank in pastBanks[0:-1]:
         if mem == pastBank:
            return count



print("Number of iterations:", main())