import copy

container=[0,0]
goal=[0,0]

def transferFromA(s):
    duplicate=copy.deepcopy(s)
    if(duplicate[1]<container[1]):
        a=container[1]-duplicate[1]
        a=min(a,duplicate[0])
        if(a>0):
            duplicate[1]+=a
            duplicate[0]-=a
    return duplicate

def transferFromB(s):
    duplicate=copy.deepcopy(s)
    if(duplicate[0]<container[0]):
        a=container[0]-duplicate[0]
        a=min(a,duplicate[1])
        if(a>0):
            duplicate[0]+=a
            duplicate[1]-=a
    return duplicate

def emptyA(s):
    duplicate=copy.deepcopy(s)
    duplicate[0]=0
    return duplicate

def emptyB(s):
    duplicate=copy.deepcopy(s)
    duplicate[1]=0
    return duplicate

def fillA(s):
    duplicate=copy.deepcopy(s)
    duplicate[0]=4
    return duplicate

def fillB(s):
    duplicate=copy.deepcopy(s)
    duplicate[1]=3
    return duplicate


def find(s):
    q=[]
    visited=[]
    q.append(s)
    while(len(q)):
        cur=q[0]
        print(cur)
        q.pop(0)

        if cur in visited:
            continue
        else:
            visited.append(cur)

        if(goal==cur):
            print("FOUND!!!")
            print(goal)
        for i in range(1,7):
            if(i==1):
                new=fillA(cur)
            
            if(i==2):    
                new=fillB(cur)

            if(i==3):
                new=transferFromA(cur)

            if(i==4):
                new=transferFromB(cur)

            if(i==5):
                new=emptyA(cur)

            if(i==6):
                new=emptyB(cur)
                
                
            if(goal==new):
                print("FOUND!!!")
                print(goal)
                return
            if (new not in visited):
                q.append(new)


if __name__=="__main__":
    container[0]=int(input('Enter max value of First container : '))
    container[1]=int(input('Enter max value of Second container : '))
    goal[0]=int(input('Enter required amount in First container : '))
    goal[1]=int(input('Enter required amount in Second container : '))
    s=[0,0]
    find(s)


    

