'''
ROSALIND Task #5

Compute the GC-content of a strand of DNA. While it sounds trivial, this has some
pretty important consequences.  G's and C's are connected by three H-bonds as
opposed to two, so this gives a pretty quick insight into the "strength" of the
DNA and corresponding melting point.

Identifying GC content also offers a quick way of identifying if a sample comes
from a prokaryote or eukaryote and can even be used to identify species.
'''

def readFASTA(filename):
  try:
    f = file(filename)
  except IOError:
    print "The file, %s, does not exist!" % filename
    return

  strands = {}

  for line in f:
    if line.startswith('>'):
      name = line[1:].rstrip('\n')
      strands[name] = ''
    else:
      strands[name] += line.rstrip('\n').rstrip('*')

  strandCount = len(strands)
  print "%d sequences were read from the input FASTA file." % strandCount
  return strands

def countGC(strand):
  gcCount = 0
  for nt in strand:
    if (nt == 'G') or (nt == 'C'):
      gcCount += 1
  return gcCount

def main():
  strands = readFASTA('SampleData/rosalind_gc.txt')
  #Create dictionary with strand names and corresponding GC contents
  gcContentDict = {}
  for strandName,sequence in strands.iteritems():
    gcContent = (countGC(sequence) / float(len(sequence))) * 100
    gcContentDict[strandName] = gcContent

  #Find key with highest value in the newly created, GC Content dictionary
  targetStrandName = max(gcContentDict, key = lambda i: gcContentDict[i])
  targetStrandGcContent = gcContentDict[targetStrandName]
  print "DNA sequence with highest GC content:  %s" % targetStrandName
  print "GC content of that DNA sequence:  %s" % targetStrandGcContent

main()
