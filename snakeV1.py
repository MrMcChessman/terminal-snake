

# strippas in paris


strippers = [29, 61, 21, 67, 81, 26, 23, 34, 45, 76, 34, 23, 76, 87, 41, 65, 34, 23, 12, 45, 65, 78, 89, 43, 12, 11, 11, 12, 17, 14, 12]



length = str(len(strippers)-1)
string = ('get age of input stripper number (n of '+length+' strippers) ==> ')
#boob = int(input(string))-1
boob = 28


#print(strippers[boob])
#print(min(strippers))

#print(strippers)


# Lists are mutable.  -  meaning you can update elements within lists.
# strings do not allow item assignments, and neither do tuples.

# negative values count from the top - the last item is index[-1], second from last is index[-2]

# "list index out of range" means you are trying to access a number too high,\
    # the list doesn't go that high.


# strippers.sort() sorts original list.

# sorted() creates a new list: y = sorted(strippers) for instance.




"""
#5x5 walkaround



x = 3
y = 3

a1 = ['_','_','_','_','_']
a2 = ['_','_','_','_','_']
a3 = ['_','_','X','_','_']
a4 = ['_','_','_','_','_']
a5 = ['_','_','_','_','_']


yfind = [a1,a2,a3,a4,a5]

def output_row(inp_list):
    return inp_list[0]+inp_list[1]+inp_list[2]+inp_list[3]+inp_list[4]


print(output_row(a1))
print(output_row(a2))
print(output_row(a3))
print(output_row(a4))
print(output_row(a5))

i = 5

while i < 10:
    
    #erase previous player position
    
    yfind[y-1][x-1] = '_'
    
    
    movement = input('enter wasd ==> ')
    
    
    yfind[y-1]
    
    if movement == 'w':
        y = y-1
    elif movement == 's':
        y = y+1
    elif movement == 'a':
        x = x-1
    elif movement == 'd':
        x = x+1 
    else:
        print('invalid key entry')
    
    #write new player position
    
    yfind[y-1][x-1] = 'X'
    
    print(output_row(a1))
    print(output_row(a2))
    print(output_row(a3))
    print(output_row(a4))
    print(output_row(a5))



"""



#more freedom tag game
"""
#define game arena
customize = input('Customize?(y/n) ==> ')

if customize == 'y':
    print('')
    
    width = int(input('Input Map Width ==> '))
    height = int(input('Input Map Height => '))
    print('')
    bc = input('Input Character for Background ==> ')
    
    sf = input('Sparse BG? (reccom.),(y/n) ======> ')
    if sf == 'n':
        bc = bc+bc
        
    else:
        bc = bc+' '
    
    pc = input('Input Player Character ==========> ')
    pc = pc+' '
    
    ec = input('Input Enemy Character ===========> ')
    ec = ec+' '
    
    
else:
    width = 30
    height = 15
    
    bc = '. '
    pc = 'O '
    ec = 'X '
    




#initiate player & enemy positions
x = int((2/3)*(width))
y = int((1/2)*(height))

ex = int((1/3)*(width))
ey = int((1/2)*(height))


i = 5

while i < 10:
    
#RENDER SCREEN
    row = 1
    while row < height+1:
        
        if row == y or row == ey:
            
            if y == ey:
                #protocol if both in same row
                if x < ex:
                    c1 = pc
                    c2 = ec
                else:
                    c1 = ec
                    c2 = pc
                
                
                
                #space1
                print((bc*((min(x,ex))-1)+c1+(bc*(abs(x-ex)-2))+c2+(bc*(width-(abs(x-ex)-2+min(x,ex))-1))))
               
                
            elif y == row:
                #protocol if x is only present
                print((bc*(x-1)+pc+(bc*(width-x))))
                
            elif ey == row:
                #protocol if ex only present
                print((bc*(ex-1)+ec+(bc*(width-ex))))
        
        else:
            print(bc*width)        
        
        row = row+1
    
    
    
    
    #SCENE MOTION
    #enemy motion
    #horizontal step
  
    #player motion
    movement = input('enter wasd ==> ')    
#    movement = movement+(' '*(width+height))
#    movement = movement[0]+movement[1]+movement[2]
    
    y = y-(movement.count('w'))
    y = y+(movement.count('s'))
    
    x = x-(movement.count('a'))
    x = x+(movement.count('d'))
    

  
    
  
    if abs(ex-x) > abs(ey-y):

        if ex < x:
            ex = ex+1
        elif ex > x:
            ex = ex-1
        else:
            ex = ex
    
    else:
        
        #vertical step
        if ey < y:
            ey = ey+1
        elif ey > y:
            ey = ey-1
        else:
            ey = ey
        
    






    #hard walls

    if y > height:
        y = height
        
    if y < 1:
        y = 1
        
    if x > width+1:
        x = width+1
        
    if x < 1:
        x = 1

    
    #edge kills

    if y > height or y < 1 or x > width or x < 1:
        i = 15
        print('\nOut of Bounds\n--Game Over--')
"""
    








