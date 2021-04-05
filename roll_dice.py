''' importing random module '''
import random
res=[1,2,3,4,5,6]
list_all = []
def dice(X):
    '''Calling a function dice'''
    print(f'         {X[1]}       ')
    print('    +---------+')
    print('   /|        /|')
    print(f'  / |   {X[2]}   / |')
    print(' +--+------+  +')
    print(f'{X[5]}|  /      |  /',f'{X[0]}')
    print(f' | /   {X[4]}   | /')
    print(' |/        |/')
    print(' +---------+')
    print(f'    {X[3]}  ')
print('Initial position of dice')
dice(res)
sh = random.randint(0,5)
for i in range(sh):
    def random_1(res):
        '''To Roll'''
        res[1],res[2],res[3],res[4]=res[3],res[1],res[4],res[2]
    random_1(res)
    def random_2(res):
        '''To Random Roll'''
        res[0],res[1],res[4],res[5]=res[4],res[0],res[5],res[1]
    random_2(res)
print('After rolling....')
dice(res) 
def dice_down(down):
    '''To_roll_down_wards'''
    down[2],down[1],down[4],down[3]=down[1],down[3],down[2],down[4]
    dice(down)
    roll_dice = down.copy()
    list_all.append(roll_dice)
    print('down')
def dice_up(up):
    '''To roll up_wards'''
    up[1],up[2],up[4],up[3]=up[2],up[4],up[3],up[1]
    dice(up)
    roll_dice = up.copy()
    list_all.append(roll_dice)
    print('up')
def dice_left(left):
    '''To roll left_side'''
    left[0],left[1],left[5],left[4]=left[1],left[5],left[4],left[0]
    dice(left)
    roll_dice = left.copy()
    list_all.append(roll_dice)
    print('left')
def dice_right(right):
    '''To roll Right_side'''
    right[4],right[5],right[1],right[0]=right[5],right[1],right[0],right[4]
    dice(right)
    roll_dice = right.copy()
    list_all.append(roll_dice)
    print('right')
