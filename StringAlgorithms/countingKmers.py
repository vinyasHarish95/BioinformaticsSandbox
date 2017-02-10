'''
Counting Kmers in DNA
'''

'''
Part 1 - Find the most frequent kmer
'''
# Function Complexity Analysis
# - Adding all kmers to dictionary -> O(n) to find
#                                     O(1) to actually store in data structure
#                                     O(n) in worst case
#                                     O(n) to keep checking if its in dictionary
# - Find maximum element in dictionary -> O(n) where n = (n-k+1)
# - Iterate through all elements in dictionary -> O(n) where n = (n-k+1)
import itertools

def countKmer(dna,k):
  #Create dictionary
  kmerDict = {}
  for x in range(len(dna)+1-k):
    kmer = dna[x:x+k]
    #Add to the dictionary and increment count
    kmerDict[kmer] = kmerDict.get(kmer, 0)+1
  #Find the number of occurrences of the most frequent kmer
  maximumVal = max(kmerDict.values())
  mostFreqKmers = []
  #Iterate through the dictionary and return the most frequent kmers in a list
  for kmer in kmerDict:
    if kmerDict[kmer] == maximumVal:
      mostFreqKmers.append(kmer)
  return (kmerDict, mostFreqKmers, maximumVal)

'''
Part 2 - Find the most frequent kmer with at most d mismatches
'''
def check(element1,element2):
  if element1 is not element2:
    return 1
  else:
    return 0

def countKmerWMismatches(dna,k,d):
  #Create list with all patterns
  patterns = []
  for x in range(len(dna)+1-k):
    kmer = dna[x:x+k]
    if kmer not in patterns:
      patterns.append(kmer)
  #Make a list where  each kmer found and the value is a list of
  #matches with at most d mismatches
  #[[Kmer1,[matches]],[Kmer2,[matches]]]
  kmerList = []
  for pattern in patterns:
    #Reslide through the DNA
    matchList = []
    numMatches = 0
    for x in range(len(dna)+1-k):
      kmer = dna[x:x+k]
      #Compute Hamming Distance
      hammDist = 0
      for nt1, nt2 in itertools.izip(kmer,pattern):
        hammDist = hammDist + check(nt1, nt2)
      #Add to matches if at most d mismatches
      if (hammDist <= d):
        numMatches += 1
    kmerList.append([pattern,numMatches])
  #Report the kmers that maximize the countd function
  maximumStringCountPair = max(kmerList,key=lambda x:x[1])
  maximumVal = maximumStringCountPair[1]
  optimalKmers = []
  for kmer in kmerList:
    if kmer[1] == maximumVal:
      optimalKmers.append(kmer[0])
  return optimalKmers

def main():
  print 'Task 1: Find the most common kmers without mismatches'
  sample = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
  kVal = 4
  (kmerDict, mostFreqKmers, maximumVal) = countKmer(sample,kVal)
  print "The most frequent kmers are: ", mostFreqKmers
  print "These kmers appeared %d times" % maximumVal

  print 'Task 2: Find the most common kmers with mismatches'
  sample2 = 'ACTATGCATACTATCGGGAACT'
  aList = countKmerWMismatches(sample2,5,1)
  print aList

main()
