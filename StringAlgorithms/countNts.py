'''
ROSALIND Task #1

Exactly what it sounds like, count the 4 nucleotides.
I came up with the brute force solution immediately, but wanted to compare the
performance against a better method that I really should've came up with!
'''
import time

def countNts_BruteForce(string):
  #The brute force solution is the one that I immediately came up with, but its
  #definitely not a very Pythonic solution.
  countA, countT, countC, countG  = (0,) * 4

  for i in range(len(string)):
    if string[i] == 'A':
      countA += 1
    if string[i] == 'T':
      countT += 1
    if string[i] == 'C':
      countC += 1
    if string[i] == 'G':
      countG += 1

  print "Number of A's = ", countA
  print "Number of T's = ", countT
  print "Number of C's = ", countC
  print "Number of G's = ", countG

def countNts_countMethod(s):
  #Count is a Python built-in C-level function, so this should run much much faster than
  #the loop I have above.
  return s.count("A"), s.count("T"), s.count("C"), s.count("G")

def main():
  print "---Running Brute Force Method---"
  bruteForce_start = time.time()
  countNts_BruteForce('TTTCAGTTTTACATCCACAAAGGTGAAATAAATTGCAACCGCTCTCTTATGTAACTCTCGCGTCTGCATCAGAGTAAAAATCGTTGAGTTTATGCCATAGGAAACCATCCCCTCCACATCAACTGAACGCTTCTGTGGTAGTCCGATTTTACCTAATAGCCACAGTGTTCTACCTGAAGTCAGGGAGCCATCCTCCAAGGATATCCCTGCCTATCTTATACCACGTGAAGTTATTTGGGTACCACAAAAATTTATCGTTAGTCGAACCGAGTGGGGGGCAACAAGGTGTGCTGTCATAAAAAGAGTCCTGACCTGGGAATTTGAGTATAAGGAATCTAGCCGGCTCGCAAATACGTACGTGTACATTTTGAGGTACGGTCGCCCCTAGGAGGCATAGAACCAGACGCAGTGGGGAAGATTGCACGTTCGTTTACCCAGGACAGGGACGGTACGCTGTTTGGCAGGATCAGAGGAAATACATACTTAGGGCCGTGGCTGAAGGATCCAACGACGGCATTCCAAAATCCCGAACCGAGTCGGAACGTCTTATGCCCTAAAAATGTTGTTACGCATGCCGCGTCAAGCGCTGACGCGCCAGCTCATTTCACGCAATGCGTTATGGCGTAAACTCATACCGCTAAGGGTTTTAGAGTACCTTTAGAGAGTTGAATTCTACCTAGGCTCCGCGGTTTGGCGGGCCGAAAATAACAAACTCGTTGTGCGGGGGCTAATCTTTAGCTTTAACAAAGTCGAACTGGACCAAATGTTCTTAAGGTCCATCTGCTCTAGGTACCTCCGTCCTCAGGTTCATCAC')
  bruteForce_stop = time.time()
  bruteForce_time = bruteForce_stop - bruteForce_start
  print "Brute Force:", bruteForce_time

  print "---Running Count Method---"
  countMethod_start = time.time()
  print countNts_countMethod('TTTCAGTTTTACATCCACAAAGGTGAAATAAATTGCAACCGCTCTCTTATGTAACTCTCGCGTCTGCATCAGAGTAAAAATCGTTGAGTTTATGCCATAGGAAACCATCCCCTCCACATCAACTGAACGCTTCTGTGGTAGTCCGATTTTACCTAATAGCCACAGTGTTCTACCTGAAGTCAGGGAGCCATCCTCCAAGGATATCCCTGCCTATCTTATACCACGTGAAGTTATTTGGGTACCACAAAAATTTATCGTTAGTCGAACCGAGTGGGGGGCAACAAGGTGTGCTGTCATAAAAAGAGTCCTGACCTGGGAATTTGAGTATAAGGAATCTAGCCGGCTCGCAAATACGTACGTGTACATTTTGAGGTACGGTCGCCCCTAGGAGGCATAGAACCAGACGCAGTGGGGAAGATTGCACGTTCGTTTACCCAGGACAGGGACGGTACGCTGTTTGGCAGGATCAGAGGAAATACATACTTAGGGCCGTGGCTGAAGGATCCAACGACGGCATTCCAAAATCCCGAACCGAGTCGGAACGTCTTATGCCCTAAAAATGTTGTTACGCATGCCGCGTCAAGCGCTGACGCGCCAGCTCATTTCACGCAATGCGTTATGGCGTAAACTCATACCGCTAAGGGTTTTAGAGTACCTTTAGAGAGTTGAATTCTACCTAGGCTCCGCGGTTTGGCGGGCCGAAAATAACAAACTCGTTGTGCGGGGGCTAATCTTTAGCTTTAACAAAGTCGAACTGGACCAAATGTTCTTAAGGTCCATCTGCTCTAGGTACCTCCGTCCTCAGGTTCATCAC')
  countMethod_stop = time.time()
  countMethod_time = countMethod_stop - countMethod_start
  print "Built-in Count Method:", countMethod_time

main()
