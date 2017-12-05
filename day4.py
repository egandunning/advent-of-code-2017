#For added security, yet another system policy has been put in place. Now, a
#valid passphrase must contain no two words that are anagrams of each other -
#that is, a passphrase is invalid if any word's letters can be rearranged to
#form any other word in the passphrase.

#For example:
#    abcde fghij is a valid passphrase.
#    abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
#    a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
#    iiii oiii ooii oooi oooo is valid.
#    oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.

#Under this new system policy, how many passphrases are valid?

import sys
import io


def validPassPhrase(line):
   words = line.split()

   for i in range(len(words)):
      for j in range(i+1, len(words)):
         if words[i] == words[j]:
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

main()