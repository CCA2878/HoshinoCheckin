import sqlite3
import os
import json
import hoshino
# import file

userDictTemplate = {'userID':'', 'userCard':'', 'status':0} # 暂定：0 无任务
# conn = sqlite3.connect('database/data.db')



class Data:
    
    def __init__(self, bot, groupID:str, userCount:int) -> None:

        self.groupID = groupID
        self.userCount = userCount

        if not os.path.isdir('data'):
            os.makedirs('data')
        if not os.path.exists('data/index.json'):
            open('data/index.json', mode = 'x')

    # @staticmethod
    # def getGroupMebNum(groupID:str):
    #     with hoshino.get_bot() as

    def genIndex(self):
        pass

    # @staticmethod
    def newUsrList(self, name:str) -> int:

        '''
        创建一个用户列表的初始配置，
        成功返回0，
        失败返回非0，
        文件已存在返回1，
        其他错误返回2
        '''

        f = None
        originDict = {'groupID':'', 'userList':[]}

        try:
            if os.path.exists(f'data/{name}.json') != False:
                return 1
            # open(f'data/{name}.json', mode = 'x')
            with open(f'data/{name}.json', mode='w+', encoding='utf-8') as f:
                json.dump(originDict, fp=f)
        except:
            return 2
        else:
            return 0
    
    def _initUsrList(self, dict:dict):
        pass








if __name__ == '__main__':
    print(Data.newUsrList('test2'))
    # name = 'test2'
    # if not os.path.exists(f'data/{name}.json'):
    #     print(1)
    # if not os.path.exists(f'data/index.json'):
    #     print(2)
    # print(os.path.exists(f'data/index.json'))
    # print(os.path.exists(f'data/{name}.json'))
    # print(f'data/index.json')
    # print(f'data/{name}.json')