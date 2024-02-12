#Sam Kelson HW2

def is_in_first_quadrant(vector: list) -> bool:
  '''
  Parameters
  ----------
  - vector: length 2 list

  Returns
  -------
  Boolean

  Returns True when vector is in the first quadrant (ie, 
  all of its entries are non-negative). Returns 
  False otherwise.
  '''
  return vector[0] >= 0 and vector[1] >= 0


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


def norm(v: list) -> float:
  '''
  Parameters
  ----------
  - v: list

  Returns
  -------
  float

  Returns the Euclidean norm of v
  '''
  result = 0.0
  for element in range(0,len(v)):
    result += v[element]**2
  return result**(1/2)


def largest_norm(vectors: "list[list]") -> list:
  '''
  Parameters
  ----------
  - vectors: list of lists

  Returns
  -------
  - v: vector

  Returns the vector v which has the largest norm 
  of all the vectors in 'vectors'. In case of a tie, returns 
  the first vector in the list.
  '''
  result = vectors[0]
  for vector in range(0,len(vectors)):
    if norm(vectors[vector]) > norm(result):
      result = vectors[vector]
  return result
