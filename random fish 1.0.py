import random
import copy
maxchou=9 #抽数的上限
lie=3
hangbei=3
ai=1
sx=0 #顺序为1时为我方，为0时为AI
maxpoint=50
pointa=0
pointb=0
qipan=[['/' for i in range(maxchou+1)] for j in range(lie)]
qipancundang=[]
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
def jiancha(cd): #检查棋盘或其存档是否能得分,返回得分,cd代表将要执行操作的是对原棋盘还是虚拟棋盘,为''代表原棋盘，带'cundang'代表棋盘存档
    pointup=0
    for i in range(lie):
        for j in range(maxchou+1):
            if eval('qipan'+cd)[i][j] == '/':
                pass
            else:
                for k in range(maxchou-j):
                    if eval('qipan'+cd)[i][j] == eval('qipan'+cd)[i][j+k+1]:
                        pointup+=(k+2)
                        for l in range(k+2):
                            eval('qipan'+cd)[i][j+l]='/'
                        break
    for i in range(maxchou+1):
        for j in range(lie-1):
            if eval('qipan'+cd)[j][i] == '/':
                pass
            else:
                for k in range(lie-1-j):
                    if eval('qipan'+cd)[j][i] == eval('qipan'+cd)[j+k+1][i]:
                        pointup+=((k+2)*hangbei)
                        for l in range(k+2):
                            eval('qipan'+cd)[j+l][i]='/'
                        break
    return pointup
def choushu(choose,cd): #在第choose列抽数，choose从1计数，返回抽到的数
    rdnum=random.randint(1,maxchou)
    for i in range(maxchou+1):
        if eval('qipan'+cd)[choose-1][i] != '/':
            pass
        else:
            eval('qipan'+cd)[choose-1][i]=rdnum
            break
    return rdnum
def sgthink(xx):
    global qipancundang
    global qipan
    qipancundang=copy.deepcopy(qipan)
    pingfen=[]
    for i in range(lie):
        pingfena=[]
        for j in range(xx):
            choushu(i+1,'')
            pingfena.append(jiancha(''))
            qipan=copy.deepcopy(qipancundang)
        pingfen.append(sum(pingfena)/xx)
    choose=pingfen.index(max(pingfen))+1
    return choose
print('炸鱼游戏')
print('1:开始游戏 2：调整游戏设置')
a=inp(2)
if a == 2:
    print('调整棋盘列数为（默认为3）')
    lie=inp(100)
    qipan=[['/' for i in range(maxchou+1)] for j in range(lie)]
    print('调整同行相同时的消除倍率为（默认为3）')
    hangbei=inp(1145141919810)
    print('调整AI智商为（默认为傻逼）1：傻逼 2：正常 3：高手')
    ai=inp(3)
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
    if sx == 1 :
        print('你选择在第几列摸鱼？')
        choose=inp(lie)
        rdnum=choushu(choose,'')
        print('你第'+str(choose)+'列抽到的数为'+str(rdnum))
        pointa+=jiancha('')
        print('现在的棋盘状况为')
        opqipan()
        print('我方得分：'+str(pointa))
        print('AI得分：'+str(pointb))
        input('请按回车键继续')
        sx=0
    else:
        if ai == 1:
            choose=random.randint(1,lie)
            rdnum=choushu(choose,'')
            print('AI选择在第'+str(choose)+'列摸鱼')
            print('AI第'+str(choose)+'列抽到的数为'+str(rdnum))
            pointb+=jiancha('')
            print('现在的棋盘状况为')
            opqipan()
            print('我方得分：'+str(pointa))
            print('AI得分：'+str(pointb))
            input('请按回车键继续')
            sx=1
        if ai == 2:
            choose=sgthink(1000)
            rdnum=choushu(choose,'')
            print('AI选择在第'+str(choose)+'列摸鱼')
            print('AI第'+str(choose)+'列抽到的数为'+str(rdnum))
            pointb+=jiancha('')
            print('现在的棋盘状况为')
            opqipan()
            print('我方得分：'+str(pointa))
            print('AI得分：'+str(pointb))
            input('请按回车键继续')
            sx=1
        if ai == 3:
            qipancundang=copy.deepcopy(qipan)
            qipancundang2=copy.deepcopy(qipan)
            pingfen=[]
            for i in range(lie):
                pingfena=[0 for i in range(100)]
                for j in range(100):
                    choushu(i+1,'')
                    pingfena[i]+=jiancha('')
                    choushu(sgthink(20),'')
                    pingfena[i]-=jiancha('')
                    choushu(sgthink(20),'')
                    pingfena[i]+=jiancha('')
                    qipan=copy.deepcopy(qipancundang2)
                pingfen.append(sum(pingfena)/100)
            choose=pingfen.index(max(pingfen))+1
            rdnum=choushu(choose,'')
            print('AI选择在第'+str(choose)+'列摸鱼')
            print('AI第'+str(choose)+'列抽到的数为'+str(rdnum))
            pointb+=jiancha('')
            print('现在的棋盘状况为')
            opqipan()
            print('我方得分：'+str(pointa))
            print('AI得分：'+str(pointb))
            input('请按回车键继续')
            sx=1
    if pointa >= maxpoint:
        print('游戏结束，你赢了')
        break
    if pointb >= maxpoint:
        print('游戏结束，AI赢了')
        break
input('请按回车键退出游戏')