# worm game?



# display a constant 20(40char) x 10

# a score - apples eaten (high score 200)

# rows of lists storing values

# the head moves around and leaves a trail of 'increases' to the stored "array"\
    # in relation to 'score'.
    # everything on the board decreases by 1 until equaling zero. (no neg)
    
# simple if function runs for each 'cell' determining whether to display a value;
# actually could probably 



import random

#IMPORTANT CUSTOMIZATION:
    # length of r1 and of a used to determine frame size.
    # more useful customization found within functions.

r1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r2 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r3 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r4 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r6 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r7 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r8 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r9 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
r10 =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

a = [r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]

x = len(r1)//2
y = len(a)//2

ax = len(r1)//3
ay = len(a)//3

score = 5


# two characters; rec one as space.
def display(num):
    
    #Snake (head->tail)
    if num == -5:
        out = '8 '
    elif num > int((2/3)*(score)):
        out = '0 '
    elif num > int((1/3)*(score)):
        out = 'O '
    elif num > 0:
        out = 'o '
        
    #Apple
    elif num == -3:
        out = 'A '
        
    #Background
    else:
        out = '. '
        
    return out

def decay(num):
    if num > 0:
        num = num-1
    elif num == -5:
        num = score
    return num







g = 5
while g < len(a):
    
    #PRINT DISPLAY
    a[ay][ax] = -3
    a[y][x] = -5
    
    #row
    i = 0
    while i < len(a):
        print('')
        #column
        j = 0
        while j < len(r1):
            print(display(a[i][j]),end='')
            a[i][j] = decay(a[i][j])
            j = j+1
    
        i = i+1
    print('Score:',score)
    
    
    
    
    #MOVE CHARACTER
    movement = input('enter wasd ==> ')
    if movement.count('w') == 0 and movement.count('a') == 0 and movement.count('s') == 0 and movement.count('d') == 0:
        while movement.count('w') == 0 and movement.count('a') == 0 and movement.count('s') == 0 and movement.count('d') == 0:
            movement = input('wasd ==> ')
        
    
    movement = movement+' '
    movement = movement[0]
    
    y = y-(movement.count('w'))
    y = y+(movement.count('s'))
    
    x = x-(movement.count('a'))
    x = x+(movement.count('d'))
    
    #hard walls
    
    if y > 9:
        g = 15
        
    elif y < 0:
        g = 15
        
    elif x > 20:
        g = 15
        
    elif x < 0:
        g = 15

   #check self
    elif a[y][x] > 0:
       g = 16

    
    #Check for Apple
    elif x == ax and y == ay:
        score = score + 1
        ax = random.randint(0,len(r1)-1)
        ay = random.randint(0,len(a)-1)
        
        while a[ay][ax] > 0 or a[ay][ax] < -1:
            ax = random.randint(0,len(r1)-1)
            ay = random.randint(0,len(a)-1)
        
    
    #if apple eaten, spawn a new one
    
    
    
    #SET ARRAY
    if g < 10:
        a[y][x] = score
    

print('\n --GAME OVER--')
if g == 15:
    print("(wall collision)\n")
elif g == 16:
    print("(self-collision)\n")
else:
    print('lol')
"""



rows = 10
cols = 5

emptyList = [0]

a = []

# populate columns
icols = 1
while icols < cols+1:    
    a.append(emptyList)
    icols = icols+1

#print(a)

#populate rows
irows = 1
while irows < rows+1-1:
    a[0].append(0)
    irows = irows+1


#print(a)


"""

























