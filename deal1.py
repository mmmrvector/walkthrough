import json
import os
from enum import Enum
import walkthrough
import data1

res = json.load(open('res.json', 'r'))
#print(res)
#需要游戏名、关卡名(关卡序号？)
def query(game, level, mission):
    # position = 0 表示概要
    #res['response']['outspeech'] = database.get_content(game, level, mission, 0)
    save(game = game, level = level, mission = mission, position = "1")
    return data1.GetContent(game, level, mission, 0)

def nextstep(*, rep = False):
    with open('record.json', 'r') as f:
        record = json.load(f)
    pos = int(record['position'])
    if rep == True:
        #res['response']['outspeech'] = database.get_content(record['game'], record['level'], mission, pos - 1)
        return data1.GetContent(record['game'], record['level'], record['mission'], pos - 1)
    else:
        #res['response']['outspeech'] = database.get_content(record['game'], record['level'], mission, pos)
        save(position=str(pos + 1))
        return data1.GetContent(record['game'], record['level'], record['mission'], pos)


def repeat():
    return nextstep(rep = True)

def exitsession():
    #res['response']['shouldEndSession'] = True
    return "欢迎下次继续使用"

def save(*, game = None, level = None, mission = None, position):

    with open('record.json', 'r') as f:
        record = json.load(f)
    if game != None:
        record['game'] = game
    if level != None:
        record['level'] = level
    if mission != None:
        record['mission'] = mission
    record['position'] = position
    with open('record.json', 'w') as f:
        json.dump(record, f, indent = 4)
'''
def printrecord():
    with open('record.json', 'r') as f:
        print(f.read())

def test():
    Intent = Enum('Intent',('Query', 'Nextstep', 'Repeat', 'Exit'))
    #database = niubi() 假设这是数据库
    dealer = {
        Intent.Nextstep: nextstep,
        Intent.Repeat: repeat,
        Intent.Exit: exitsession
    }
    res['response']['shouldEndSession'] = False

    while True:
        intent = int(input('输入意图：1查询2下一步3重复4退出\n'))
        if Intent(intent) == Intent.Query:
            query('看门狗2', '2')
        else:
            dealer[Intent(intent)]()
        print(res)
        printrecord()
        if res['response']['shouldEndSession'] == True:
            exit()
if __name__ == '__main__':
    test()
'''