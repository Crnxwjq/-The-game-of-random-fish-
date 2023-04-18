from random import randint as rd
from random import choice as choice
import copy
#开始定义全局重要变量
all_games=[]
sxmeans=[{True:'你',False:'AI'},{True:'ai_help',False:'ai_mode'},
         {True:'all_games[-1].pointa',False:'all_games[-1].pointb'},
         {True:'all_games[-1].stepa',False:'all_games[-1].stepb'},
         {True:'awin_times',False:'bwin_times'}]
print_switch = True
def print_if(what,end_if,switch):
    if switch:
        if end_if == None:
            print(what)
        else:
            print(what,end=end_if)
def inp(x):
    try:
        y=int(input())
        if x == None and y>=1:
            return y
        elif y<=x and y>=1:
            return y
        else:
            raise Exception()
    except:
        print('输入错误，请重新输入')
        return inp(x)
def median(lst):
    lst.sort()
    n=len(lst)
    if n%2 == 0:
        return (lst[n//2-1]+lst[n//2])/2
    else:
        return lst [n//2]
class games:
    def __init__(self,group,maxnum,line_rate,maxpoint,pointa,pointb,stepa,stepb):
        self.group=group
        self.maxnum=maxnum
        self.line_rate=line_rate
        self.maxpoint=maxpoint
        self.pointa=pointa
        self.pointb=pointb
        self.stepa=stepa
        self.stepb=stepb
        self.qipan=[['/' for i in range(maxnum+1)] for j in range(group)]
    def print_qipan(self):
        for i in range(self.group):
            if i == 0:
                print_if('| ','',print_switch)
            print_if('Group%d'%(i+1),' | ',print_switch)
        for i in range(self.maxnum+1):
            print_if('',None,print_switch)
            for j in range(self.group):
                if j == 0:
                    print_if('|    ','',print_switch)
                print_if(self.qipan[j][i],(''.join([' ' for k in range(2+len(str(j+1)))])+'|'+'    '),print_switch)
        print_if('',None,print_switch)
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
            print_if('你选择在第几列炸鱼？',None,print_switch)
            choose_group=inp(self.group)
            return choose_group
        else:
            if ai_mode == 1:
                choose_group=rd(1,self.group)
            elif ai_mode == 2:
                all_point=[]
                for i in range(self.group):
                    single_point=[]
                    for j in range(1,self.maxnum+1):
                        all_games.append(copy.deepcopy(all_games[-1]))
                        single_point.append(all_games[-1].rujian(i+1,j))
                        all_games.pop(-1)
                    all_point.append(sum(single_point)/self.maxnum)
                choose_group=all_point.index(max(all_point))+1
            elif ai_mode == 3:
                all_point=[]
                higher_rate=[]
                all_median_point=[]
                for i in range(self.group):
                    single_point=[]
                    higher_num=0
                    for j in range(1,self.maxnum+1):
                        all_games.append(copy.deepcopy(all_games[-1]))
                        pointup=all_games[-1].rujian(i+1,j)
                        single_point.append(pointup)
                        if pointup>=self.maxpoint-self_point:
                            higher_num+=1
                        all_games.pop(-1)
                    all_point.append(sum(single_point)/self.maxnum)
                    higher_rate.append(higher_num/self.maxnum)
                    all_median_point.append(median(single_point))
                if (self_point>self.maxpoint*0.9 or (self_point<others_point and others_point>self.maxpoint*0.8)) and max(higher_rate)>0:
                    choose_group=higher_rate.index(max(higher_rate))+1
                elif self_point>others_point and self_point-others_point>self.maxpoint*0.2:
                    choose_group=all_median_point.index(max(all_median_point))+1
                else:
                    choose_group=all_point.index(max(all_point))+1
            print_if('AI选择在第%d列炸鱼'%choose_group,None,print_switch)
            return choose_group
while True:
    print('炸鱼游戏(random fish)1.3')
    print('1:开始游戏 2:调整游戏设置')#3:调试模式
    choose=inp(3)
    if choose == 1:
        all_games.append(games(3,9,3,50,0,0,0,0))
        ai_mode=2
        ai_help=0
    elif choose == 2:
        print('你是否让选择让AI帮助你？1:是 2:否')
        if inp(2) == 1:
            print('你选择什么AI帮助你？1:傻逼 2:正常 3:高手(默认为正常)')
            ai_help=inp(3)
        else:
            ai_help=0
        print('调整棋盘列数为(默认为3)')
        group=inp(None)
        print('调整同行相同时的消除倍率为(默认为3)')
        line_rate=inp(None)
        print('调整AI智商为(默认为正常)1:傻逼 2:正常 3:高手 4:无AI')
        ai_mode=inp(4)
        print('调整目标得分为(默认为50)')
        maxpoint=inp(None)
        print('调整抽取的最大数字为(默认为9)')
        maxnum=inp(None)
        all_games.append(games(group,maxnum,line_rate,maxpoint,0,0,0,0))
        input('调整完成，按回车键开始游戏')
    elif choose == 3:
        print('在调试模式中将仅由AI与AI对战，以检验AI的智能程度')
        print('请输入双方的ai_mode')
        ai_help=inp(3)
        ai_mode=inp(3)
        print('调整棋盘列数为(默认为3)')
        group=inp(None)
        print('调整同行相同时的消除倍率为(默认为3)')
        line_rate=inp(None)
        print('调整目标得分为(默认为50)')
        maxpoint=inp(None)
        print('调整抽取的最大数字为(默认为9)')
        maxnum=inp(None)
        print('请输入试验总次数')
        try_times=inp(None)
        awin_times=0
        bwin_times=0
        all_games.append(games(group,maxnum,line_rate,maxpoint,0,0,0,0))
        print_switch=False
        input('调整完成，按回车键开始测试')
    while True:
        sx=choice([True,False])
        print_if('游戏开始，本局游戏随机由'+sxmeans[0][sx]+'先手',None,print_switch)
        all_games[-1].print_qipan()
        while True:
            exec(sxmeans[3][sx]+'='+sxmeans[3][sx]+'+1')
            choose_group=all_games[-1].aithink(eval(sxmeans[1][sx]),eval(sxmeans[2][sx]),eval(sxmeans[2][not sx]))
            get_num=rd(1,all_games[-1].maxnum)
            exec(sxmeans[2][sx]+'+=all_games[-1].rujian(choose_group,get_num)')
            print_if(sxmeans[0][sx]+'第%d列抽到的数为%d'%(choose_group,get_num),None,print_switch)
            print_if('现在的棋盘状况为',None,print_switch)
            all_games[-1].print_qipan()
            print_if('我方得分:%d\nAI得分:%d'%(all_games[-1].pointa,all_games[-1].pointb),None,print_switch)
            if all_games[-1].pointa >= all_games[-1].maxpoint or all_games[-1].pointb >= all_games[-1].maxpoint:
                print_if('游戏结束,'+sxmeans[0][sx]+'赢了',None,True)
                exec(sxmeans[4][sx]+'='+sxmeans[4][sx]+'+1')
                break
            if print_switch:
                input('请按回车键继续')
            sx=not sx
        print_if('是否开始新一轮游戏？1:返回主菜单,2:以当前规则重启游戏,3：退出游戏',None,print_switch)
        if print_switch:
            choose=inp(3)
        else:
            if awin_times+bwin_times<try_times:
                choose=2
            else:
                input('%d:%d,按回车键以退出'%(awin_times,bwin_times))
                print_switch=True
                choose=3
        if choose == 1:
            break
        elif choose == 2:
            all_games.append(games(all_games[-1].group,all_games[-1].maxnum,all_games[-1].line_rate,all_games[-1].maxpoint,0,0,0,0))
            print_if('游戏已重启',None,print_switch)
        else:
            break
    if choose == 3:
        break