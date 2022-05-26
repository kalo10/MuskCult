def alter_stack(command, n):
    ID = ""
    top = 0
    stack = [0]*100
    for i in range(n):
        ID = ""
        if command[i][0] == 'A':
            top += 1
            for j in range(9, len(command[i])):
                ID = ID + command[i][j]
            ID = int(ID)
            stack[top] = ID
            
        elif command[i] == "Check":
            if top <= 0:
                print("Invalid")
                top = 0
            else: 
                print(stack[top])
                
        
        elif command[i] == "PickPlate":
            top -= 1
            if top < 0:
                print("Invalid")
                top = 0

n = int(input())
command = [0]*100
top = 0
for i in range(n):
    command[i] = input()
alter_stack(command, n)
print(n)
