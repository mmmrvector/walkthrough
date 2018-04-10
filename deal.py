import json
import os
from enum import Enum
import walkthrough
import data

#需要游戏名、关卡名(关卡序号？)
def query(game, level, mission):
    # position = 0 表示概要
    outspeech, ll, ml, sl = data.GetContent(game, level, mission, 0, True)
    save(game = game, level = level, mission = mission, position = 1, ll = ll, ml = ml, sl = sl)
    if outspeech == '':
        outspeech = '本篇攻略没有概要，请准备好后对我说开始或下一步。'
    return '现在为您播放'+ game + '的第' + str(level) + '章第' + str(mission) + '关的攻略，' + outspeech

def nextstep(*, rep = False):
    with open('record.json', 'r') as f:
        record = json.load(f)
    pos = record['position']
    if rep == True:
        return data.GetContent(record['game'], record['level'], record['mission'], pos - 1)
    else:
        ll = record['levellength']
        ml = record['missionlength']
        sl = record['steplength']
        mission = record['mission']
        level = record['level']
        # 已经到下一个mission
        print('pos', pos, 'sl', sl)
        if pos == sl:
            # 已经到下一个level
            if mission == ml - 1:
                # 已经到最后一个level
                if level == ll - 1:
                    return record['game']+'的攻略已经结束啦！'
                else:
                    outspeech, ll, ml, sl = data.GetContent(record['game'], level + 1, 0, 0, True)
                    save(level = level + 1, mission = 0, position = 1, ll = ll, ml = ml, sl = sl)
                    return '现在进入下一章节。' + outspeech
            else:
                outspeech, ll, ml, sl = data.GetContent(record['game'], level, mission + 1, 0, True)
                save(level = level, mission = mission + 1, position = 1, ll = ll, ml = ml, sl = sl)
                return '现在进入下一个任务。' + outspeech
        else:
            save(position = pos + 1)
            return data.GetContent(record['game'], record['level'], record['mission'], pos)


def repeat():
    return nextstep(rep = True)

def exitsession():
    #res['response']['shouldEndSession'] = True
    return "欢迎下次继续使用"

def save(*, game = None, level = None, mission = None, position, ll = None, ml = None, sl = None):

    with open('record.json', 'r') as f:
        record = json.load(f)
    if game != None:
        record['game'] = game
    if level != None:
        record['level'] = level
    if mission != None:
        record['mission'] = mission
    if ll != None:
        record['levellength'] = ll
    if ml != None:
        record['missionlength'] = ml
    if sl != None:
        record['steplength'] = sl
    record['position'] = position
    with open('record.json', 'w') as f:
        json.dump(record, f, indent = 4)


def lastPos():
    with open('record.json', 'r') as f:
        record = json.load(f)
    game = record['game']
    level = record['level']
    mission = record['mission']
    if game == "":
        return ""
    #TODO 采用map进行中文和阿拉伯数字的转换
    return '您上次在'+ game + '中玩到第' + str(level) +'章第' + str(mission) +'关'+ '请问您想继续下一步吗还是'

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
            query('看门狗2', 2, 1)
        else:
            dealer[Intent(intent)]()
        print(res)
        printrecord()
        if res['response']['shouldEndSession'] == True:
            exit()
if __name__ == '__main__':
    test()
'''
