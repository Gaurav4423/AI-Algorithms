import copy


def heuristic(s,g):
    cnt=0
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]!=g[i][j]):
                cnt+=1
    return cnt


def up(row,col,s):
    duplicate=copy.deepcopy(s)
    if(row-1>=0):
        duplicate[row][col]=duplicate[row-1][col]
        duplicate[row-1][col]=0
    return duplicate

def down(row,col,s):
    duplicate=copy.deepcopy(s)
    if(row+1<len(s)):
        duplicate[row][col]=duplicate[row+1][col]
        duplicate[row+1][col]=0
    return duplicate

def left(row,col,s):
    duplicate=copy.deepcopy(s)
    if(col-1>=0):
        duplicate[row][col]=duplicate[row][col-1]
        duplicate[row][col-1]=0
    return duplicate

def right(row,col,s):
    duplicate=copy.deepcopy(s)
    if(col+1<len(s[0])):
        duplicate[row][col]=duplicate[row][col+1]
        duplicate[row][col+1]=0
    return duplicate

def findIndex(x,s):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]== x):
                return (i,j)

def check(s,newState):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if(s[i][j]!=newState[i][j]):
                return False
    return True
            
def main():
    s=[[2,0,3],[1,8,4],[7,6,5]]
    g=[[1,2,3],[8,0,4],[7,6,5]]
    row,col=findIndex(0,s)
    print(row,col)
    
    
    q = []
    visited = []
    print(heuristic(s,g))
    q.append([heuristic(s,g),0,s])
    
#     print("HELOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    print(q[0][1])
    count=0
#     print(q)
    while(1):
        q.sort()
#         print("HIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
        cur=q[0][2]
        costToReach=q[0][1]
        q.pop(0)
        
        if cur in visited:
            continue
        else:
            visited.append(cur)
        
        if cur==s and count!=0:
            continue
        count+=1
        
        row,col=findIndex(0,cur)
        
        #up
        newState=up(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print(newState)
            break
        if (newState not in visited):
            q.append([heuristic(newState,g)+costToReach+1,costToReach+1,newState])
            
        #down
        newState=down(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print(newState)
            break
        if (newState not in visited):
            q.append([heuristic(newState,g)+costToReach+1,costToReach+1,newState])
        
        
        
        #left
        newState=left(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print(newState)
            break
        if (newState not in visited):
            q.append([heuristic(newState,g)+costToReach+1,costToReach+1,newState])
            
        
        #right
        newState=right(row,col,cur)
        if(g==newState):
            print("FOUND!!")
            print(newState)
            break
        if (newState not in visited):
            q.append([heuristic(newState,g)+costToReach+1,costToReach+1,newState])
#     print(s)
#     print(g)
    print("Number of times code executed : ",count+1)


if __name__=="__main__":
    main()
