def all_possibility(current, size):
    all_list = []
    
    for i in range(len(current)):
        new_node = [current[0], current[1], current[2]] 
        new_node[i] = 0
        all_list.append(new_node)

        
    for i in range(len(current)):
        
        capacity = size[i] - current[i]
        for j in range(len(current)):
            if i != j:
                new_node = [current[0], current[1], current[2]]
                new_node[i] += new_node[j]
                new_node[j] -= capacity
                
                if new_node[i] > size[i]:
                    new_node[i] = size[i]
                if new_node[j] < 0:
                    new_node[j] = 0
                
                if new_node != current:
                    all_list.append(new_node)
                
                
    return all_list

def copy_history(node, history):
    new_node = []
    
    for i in range(len(history)):
        new_node.append(history[i])
        
    new_node.append(node)
    
    return new_node

def allready_exists(node, qeue):
    
    found = False
    count = 0
    while count < len(qeue):
        last = len(qeue[count]) - 1
        if qeue[count][last] == node:
            found = True
        count += 1
    
        
    return found

def total_amount(node):
    num = 0
    for i in range(len(node)):
        num += node[i]
        
    return num

def jugs(jugsize1, jugsize2, jugsize3, endstate1, endstate2, endstate3):
    start = [jugsize1, jugsize2, jugsize3]
    size = [jugsize1, jugsize2, jugsize3]
    end = [endstate1, endstate2, endstate3]
    algorithm="bfs"
    
    # if bfs algorithm is being tested
    if algorithm == "bfs":
        qeue = []
        qeue.append([start])
        found = False
        if start == end:
            found = True
            
            
        #this loop searhes for the desired state
        index = 0
        while index < len(qeue) and found == False:
            # checks all possible states and appends to the qeue
            last = len(qeue[index]) - 1
            new_nodes = all_possibility(qeue[index][last], size)

            for i in range(len(new_nodes)):
                if found == False:
                    if allready_exists(new_nodes[i], qeue) == False and total_amount(new_nodes[i]) >= total_amount(end):
                        node = copy_history(new_nodes[i], qeue[index])
                        qeue.append(node)
                        # checks if the end has been reached
                        if new_nodes[i] == end:
                            found = True
            index += 1
        
        
        # if found print the solution
        if found:
            answer = qeue[len(qeue)-1]
            for i in range(len(answer)):
                print(answer[i][0],answer[i][1],answer[i][2])
                
        else:
            print("no solution found")
            

jugs_ = [12,8,5]
end_state = [6,6,0]

print("BFS:")
jugs(jugs_[0], jugs_[1] , jugs_[2] , end_state[0], end_state[1], end_state[2])