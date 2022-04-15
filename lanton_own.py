import numpy as np
import turtle

step = 10

def clk_draw():
    for i in range(4):
        turtle.forward(step)
        turtle.left(90)

def anti_clk_draw():
    for i in range(4):
        turtle.forward(step)
        turtle.right(90)

def draw_square(forward):
    if forward == 'd':
        clk_draw()
    if forward == 'w':
        anti_clk_draw()
    if forward == 'a':
        turtle.right(180)
        clk_draw()
        turtle.right(180)
    if forward == 's':
        turtle.right(180)
        anti_clk_draw()
        turtle.right(180)


def arr_move(forward, pos_i, pos_j):
    if forward == 'd':
        pos_i += 1
    elif forward == 'w':
        pos_j -= 1
    elif forward == 'a':
        pos_i -= 1
    elif forward == 's':
        pos_j += 1
    return pos_i, pos_j
if __name__ == '__main__':
    width = 200
    height = 200
    arr_virtual = np.ones((width, height)) #设定1是白格，数组中每个节点 作为每个方格的 左下角， 也就是该点的东北间隔就是方块
    pos_status_list = ['d', 'w', 'a', 's'] #这里先从d开始，是因为海龟的开始朝向就是向右，这个list是海龟的朝向索引列表
    count = 0
    pos_status = 0
    forward = pos_status_list[pos_status] #forward就是海龟的朝向
    pos_i = width // 2
    pos_j = height // 2
    # print (pos_i)
    # print (pos_j)
    turtle.speed(0)
    while pos_j < height and pos_i < width:
        if arr_virtual[pos_i][pos_j] == 1 :  #设定 1 代表白色
            turtle.color('white', 'black')
            arr_virtual[pos_i][pos_j] = 0  #设置成黑色 0
            turtle.begin_fill() #这里是开始填充方格的颜色， 前面color(argv1, argv2),第二个参数就是填充的颜色，第一个是画笔的线的颜色
            # print ('pos ( %d, %d ) , posstatus:%d to: %s '%(pos_i, pos_j, pos_status, str(turtle.heading())))
            draw_square(forward) #这里根据海龟的朝向不同， 画的格子的位置也不同
            turtle.end_fill()
            turtle.left(90) #兰顿蚂蚁 在白格 左转90度，前进一步
            turtle.forward(step)
            pos_status = (pos_status + 1) % 4 #这个left就是逆时针，对应list的逆时针顺序
            forward = pos_status_list[pos_status]
            pos_i, pos_j = arr_move(forward, pos_i, pos_j) #这里是数组中坐标的位置变化，因为从原始点到目标点，因为左转和右转的区别，有两种可能，但是对于目标点来说， 只有一种可能，就是所有节点的目的都是目标点
            #所以， 逆时针和顺时针到目标点，所做的动作也是一样的, 比如目标点是w，那么逆时针d->w,操作就是j-1, 顺时针a->w, 操作就是j-1,两个操作都是一样的
            #      i   i+1  i+2
            #j          w
            #j+1    a       d
            #j+2        s
            # print ('pos ( %d, %d ) , posstatus:%d to: %s '%(pos_i, pos_j, pos_status, str(turtle.heading())))
        else :
            turtle.color('white', 'white')
            arr_virtual[pos_i][pos_j] = 1
            turtle.begin_fill()
            # print ('---pos ( %d, %d ) , posstatus:%d to: %s '%(pos_i, pos_j, pos_status, str(turtle.heading())))
            draw_square(forward)

            turtle.end_fill()
            turtle.right(90)
            turtle.forward(step)
            pos_status = (pos_status - 1) % 4
            forward = pos_status_list[pos_status]
            pos_i, pos_j = arr_move(forward, pos_i, pos_j)
            # print ('---pos ( %d, %d ) , posstatus:%d to: %s '%(pos_i, pos_j, pos_status, str(turtle.heading())))
        count += 1
        print (count)

