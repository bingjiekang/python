# -*- coding:utf-8 -*-
import copy     # 注意对象的深拷贝和浅拷贝的使用！！！
class GameNode:  
    '''博弈树结点数据结构  
    成员变量：  
    map - list[[]] 二维列表，三子棋盘状态  
    val - int  该棋盘状态对执x棋子的评估值，1表示胜利，-1表示失败，0表示平局  
    deepID - int 博弈树的层次深度，根节点deepID=0  
    parent - GameNode，父结点  
    children - list[GameNode] 子结点列表  
    '''  
    def __init__(self, map, val=0, deepID=0, parent=None, children=[]):  
        self.map = map  
        self.val = val  
        self.deepID = deepID  
        self.parent = parent  
        self.children = children
class GameTree:  
    '''博弈树结点数据结构  
    成员变量：  
    root - GameNode 博弈树根结点  
    成员函数：  
    buildTree - 创建博弈树  
    '''  
    def __init__(self, root):  
        self.root = root                # GameNode 博弈树根结点
    def buildTree(self, root):  
        '''递归法创建博弈树  
        参数：  
        root - GameNode 初始为博弈树根结点  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        posList = []  
        for i in range(3):  
            for j in range(3):  
                if root.map[i][j]=='_':  
                    posList.append((i,j))
        for (x, y) in posList:  
            childNode = GameNode(map=copy.deepcopy(root.map),  
                                 val=0, deepID=root.deepID+1, parent=root, children=[])  
            if root.deepID%2==0:  
                childNode.map[x][y]='x'  
            else :  
                childNode.map[x][y]='o'  
            root.children.append(childNode)
        for childNode in root.children:  
            self.buildTree(childNode)
        #********** End **********#
class MinMax:  
    '''博弈树结点数据结构  
    成员变量：  
    game_tree - GameTree 博弈树  
    成员函数：  
    minmax - 极大极小值算法，计算最优行动  
    max_val - 计算最大值  
    min_val - 计算最小值  
    get_val - 计算某棋盘状态中：执x棋子的评估值，1表示胜利，-1表示失败，0表示平局  
    isTerminal - 判断某状态是否为最终状态：无空闲棋可走  
    '''  
    def __init__(self, game_tree):  
        self.game_tree = game_tree      # GameTree 博弈树
    def minmax(self, node):  
        '''极大极小值算法，计算最优行动  
        参数：  
        node - GameNode 博弈树结点  
        返回值：  
        clf - list[map] 最优行动，即x棋子的下一个棋盘状态GameNode.map  
              其中，map - list[[]] 二维列表，三子棋盘状态  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        best_val = self.max_value(node)  
        best_move = []  
        for childNode in node.children:  
            if childNode.val == best_val and best_val==1:  
                best_move.append(childNode.map)  
        return best_move
        #********** End **********#
    def max_value(self, node):  
        '''计算最大值  
        参数：  
        node - GameNode 博弈树结点  
        返回值：  
        clf - int 子结点中的最大的评估值  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        if self.isTerminal(node):  
            val = self.get_value(node)  
            node.val = val  
            return val  
        inf_val = float('inf')  
        max_val = -inf_val  
        for childNode in node.children:  
            max_val = max(max_val, self.min_value(childNode))  
        node.val = max_val  
        return max_val
        #********** End **********#
    def min_value(self, node):  
        '''计算最小值  
        参数：  
        node - GameNode 博弈树结点  
        返回值：  
        clf - int 子结点中的最小的评估值  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        if self.isTerminal(node):  
            val = self.get_value(node)  
            node.val = val  
            return val  
        inf_val = float('inf')  
        min_val = inf_val  
        for childNode in node.children:  
            min_val = min(min_val, self.max_value(childNode))  
        node.val = min_val  
        return min_val
        #********** End **********#
    def get_value(self, node):  
        '''计算某棋盘状态中：执x棋子的评估值，1表示胜利，-1表示失败，0表示平局  
        参数：  
        node - GameNode 博弈树结点  
        返回值：  
        clf - int 执x棋子的评估值，1表示胜利，-1表示失败，0表示平局  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        for i in range(3):  
            if node.map[i][0]=='o' and node.map[i][0]==node.map[i][1] and node.map[i][1]==node.map[i][2]:  
                return -1  
            if node.map[0][i]=='o' and node.map[0][i]==node.map[1][i] and node.map[1][i]==node.map[2][i]:  
                return -1  
        if node.map[0][0]=='o' and node.map[0][0]==node.map[1][1] and node.map[1][1]==node.map[2][2]:  
            return -1  
        if node.map[0][2]=='o' and node.map[0][2]==node.map[1][1] and node.map[1][1]==node.map[2][0]:  
            return -1  
        for i in range(3):  
            if node.map[i][0]=='x' and node.map[i][0]==node.map[i][1] and node.map[i][1]==node.map[i][2]:  
                return 1  
            if node.map[0][i]=='x' and node.map[0][i]==node.map[1][i] and node.map[1][i]==node.map[2][i]:  
                return 1  
        if node.map[0][0]=='x' and node.map[0][0]==node.map[1][1] and node.map[1][1]==node.map[2][2]:  
            return 1  
        if node.map[0][2]=='x' and node.map[0][2]==node.map[1][1] and node.map[1][1]==node.map[2][0]:  
            return 1  
        return 0
        #********** End **********#
    def isTerminal(self, node):  
        '''判断某状态是否为最终状态：无空闲棋可走（无子结点）  
        参数：  
        node - GameNode 博弈树结点  
        返回值：  
        clf - bool 是最终状态，返回True，否则返回False  
        '''  
        #请在这里补充代码，完成本关任务  
        #********** Begin **********#
        assert node is not None  
        return len(node.children)==0
        #********** End **********#
