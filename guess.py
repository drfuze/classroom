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

print '��Ϸ˵������1-100֮���������һ�������󶺶����£����Ի���ʾ�´��˻���С�ˡ������Ը������£��������С��������ͻ��˳������Ի��Զ�������Ϸ��¼����


print '���Ѿ�����%d�Σ�����%d�ֲ³��𰸣�ƽ��%.2f�ֲ³���'%(game_times,min_times,avg_times)

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
#��һ�������������С����С���͸�����С����
if game_times==0 or times<min_times:
    min_times=times
total_times+=times
game_times+=1
result='%d %d %d' %(game_times,min_times,total_times)

f=open('game.txt', 'w')
f.write(result)
f.close
