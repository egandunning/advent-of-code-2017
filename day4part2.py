#A new system policy has been put in place that requires all accounts to use
#a passphrase instead of simply a password. A passphrase consists of a series
#of words (lowercase letters) separated by spaces.

#To ensure security, a valid passphrase must contain no duplicate words.

#For example:
#    aa bb cc dd ee is valid.
#    aa bb cc dd aa is not valid - the word aa appears more than once.
#    aa bb cc dd aaa is valid - aa and aaa count as different words.

#The system's full passphrase list is available as your puzzle input.
#How many passphrases are valid?

import sys
import io

def isPermutation(word1, word2):
   chars1 = list(word1)
   chars2 = list(word2)

   charsToDelete = []

   for ch in chars1:
      for ch2 in chars2:
         if ch == ch2:            
            charsToDelete.append(ch)

   for ch in charsToDelete:
      try:
         chars1.remove(ch)
         chars2.remove(ch)
      except:
         #do nothing
         _ = 0

   if len(chars1) == 0 and len(chars2) == 0:
      return True
   return False

def validPassPhrase(line):
   words = line.split()

   for i in range(len(words)):
      for j in range(i+1, len(words)):
         if isPermutation(words[i], words[j]):
            return 0
   return 1

def main():

   if len(sys.argv) != 2 :
      print("Incorrect number of arguments! Pass the passphrase filename as a command line arg")
      return

   passFile = sys.argv[1]

   validCount = 0

   with open(passFile, 'r') as file:
      for line in file:
         validCount += validPassPhrase(line)
   
   print("Valid passphrases: {}".format(validCount))

   file.close()

print(isPermutation("abcde", "ecdab"))
main()