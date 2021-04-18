n = int(input())
dir1 = input().split()
dir2 = input().split()
dir3 = input().split()
dir4 = input().split()
waves = [dir1, dir2, dir3, dir4]
sumlist = [0, 0, 0, 0]

def popitem():
    for i in waves:
        i.pop(0)
    
def do_sum(x, ind):
    for i in x:
        sumlist[ind]+=int(i)
     
for i in range(0, 4):
        do_sum(waves[i], i)

def check_same():
    c = 0
    for i in range(1,4):
        if sumlist[0] == sumlist[i]:
            c += 1
    if c == 3:
        return True
    else:
        return False

for v in range(0, n):
    if check_same():
        print(sumlist[0])
        exit()
    else:
        for i in range(0,4):
            sumlist[i] -= int(waves[i][0]) 
        popitem()
        