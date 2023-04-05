import random
import copy
maxchou=9
lie=3
hangbei=3
ai=2
aihelp=0
sx=0
maxpoint=50
pointa=0
pointb=0
qipan=[['/' for i in range(maxchou+1)] for j in range(lie)]
qipancd=[]
def inp(x):
    while True:
        try:
            y=int(input())
            if y<=x and y>=1:
                break
            else:
                1/0
        except:
            print('输入错误，请重新输入')
    return y
def opqipan():
    for i in range(lie):
        print('第'+str(i+1)+'列',end=' ')
    for i in range(maxchou+1):
        print('')
        for j in range(lie):
            print(qipan[j][i],end='     ')
    print('')
def rujian(choose,rdnum):
    for i in range(maxchou+1):
        if qipan[choose-1][i] != '/':
            pass
        else:
            qipan[choose-1][i]=rdnum
            ruhang=i
            break
    pointup=0
    for i in range(maxchou+1):
        if qipan[choose-1][i] == rdnum:
            if i == ruhang:
                pass
            elif i<ruhang:
                for j in range(ruhang-i):
                    qipan[choose-1][i+j]='/'
                pointup+=(ruhang-i+1)
                break
            elif i>ruhang:
                for j in range(i-ruhang):
                    qipan[choose-1][ruhang+1+j]='/'
                pointup+=(i-ruhang+1+1)
                break
    for i in range(lie):
        if qipan[i][ruhang] == rdnum:
            if i == choose-1:
                pass
            elif i<choose-1:
                for j in range(choose-1-i):
                    qipan[i+j][ruhang]='/'
                pointup+=(choose-i)*hangbei
                break
            elif i>choose-1:
                for j in range(i+1-choose):
                    qipan[choose+j][ruhang]='/'
                pointup+=(i+2-choose)*hangbei
                break
    if pointup !=0:
        qipan[choose-1][ruhang]='/'
    return pointup
def sgthink():
    global qipan
    global qipancd
    qipancd=copy.deepcopy(qipan)
    pingfen=[]
    for i in range(lie):
        pingfena=[]
        for j in range(1,maxchou+1):
            pingfena.append(rujian(i+1,j))
            qipan=copy.deepcopy(qipancd)
        pingfen.append(sum(pingfena)/maxchou)
    choose=pingfen.index(max(pingfen))+1
    return choose
def aithink(ai):
    global qipan
    global qipancd
    if ai == 1:
        return random.randint(1,lie)
    elif ai == 2:
        return sgthink()
    elif ai == 3:
        qipancd2=copy.deepcopy(qipan)
        pingfen=[]
        for i in range(lie):
            pingfena=[0 for j in range(maxchou)]
            for j in range(1,maxchou+1):
                pingfena[j-1]+=rujian(i+1,j)
                pingfena[j-1]-=rujian(sgthink(),random.randint(1,maxchou))
                pingfena[j-1]+=rujian(sgthink(),random.randint(1,maxchou))
                qipan=copy.deepcopy(qipancd2)
            pingfen.append(sum(pingfena)/maxchou)
        choose=pingfen.index(max(pingfen))+1
        return choose
print('炸鱼游戏')
print('1:开始游戏 2:调整游戏设置')
a=inp(2)
if a == 2:
    print('你是否让选择让AI帮助你？1:是 2:否')
    if inp(2) == 1:
        print('你选择什么AI帮助你？1:傻逼 2:正常 3:高手')
        aihelp=inp(3)
    print('调整棋盘列数为(默认为3)')
    lie=inp(100)
    qipan=[['/' for i in range(maxchou+1)] for j in range(lie)]
    print('调整同行相同时的消除倍率为(默认为3)')
    hangbei=inp(1145141919810)
    print('调整AI智商为(默认为正常)1:傻逼 2:正常 3:高手 4:无AI')
    ai=inp(4)
    print('调整目标得分为')
    maxpoint=inp(1145141919810)
    print('调整抽取的最大数字为')
    maxchou=inp(1145141919810)
    qipan=[['/' for i in range(maxchou+1)] for j in range(lie)]
    print('调整完成，按回车键开始游戏')
    input()
sx=random.randint(0,1)
if sx==0:
    print('游戏开始,当前随机为AI先手')
else:
    print('游戏开始,当前随机为你先手')
    print('现在的棋盘状况为')
    opqipan()
while True:
    if sx == 1:
        if aihelp == 0:
            print('你选择在第几列摸鱼？')
            choose=inp(lie)
        else:
            choose=aithink(aihelp)
            print('AI帮你选择在第'+str(choose)+'列摸鱼')    
        rdnum=random.randint(1,maxchou)
        pointa+=rujian(choose,rdnum)
        print('你第'+str(choose)+'列抽到的数为'+str(rdnum))
        print('现在的棋盘状况为')
        opqipan()
        print('我方得分:'+str(pointa))
        print('AI得分:'+str(pointb))
        input('请按回车键继续')
        sx=0
    if sx == 0:
        choose=aithink(ai)
        rdnum=random.randint(1,maxchou)
        pointb+=rujian(choose,rdnum)
        print('AI选择在第'+str(choose)+'列摸鱼')
        print('AI第'+str(choose)+'列抽到的数为'+str(rdnum))
        print('现在的棋盘状况为')
        opqipan()
        print('我方得分:'+str(pointa))
        print('AI得分:'+str(pointb))
        input('请按回车键继续')
        sx=1
    if pointa >= maxpoint:
        print('游戏结束，你赢了')
        break
    if pointb >= maxpoint:
        print('游戏结束，AI赢了')
        break
input('请按回车键退出游戏')
