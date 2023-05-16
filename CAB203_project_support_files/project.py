import graphs
import digraphs
import csv

# Make sure that you implement all of the following functions
# Run the test suit like:
# python test_project.py
# or
# python3 test_project.py
# 
# you can install pytest with
# pip install pytest 
# Then you can run
# pytest test_project.py

def gamesOK(games):
   # set verticies as all distinct players in games
   V = getVerticiesFromList(games)
   # set edges as all games and the revers of all games
   E = getEdgesFromList(games)
   # find the distance between each player and return false if more than 2
   for u in V:
      for v in V:
         if (graphs.distance(V,E,u,v) > 2): return False
   return True

def potentialReferees(refereecsvfilename, player1, player2):
   R = set()
   with open(refereecsvfilename, 'r') as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
         if( not ((player1 in row) | (player2 in row))): R.add(row[0])
   return R

def gameReferees(gamePotentialReferees):
   pass # Delete

def gameSchedule(assignedReferees):
   pass # Delete

def ranking(games):
   pass # Delete

def getVerticiesFromList(list):
   return set(V for N in list for V in N)

def getEdgesFromList(list):
   return list.union(set((v,u) for u,v in list))