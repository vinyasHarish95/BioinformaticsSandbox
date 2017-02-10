'''
Rosalind Set Theory Problem 3 --> Creating a restriction map

Before next gen sequencing, a limited picture of a person's genetic makeup could be made based on restriction digest.
Restriction enzymes cut up the person's DNA at certain restriction sites, which due to SNPs and other variations, are at
unique places for each individual.  The distances between restriction sites can be used to create what is known as a
restriction map.

Mathematically, this problem can be generalized to constructing a set from a multiset.

The solution to this problem is an implementation of an algorithm presented 'An Introduction to Bioinformatics
Algorithms' by Jones and Pevzner (2004).
'''

#Solving the partial digest problem in a time-efficient manner requires two functions: PartialDigest and Place

def partialDigest(multiset):
  width = max(multiset)
  multiset.remove(width)
  x = [0, width]
  place(multiset, x, width)

def place(multiset, x, width):
  #Base case
  if not multiset:
    x.sort()
    print x
    return x

  y = max(multiset)
  delta_Y_X = computeDeltaYX(y,x)
  delta_WidthMinusY_X = computeDeltaYX(width-y,x)

  #Adding to the front
  if (set(delta_Y_X) <= set(multiset)):
    x.append(y)
    for element in delta_Y_X:
      multiset.remove(element)
    place(multiset, x, width)
    #Backtrack if need be...
    x.remove(y)
    for element in delta_Y_X:
      multiset.append(element)

  #Adding to the back
  if (set(delta_WidthMinusY_X) <= set(multiset)):
    x.append(width-y)
    for element in delta_WidthMinusY_X:
      multiset.remove(element)
    place(multiset, x, width)
    #Backtrack if need be...
    x.remove(width-y)
    for element in delta_WidthMinusY_X:
      multiset.append(element)
  return

def computeDeltaYX(y,x):
  delta = []
  for element in x:
    delta.append(abs(y-element))
  return delta

'''
Side Problem: Make a multiset
'''
def makeMultiset(aSet):
  multiset = []
  for element in aSet:
    for anotherElement in aSet:
      if element is not anotherElement:
        multiset.append(abs(anotherElement-element))
  return multiset

def main():
  testCase = [2,2,3,3,4,5,6,7,8,10]
  print "The solution for the partial digest, and its mirror are:  "
  partialDigest(testCase)


main()
