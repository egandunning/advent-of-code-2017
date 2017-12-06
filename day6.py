#In this area, there are sixteen memory banks; each memory bank can hold any
#number of blocks. The goal of the reallocation routine is to balance the
#blocks between the memory banks.

#The reallocation routine operates in cycles. In each cycle, it finds the
#memory bank with the most blocks (ties won by the lowest-numbered memory
#bank) and redistributes those blocks among the banks. To do this, it removes
#all of the blocks from the selected bank, then moves to the next (by index)
#memory bank and inserts one of the blocks. It continues doing this until it
#runs out of blocks; if it reaches the last memory bank, it wraps around to
#the first one.

#The debugger would like to know how many redistributions can be done before
#a blocks-in-banks configuration is produced that has been seen before.

#Given the initial block counts in your puzzle input, how many
#redistribution cycles must be completed before a configuration is produced
#that has been seen before?

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
   cycle = 0
   while True:
      pastBanks.append(mem[:])
      maxBank, maxBankVal = getMaxBank(mem)
      mem[maxBank] = 0
      for i in range(maxBank + 1, maxBankVal + maxBank + 1):
         mem[i % 16] += 1

      if match == True:
         cycle += 1
      for pastBank in pastBanks[0:-1]:
         if mem == pastBank:
            if match == True:
               return cycle + 1
            match = True
            pastBanks = pastBanks[-1:]



print("Number of iterations:", main())