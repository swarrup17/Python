adj_list={
    "1":["2","3","4"],
    "2":["5"],
    "3":["6","7"],
    "4":["8","9"],
    "5":[],
    "6":[],
    "7":[],
    "8":[],
    "9":[],
    }
closedlist={}
top=[]
for node in adj_list.keys():
    closedlist[node]="notvisited"
def dfs(stnode):
    closedlist[stnode]="visited"
    top.append(stnode)

    for v in adj_list[stnode]:
        if closedlist[v]!="visited":
            dfs(v)
stnode=input("enter the start node from where you want to traverse= ")
dfs(stnode)
print("traversed output = ",top)