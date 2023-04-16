import random
import copy
import numpy
class qipans:
    def __init__(self,group,maxnum,line_rate,maxpoint,pointa,pointb):
        self.group=group
        self.maxnum=maxnum
        self.line_rate=line_rate
        self.maxpoint=maxpoint
        self.pointa=pointa
        self.pointb=pointb
        self.qipan=[['/' for i in range(maxnum+1)] for j in range(group)]
    def print_qipan(self):
        for i in range(self.group):
            if i == 0:
                print('| ',end='')
            print('Group%d'%(i+1),end=' | ')
        for i in range(self.maxnum+1):
            print('')
            for j in range(self.group):
                if j == 0:
                    print('|    ',end='')
                print(self.qipan[j][i],end=(''.join([' ' for k in range(2+len(str(j+1)))])+'|'+'    '))
        print('')
    def rujian(self,choose_group,get_num):
        for i in range(self.maxnum+1):
            if self.qipan[choose_group-1][i] == '/':
                self.qipan[choose_group-1][i]=get_num
                real_line=i
                break
        pointup=0
        for i in range(self.maxnum+1): #对单列进行检查
            if self.qipan[choose_group-1][i] == get_num and i != real_line:
                if i<real_line:
                    for j in range(real_line-i):
                        self.qipan[choose_group-1][i+j]='/'
                    pointup+=(real_line-i+1)
                    break
                else:
                    for j in range(i-real_line):
                        self.qipan[choose_group-1][real_line+1+j]='/'
                    pointup+=(i-real_line+1)
                    break
        for i in range(self.group): #对单行进行检查
            if self.qipan[i][real_line] == get_num and i != choose_group-1:
                if i<choose_group-1:
                    for j in range(choose_group-1-i):
                        self.qipan[i+j][real_line]='/'
                    pointup+=(choose_group-i)*self.line_rate
                    break
                else:
                    for j in range(i+1-choose_group):
                        self.qipan[choose_group+j][real_line]='/'
                    pointup+=(i+2-choose_group)*self.line_rate
        if pointup != 0:
            self.qipan[choose_group-1][real_line]='/'
        return pointup
    def aithink(self,ai_mode,self_point,others_point):
        if ai_mode == 0:
            print('你选择在第几列炸鱼？')
            choose_group=inp(self.group)
            return choose_group
        else:
            if ai_mode == 1:
                choose_group=random.randint(1,self.group)
            elif ai_mode == 2:
                all_point=[]
                for i in range(self.group):
                    single_point=[]
                    for j in range(1,self.maxnum+1):
                        all_qipans.append(copy.deepcopy(all_qipans[-1]))
                        single_point.append(all_qipans[-1].rujian(i+1,j))
                        all_qipans.pop(-1)
                    all_point.append(numpy.mean(single_point))
                choose_group=all_point.index(max(all_point))+1
            elif ai_mode == 3:
                all_point=[]
                all_pointup=[]
                all_pointdown=[]
                for i in range(self.group):
                    single_point=[]
                    for j in range(1,self.maxnum+1):
                        all_qipans.append(copy.deepcopy(all_qipans[-1]))
                        single_point.append(all_qipans[-1].rujian(i+1,j))
                        all_qipans.pop(-1)
                    avg=numpy.mean(single_point)
                    std=numpy.std(single_point)
                    all_point.append(avg)
                    all_pointup.append(min(avg+std,max(single_point)))
                    all_pointdown.append(max(avg-std,min(single_point)))
                if self_point>others_point:
                    if (self_point-others_point)>self.maxpoint/4 or self_point>self.maxpoint*0.9:
                        choose_group=all_pointdown.index(max(all_pointdown))+1
                    else:
                        choose_group=all_point.index(max(all_point))+1
                elif self_point<others_point:
                    if (others_point-self_point)>self.maxpoint/4 or others_point>self.maxpoint*0.9:
                        choose_group=all_pointup.index(max(all_pointup))+1
                    else:
                        choose_group=all_point.index(max(all_point))+1
                else:
                    choose_group=all_point.index(max(all_point))+1
            print('AI选择在第%d列炸鱼'%choose_group)
            return choose_group
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

all_qipans=[]
sxmeans=[{True:'你',False:'AI'},{True:'ai_help',False:'ai_mode'},{True:'all_qipans[-1].pointa',False:'all_qipans[-1].pointb'}]
while True:
    print('炸鱼游戏(random fish)1.2')
    print('1:开始游戏 2:调整游戏设置')
    choose=inp(2)
    if choose == 1:
        all_qipans.append(qipans(3,9,3,50,0,0))
        ai_mode=2
        ai_help=0
    else:
        print('你是否让选择让AI帮助你？1:是 2:否')
        if inp(2) == 1:
            print('你选择什么AI帮助你？1:傻逼 2:正常 3:高手(默认为正常)')
            ai_help=inp(3)
        else:
            ai_help=0
        print('调整棋盘列数为(默认为3)')
        group=inp(99)
        print('调整同行相同时的消除倍率为(默认为3)')
        line_rate=inp(114514)
        print('调整AI智商为(默认为正常)1:傻逼 2:正常 3:高手 4:无AI')
        ai_mode=inp(4)
        print('调整目标得分为(默认为50)')
        maxpoint=inp(1145141919810)
        print('调整抽取的最大数字为(默认为9)')
        maxnum=inp(99)
        all_qipans.append(qipans(group,maxnum,line_rate,maxpoint,0,0))
        print('调整完成，按回车键开始游戏')
        input()
    sx=random.choice([True,False])
    print('游戏开始，本局游戏随机由'+sxmeans[0][sx]+'先手')
    all_qipans[-1].print_qipan()
    while True:
        choose_group=all_qipans[-1].aithink(eval(sxmeans[1][sx]),eval(sxmeans[2][sx]),eval(sxmeans[2][not sx]))
        get_num=random.randint(1,all_qipans[-1].maxnum)
        exec(sxmeans[2][sx]+'+=all_qipans[-1].rujian(choose_group,get_num)')
        print(sxmeans[0][sx]+'第%d列抽到的数为%d'%(choose_group,get_num))
        print('现在的棋盘状况为')
        all_qipans[-1].print_qipan()
        print('我方得分:%d\nAI得分:%d'%(all_qipans[-1].pointa,all_qipans[-1].pointb))
        input('请按回车键继续')
        sx=not sx
        if all_qipans[-1].pointa >= all_qipans[-1].maxpoint or all_qipans[-1].pointb >= all_qipans[-1].maxpoint:
            print('游戏结束,'+sxmeans[0][not sx]+'赢了')
            if sx and all_qipans[-1].pointb-all_qipans[-1].pointa<=all_qipans[-1].maxpoint/10:
                print('太可惜了,你差一点就赢了,你现在有一次复活机会，你想使用吗？(放弃请直接按回车键，使用请按其他任意键再按回车键)')
                if input() != '':
                    all_qipans[-1].maxpoint+=50
                    print('已将目标得分调高50,尝试反超吧！')
                    continue
            break
    print('是否开始新一轮游戏？1:重新开始,2：退出游戏')
    choose=inp(3)
    if choose == 2:
        break
