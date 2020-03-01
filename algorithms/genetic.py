# can i use libraries?
# https://studiohouthaak.nl/solving-a-sudoku-with-a-genetic-algorithm/

'''
from optopus import ga, stdgenomes
 
#Now we choose a representation. We know that the answer to the puzzle must be some permutation of the digits 1 to 9, each used nine times.
 
init_vect = sum([range(1,10)] * 9, []) # A vector of 81 elements
genome = stdgenomes.PermutateGenome (init_vect)
 
#I made a few functions to calculate how many conflicts a potential Sudoku solution has. I'll show them later, but for now let us just import the package. I also found a puzzle somewhere and put it in the PUZZLE constant.
 
import sudoku
solver = ga.GA(sudoku.ga_sudoku(sudoku.PUZZLE) , genome)
 
#And now, when we have supplied the GA with a fitness function (ga_sudoku, which counts Sudoku conflicts) and a representation (genome), let us just let the solver do its magic.
 
solver.evolve(target_fitness=0)





DIM = 9
 
def one_box(solution, i):
    """Extract the 9 elements of a 3 x 3 box in a 9 x 9 Sudoku solution."""
    return solution[i:i+3] + solution[i+9:i+12] + solution[i+18:i+21]
 
def boxes(solution):
    """Divide a flat vector into vectors with 9 elements, representing 3 x 3
    boxes in the corresponding 9 x 9 2D vector. These are the standard
    Sudoku boxes."""
    return [one_box(solution, i) for i in [0, 3, 6, 27, 30, 33, 54, 57, 60]]
 
def splitup(solution):
    """Take a flat vector and make it 2D"""
    return [solution[i * DIM:(i + 1) * DIM] for i in xrange(DIM)]

def consistent(solution):
    """Check how many different elements there are in each row.
    Ideally there should be DIM different elements, if there are no duplicates."""
    return sum(DIM - len(set(row)) for row in solution)
 
def compare(xs1, xs2):
    """Compare two flat vectors and return how much they differ"""
    return sum(1 if x1 and x1 != x2 else 0 for x1, x2 in zip(xs1, xs2))
 
def sudoku_fitness(flatsolution, puzzle, flatpuzzle=None):
    """Evaluate the fitness of flatsolution."""
    if not flatpuzzle:
        flatpuzzle = sum(puzzle, [])
    solution = splitup(flatsolution)
    fitness = consistent(solution) #check rows
    fitness += consistent(zip(*solution)) #check columns
    fitness += consistent(boxes(flatsolution)) #check boxes
    fitness += compare(flatpuzzle, flatsolution) * 10 #check that it matches the known digits
    return fitness
 
def ga_sudoku(puzzle):
    """Return a fitness function wrapper that extracts the .genes attribute from
    an individual and sends it to sudoku_fitness."""
    flatpuzzle = sum(puzzle, []) #just a precalcing optimization
    def fit(guy):
        return sudoku_fitness(guy.genes, puzzle, flatpuzzle)
    return fit
'''