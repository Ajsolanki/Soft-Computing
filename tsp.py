import itertools as it

def gen_tsp_matrix(N):
    
    print("Enter cost between Cities (Enter None for no link):")
    
    cost_matrix = []
    for i in range(1, N+1):
        cost_matrix.append([])
        for j in range(1, N+1):
            if i==j:
                cost_matrix[i-1].append(None)
            else:
                try:
                    print("Enter cost between city "+str(i)+" and "+str(j)+": ")
                    cost = int(input())
                    cost_matrix[i-1].append(cost)
                except:
                    cost_matrix[i-1].append(None)
    return cost_matrix

#N = int(input("Enter Number of cities: "))    
#mat = gen_tsp_matrix(N)
N = 4
mat =[[None, 12,34,54],[32, None, 23,25],[65,34,None,2],[22,33,24,None]]
def gen_all_poss_path(N, start_city):
    paths = []
    temp_list = []
    for i in range(1,N+1):
        temp_list.append(i)
    all_comb = it.permutations(temp_list,N)
    for i in all_comb:
        if i[0] == start_city:
            paths.append(i)
    return paths
    
#print("Enter starting point")
#st = int(input())
st = 3
path = gen_all_poss_path(N,st)
final_paths = []
for i in range(len(path)):
    final_paths.append([])
    for j in range(len(path[i])):
        final_paths[i].append(path[i][j])
        
for i in range(len(final_paths)):
    final_paths[i].append(st)
    
    
cost_all = []
for i in range(len(final_paths)):
    temp_cost = 0
    for j in range(len(final_paths[i])-1):
        try:
            temp_cost += mat[final_paths[i][j]-1][final_paths[i][j+1]-1]
        except:
            None
    cost_all.append(temp_cost)
temp = cost_all[0]
temp_i = 0
best_path = None
for i in range(len(cost_all)):
    if cost_all[i] < temp:
        temp = cost_all[i]
        temp_i = i

best_path = final_paths[temp_i]
       
print(best_path)