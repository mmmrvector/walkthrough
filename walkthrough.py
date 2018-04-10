from flask import Flask,json, jsonify, request, Response
import extractSlots
import deal
import fileinput
import os

app = Flask(__name__)

global db




@app.route('/', methods = ['POST'])
def GetRequest():
    Data = request.get_data()
    data = json.loads(Data)
    utterance = data['request']['utterance']
    print(utterance)
    #得到操作类型和操作指令
    op,cmd = extractSlots.extractSlots(utterance)
    print(op, cmd)
    game = None
    level = None
    mission = None
    if cmd != None:
        #(game, level, mission) = cmd
        print(cmd)
        game = cmd[0]
        if(cmd[1] == '二'):
            level = 2
        if(cmd[2] == '二'):
            mission = 2
        level = int(cmd[1])
        mission = int(cmd[2])

    #通过游戏名和关卡名查询游戏通关攻略
    if op == 1:
        outspeech = deal.query(game, level, mission)
    #下一步
    elif op == 2:
        outspeech = deal.nextstep()
    #重复当前步骤
    elif op == 3:
        outspeech = deal.repeat()
    #停止提供服务
    elif op == 4:
        outspeech = deal.exitsession()
    #打开芭乐攻略
    elif op == 7:
        outspeech = deal.lastPos() + '请问您需要哪个游戏的攻略'
    else:
        outspeech = '对不起，没听清您的指令'
    return SendResponse(outspeech, op, data)



def SendResponse(rt, op, data):
    with open('response_pattern.json', 'r') as input:
        response = json.load(input)
    if op == 4:
        response['response']['shouldEndSession'] = True
    response['version'] = data['version']
    response['requestId'] = data['request']['requestId']
    response['response']['reprompt']['outputSpeech'] = ""
    response['response']['outputSpeech'] = rt
    response['response']['directives']['url'] = 'http://123.57.219.210/voice/silence.mp3'
    print(response)
    return jsonify(response)





if __name__ == '__main__':
    #StartDB()
    app.run(
        host = "localhost",
        port = 22141,
        debug = True
    )
