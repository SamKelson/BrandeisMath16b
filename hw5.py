import numpy as np

def is_stochastic(M: np.ndarray) -> bool:
  '''
  Parameters
  ----------
  - M: list of lists (numpy arrays)

  Returns
  -------
  bool

  Returns True if M is a left stochastic matrix, False otherwise
  '''
  #check if: M is square, entries are non-negative, and the sum of each column is 1
  return (M.shape[0] == M.shape[1]) and (np.all(M >= 0)) and (np.all(np.sum(M, axis=0) == 1))

def stationary_states(M: np.ndarray) -> "list[np.array]":
    '''
    Parameters
    ----------
    - M: list of lists (numpy arrays)
    
    Returns
    -------
    np.array
    
    Returns a list of the stationary states of M
    '''
    #find the eigenvalues and eigenvectors (these are the stationary states) of M
    eigenvalues, eigenvectors = np.linalg.eig(M)
    #get the eigenvectors corresponding to the eigenvalues of 1
    normed_stationary_states = [eigenvectors[:,i] for i in range(len(eigenvalues)) if np.isclose(eigenvalues[i], 1)]
    #because the eigenvectors are normalized they will not be a distribution so we need to "unormalize" them and make sure elements sum to one by multiplying by a constant
    stationary_states = [stationary_state / np.sum(stationary_state) for stationary_state in normed_stationary_states]
    return stationary_states

def probability_of_return(n: int) -> float:
    '''
    Parameters
    ----------
    - n: int
    
    Returns
    -------
    - float
    
    Returns the probability of returning to initial position after n random steps along a regular tetrahedron
    '''
    #create the transition matrix M for the regular tetrahedron with 4 vertices
    #the probability of moving from one vertex to another is 1/4 as we assume equal probability of moving to each vertex including staying on the same vertex
    M = 1/3*(np.ones((4,4)) - np.eye(4))

    #current state:
    state = np.array([1, 0, 0, 0])

    #return the probability of returning to state 1 after n steps
    return (np.linalg.matrix_power(M, n) @ state)[0]

    #as n goes to infinity the probability of returning to the initial state does not seem to go the stationary state [0.25,0.25,0.25,0.25] of the transition matrix which would normally be expected but is not guaranteed for all transition matrices

def matrix_to_dict(M: np.ndarray) -> dict:
    '''
    Parameters
    ----------
    - M: list of lists (numpy arrays)
    
    Returns
    -------
    - dict
    
    Returns a dictionary representation of the matrix M that represents a Markov chain
    '''
    #convert the matrix to a dictionary using a dictionary comprehension
    return {j: [(i,M[i][j]) for i in range(len(M))] for j in range(len(M[0]))}