import json



def GetContent(game, level, mission, step):
    print('game', game, 'level', level, 'mission', mission, 'step', step)
    if game == '看门狗2' or game == '看门狗二' or game == '看门狗而':
        data = json.load(open("DATA_WATCHDOG2.json", 'r'))
    elif game == '侠盗猎车5' or game == 'GTA5' or game =='侠盗飞车5' or game == '侠盗猎车五':
        data = json.load(open("DATA_GTA5.json"), 'r')
    elif game == '使命召唤14二战' or game == '使命召唤十四二战' or game == '使命召唤十四' or game == '使命召唤14':
        data = json.load(open("DATA_COD14.json"))
    return data['level'][level]['missions'][mission]['content'][step]['step']