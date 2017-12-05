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