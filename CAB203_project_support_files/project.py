import graphs
import digraphs
import csv

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
   # set inital variables
   V = set()
   E = set()
   U = set()
   S = {player1,player2}

   #opens the CSV
   with open(refereecsvfilename, 'r') as file:
      csvreader = csv.reader(file)
      next(csvreader)
      for row in csvreader:
         # adds the verticies as all entries in the CSV
         for v in row:
            V.add(v)
         # makes U the referees
         u = row[0]
         U.add(u)
         # gets all the edges as the referees and the people they conflict with
         for e in row[1:]:
            E.add((u,e))
   
   # returns the referees that dont have conflicts with the players
   return U - digraphs.NS_in(V,E,S) - S

def gameReferees(gamePotentialReferees):
   # set initial variables
   N = gamePotentialReferees
   # sets A as the players
   A = set(N.keys())
   # sets B as the potential referees
   B = {v for u in A for v in N[u]}
   # sets the edges to the games and potential referees
   E = {(u,v) for u in A for v in N[u]}
   R = {}

   # returns the max matching from A,B and E
   MM = digraphs.maxMatching(A,B,E)

   # checks if the first entry in the returned tuple is a game and adds it to the dictionary R
   for m in MM:
      if(m[0] not in B):R[m[0]] = m[1]

   # sets R to none if there are no entries
   if len(R) < len(N): R = None

   return R

def gameSchedule(assignedReferees):
   # sets initial variables
   N = assignedReferees
   # sets the verticies to a triple of the players and the referee for each game
   V = {(u,v,N[(u,v)]) for u,v in N.keys()}
   E = set()
   R = []

   # sets the edges to the games that share a person
   for u in V:
      for e in u:
         for t in V:
            if (e in t and t != u): E.add((t,u))

   # gets the colouring of the graph
   C = graphs.minColouring(V,E)

   # adds sets of triples to the list R in their order according to the colouring
   for i in range(C[0]):
      T = set()
      for e in C[1]:
         if(C[1][e] == i): T.add(e)
      R.append(T)

   return R
   

def ranking(games):
   # sets the verticies to each player
   V = set(V for N in games for V in N)

   # returns the topological ordering of the players with games being the edges
   return digraphs.topOrdering(V,games)