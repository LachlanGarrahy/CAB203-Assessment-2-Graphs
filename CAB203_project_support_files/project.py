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
   V = set(V for N in games for V in N)

   # set edges as all games and the revers of all games
   E = games.union(set((v,u) for u,v in games))

   # find the distance between each player and return false if more than 2
   for u in V:
      for v in V:
         if (graphs.distance(V,E,u,v) > 2): return False
   return True

def potentialReferees(refereecsvfilename, player1, player2):
   V = set()
   E = set()
   U = set()
   S = {player1,player2}
   with open(refereecsvfilename, 'r') as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
         for v in row:
            V.add(v)
         u = row[0]
         U.add(u)
         for e in row[1:]:
            E.add((u,e))
   return U - digraphs.NS_in(V,E,S) - S

def gameReferees(gamePotentialReferees):
   N = gamePotentialReferees
   A = set(N.keys())
   B = {v for u in A for v in N[u]}
   E = {(u,v) for u in A for v in N[u]}
   R = {}

   MM = digraphs.maxMatching(A,B,E)

   for m in MM:
      if(m[0] not in B):R[m[0]] = m[1]

   if len(R) < len(N): R = None

   return R

def gameSchedule(assignedReferees):
   N = assignedReferees
   U = set(N.keys())
   V = {(u,v,N[(u,v)]) for u,v in U}
   E = set()
   R = []
   for u in V:
      for e in u:
         for t in V:
            if (e in t and t != u): E.add((t,u))
   C = graphs.minColouring(V,E)
   for i in range(C[0]):
      T = set()
      for e in C[1]:
         if(C[1][e] == i): T.add(e)
      R.append(T)
   return R
   

def ranking(games):
   V = set(V for N in games for V in N)
   return digraphs.topOrdering(V,games)

gameSchedule({ 
      ('Alice', 'Bob'): 'Rene', 
      ('Elaine', 'Charlie'): 'Dave',
      ('Rene', 'Elaine'): 'Alice',
      ('Dave', 'Bob'): 'Charlie'
   })