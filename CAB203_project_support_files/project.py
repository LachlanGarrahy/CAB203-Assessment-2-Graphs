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
   V = set(V for N in games for V in N)
   E = games.union(set((v,u) for u,v in games))
   for u in V:
      for v in V:
         if (graphs.distance(V,E,u,v) > 2): return False
   return True

def potentialReferees(refereecsvfilename, player1, player2):
   pass # Delete

def gameReferees(gamePotentialReferees):
   pass # Delete

def gameSchedule(assignedReferees):
   pass # Delete

def ranking(games):
   pass # Delete

