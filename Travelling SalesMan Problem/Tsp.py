import copy
class TSP:
    def __init__(self,thismap,startcity):
        TSP.map=thismap
        self.start=startcity
        self.current=startcity
        self.previousState=None
        self.cost=0;
        self.visitedList=[]
        self.visitedList.append(self.current)

    

    def isGoalReached(self):
        if len(TSP.map)+1 ==len(self.visitedList):
            return True
        else:
            return False

    def __eq__(self,other):
        return self.visitedList == other.visitedList

    def __lt__(self,other):
        return self.cost < other.cost

    def __gt__(self,other):
        return self.cost > other.cost 

    def move(self,city):
        if len(self.visitedList) ==len(TSP.map[0]):
            prevState=copy.deepcopy(self)
            self.cost=self.cost+ TSP.map[self.current][self.start]
            self.current =self.start
            self.visitedList.append(self.start)
            return True
        elif city!=self.current and city not in self.visitedList:
                prevState=copy.deepcopy(self)
                print("Moving from city:",self.current,"to",city)
                self.cost=self.cost + TSP.map[self.current][city]
                self.current=city
                self.visitedList.append(city)
                return True
                   
        else:
            print("Already visited:",city)
            return False
        
    def displayState(self):
        print("---------------------")
        print("Current City:",self.current,"Cost:",self.cost)
        print("Visited Cities",self.visitedList)
        print("---------------------")
        
    def PropagateImprovement(self):
        pass
    
    def PossibleNextStates(self):
        stateList=[]
        for i in range(0,len(TSP.map[0])):
            state=copy.deepcopy(self)
            if state.move(i):
                stateList.append(state)
        return stateList


    def constructPath(gstate):
        print("The Solution Path from Goal to Start")
        while gstate is not None:
            gstate.displayState()
            gstate=gstate.previousState   
    
    def goalachieved(self):
        if len(TSP.map[0])+1==len(self.visitedList):
            return True
        else:
            return False

open=[]
closed=[]


def UCS(startState):
    open.append(startState)
    while open:
        print(len(open),len(closed))
        thisState=open.pop(0)
        thisState.displayState()
        if thisState not in closed:
            closed.append(thisState)
            if thisState.isGoalReached():
                print("Goal State Found.. Stopping Search")
                thisState.displayState()
                #constructPath(thisState)
                break
            nextStates=thisState.PossibleNextStates()
            for eachstate in nextStates:
                if eachstate not in closed and eachstate not in open:
                    open.append(eachstate)
                    

map=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
start=int(input("enter the start city"))
problem=TSP(map,start)
UCS(problem)              