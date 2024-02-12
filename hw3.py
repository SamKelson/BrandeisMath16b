'''
Use this space to copy and paste functions you wrote in 
the last class. For example:
'''

def dot(v1: list, v2: list) -> float:
  '''
  Parameters
  ----------
  - v1: list
  - v2: list

  Returns
  -------
  float

  Returns the dot product of v1 and v2
  '''

  result = 0.0
  for element in range(0,len(v1)):
    result += v1[element]*v2[element]
  return result

# solution starts here:

def is_scalar_multiple(v1, v2):
  '''
  Parameters
  ----------
  - v1: list
  - v2: list

  Returns
  -------
  True if v1 and v2 are linearly dependent, and False otherwise
  '''
  
  #basicly: go through each element of v1 and v2 and check if the same scalar multiple can be applied to each element to make them equal

  #if the vectors are not the same length, they cannot be scalar multiples
  if len(v1) != len(v2):
    return False
  
  #check if either vector is all zeros
  for vec in [v1,v2]:
    allZero = True
    for i in vec:
      if i != 0:
        allZero = False
        break
    if allZero:
      return True

  for i in range(len(v1)):
    if v1[i] == 0 and v2[i] == 0:
      continue
    if v1[i] == 0 or v2[i] == 0:
      return False
    if v1[0] / v2[0] != v1[i] / v2[i]:
      return False
  return True

def count_vectors(vectors):
  '''
  Parameters
  ----------
  - vectors: a list of vectors (not necessarily of the same 
    dimension)

  Returns
  -------
  A dictionary whose keys are the vectors, and whose values 
  are the number of occurances of each vector. 

  For example:
  count_vectors([(1,0), (1,0), (2,3), (0,0), (0,)])
    = {(1,0) : 2, (2,3) : 1, (0,0): 1, (0,): 1}
  '''
  
  #start by creating dictionary
  dict = {}

  #go through vecs and put into dict depending on if the vec is already there or not
  for vec in vectors:
    if vec not in dict:
      dict[vec] = 1
    else:
      dict[vec] += 1
  return dict

def reverse_dictionary(d):
  '''
  Parameters
  ----------
  - d: dictionary whose values are immutable

  Returns
  -------
  reversed dictionary, whose keys are the values of d, 
  and whose values are lists of keys of d.

  For example:
  reverse_dictionary({1 : a, 2: b, 3: b}) 
    ={a : 1, b: [2,3]}
  '''
  
  #grab the list of keys which will become the values of the new dict
  keys = list(d.keys())
  #grab the list of values which will become the keys of the new dict
  values = list(d.values())

  #create new dict
  new_dict = {}

  # and new keys to the new dict
  for value in values:
    new_dict[value] = []

  #populate new dict with old dict keys
  for key in keys:
    new_dict[d[key]].append(key)

  return new_dict

def normalize(v):
  '''
  Parameters
  ----------
  - v: list representing a nonzero vector

  Returns
  -------
  - normalized_v: list

  Returns v/|v|
  '''

  #find the magnitude of the vector
  magnitude = dot(v,v)**0.5

  if magnitude == 0 or magnitude == 1:
    return v

  #divide each element by magnitude
  for i in range(len(v)):
    v[i] = v[i]/magnitude

  return v

def orthogonal_projection(v, w):
  '''
  Parameters
  ----------
  - v: list
  - w: list (nonzero)

  Returns
  -------
  The orthogonal projection of v onto w. Returns 
  two vectors, x and y such that:
    1. v = x + y
    2. x is parallel to w
    3. y is perpendicular to w
  '''
  
  #get parallel vect by multiplying the norm of w by the dot product of v and w
  parrel_vector = [i*dot(v,w) for i in normalize(w)]

  #get perpendic vect by subtracting the parallel vect from v
  perpendic_vector = [v[i] - parrel_vector[i] for i in range(len(v))]

  return parrel_vector, perpendic_vector