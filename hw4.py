import numpy as np

'''
Use this space to copy and paste functions you wrote in 
the last class.
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

  result = 0
  for element in range(0,len(v1)):
    result += v1[element]*v2[element]
  return result

def multiply(M: "list[list]", v: list) -> list:
  '''
  Parameters
  ----------
  - M: list of lists 
  - v: list

  Returns
  -------
  list

  Returns the vector Mv
  '''

  #return a list of the dot product of each row of M and v
  return [dot(M[row],v) for row in range(len(M))]


def transpose(M: "list[list]") -> "list[list]":
  '''
  Parameters
  ----------
  - M: list of lists

  Returns
  -------
  list of lists corresponding to the transpose of M

  '''

  #simply return the list of lists with the rows and columns swapped by first going through the columns and then the rows and placing elements accordingly
  return  [ [M[row][col] for row in range(len(M))] for col in range(len(M[0]))]

def complex_multiply(z1: tuple, z2: tuple) -> tuple:
  '''
  Parameters
  ----------
  - z1: tuple corresponding to the real and imaginary part of
    a complex number
  - z2: tuple corresponding to the real and imaginary part of
    a complex number

  Returns
  -------
  tuple corresponding to z1*z1
  
  '''

  #create matricies for z1 and z2
  m1 = [[z1[0],-1*z1[1]],
        [z1[1],z1[0]]]
  m2 = [[z2[0],-1*z2[1]],
        [z2[1],z2[0]]]
  #multiply the matricies
  result = [[dot(m1[row], [m2[i][col] for i in range(len(m2))]) for col in range(len(m2[row]))] for row in range(len(m1))]
  return (result[0][0],result[1][0])
  


def rotate_matrix(M:"list[list]") -> list:
  '''
  Parameters
  ----------
  - M: square matrix given as list of lists

  Returns
  -------
  M, but rotated 90 degrees counter-clockwise.
  '''

  # rotate 90 degrees counter-clockwise by transposing and reversing the columns
  transp = transpose(M)
  # reverses rows by using range method in reverse order: range(start,stop,step)
  return [ [transp[row][col] for col in range(len(transp[row]))] for row in range(len(transp)-1,-1,-1)]

def is_positive_semidefinite(M: "list[list]") -> bool:
  '''
  Parameters
  ----------
  - M: an arbitrary matrix

  Returns
  -------
  True if M is positive semi-definite, False otherwise

  '''
  
  #check if the matrix is equal to its transpose and if it's eigenvalues are all non-negative
  if(M == transpose(M)):
    eigenvalues, eigenvectors = np.linalg.eig(M)
    for eigenvalue in eigenvalues:
      if eigenvalue < 0:
        return False
    return True
  return False
