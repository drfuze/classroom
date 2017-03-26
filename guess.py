# -*- coding: cp936 -*-
from random import randint

f=file('game.txt')
score=f.read().split()
#print score
game_times=int(score[0])
min_times=int(score[1])
total_times=int(score[2])

if game_times>0:
    avg_times=float(total_times)/game_times
else:
    avg_times=0

print '游戏说明：从1-100之间随机产生一个数，大逗逗来猜，电脑会提示猜大了还是小了。如果不愿意继续猜，随便输入小于零的数就会退出。电脑会自动保存游戏记录。‘


print '你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(game_times,min_times,avg_times)

num=randint(1,100)
times=0
print 'Guess what I think?'
bingo=False
while bingo==False:
    times+=1
    answer=input()
    if answer<0:
        print 'you quit this game'
        break
    if answer<num:
        print 'too small'
    if answer>num:
        print 'too big'
    if answer==num:
        bingo=True
        print 'bingo!'
#第一次玩或轮数比最小轮数小，就更新最小轮数
if game_times==0 or times<min_times:
    min_times=times
total_times+=times
game_times+=1
result='%d %d %d' %(game_times,min_times,total_times)

f=open('game.txt', 'w')
f.write(result)
f.close
