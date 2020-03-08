
from pyevolve import G1DList, GSimpleGA, Consts

sudoku=[
0,0,6,0,0,0,0,0,0,
0,8,0,0,5,4,2,0,0,
0,4,0,0,9,0,0,7,0,
0,0,7,9,0,0,3,0,0,
0,0,0,0,8,0,4,0,0,
6,0,0,0,0,0,1,0,0,
2,0,3,0,6,7,9,8,1,
0,0,0,5,0,0,0,4,0,
4,7,8,3,1,9,5,6,2]



def row(sd,rijnum):
    #function that returs a list consisting of row
    row=[]
    for index in range(9):
        row.append(sd[rijnum*9+index])
    return row
 
def column(sd, columnnum):
    #returns column
    column=[]
    for index in range(9):
        column.append(sd[index*9+columnnum])
    return column
 
def block(sd,blocknum):
    #returns block numbered form left to right and then down
    block=[]
    blockstart=int(blocknum/3)*9*3+(blocknum-int(blocknum/3)*3)*3
    for indexX in range(3):
        for indexY in range(3):
            block.append(sd[blockstart+indexX*9+indexY])
    return block
 
def errors(sdsol):
    #this is the fitness function. No errors means the solution
    err=0
    for index in range (9):
        for element in [row(sdsol,index),column(sdsol,index),block(sdsol,index)]:
            for getal in [1,2,3,4,5,6,7,8,9]:
                # check on double numbers
                if (element.count(getal))>1:
                    err+=element.count(getal)-1
 
    for i,getal in enumerate(sdsol):
        # check on numbers that don't match the startnumbners
        if getal!=sudoku[i] and sudoku[i]!=0:
            err+=2
    return err




genome = G1DList.G1DList(81) #defining the genome as a list of 81 integers
genome.setParams(rangemin=1,rangemax=9)
genome.evaluator.set(errors) #sets fitness function to errors
genome.setParams(bestrawscore=0.00, rounddecimal=2)
ga = GSimpleGA.GSimpleGA(genome)
ga.setMinimax(Consts.minimaxType["minimize"]) #0 errors wanted
ga.setMutationRate(0.06)
ga.setGenerations(10000)
ga.setPopulationSize(200)
ga.setCrossoverRate(1.0)
ga.setElitismReplacement(5)
ga.terminationCriteria.set(GSimpleGA.RawScoreCriteria)
ga.evolve(freq_stats=10)
 
print (ga.bestIndividual())
