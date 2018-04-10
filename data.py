import json

def GetContent(game, level, mission, step, first = False):
	level = level - 1
	mission = mission - 1
	print('level', level, 'mission', mission, 'step', step)
	#data = json.load(open('DATA_WATCHDOG2.json', 'r'))

	if game == '看门狗2' or game == '看门狗二' or game == '看门狗而' or game == '看萌狗二' or game == '开门狗二' or game == '开门口二':
		data = json.load(open("DATA_WATCHDOG2.json", 'r'))
	elif game == '侠盗飞车五' or game == 'GTA5' or game == '侠盗飞车5' or game == '侠盗猎车五':
		data = json.load(open("DATA_GTA5.json", 'r'))
	elif game == '使命召唤14二战' or game == '使命召唤十四二战' or game == '使命召唤十四' or game == '使命召唤':
		data = json.load(open("DATA_COD14.json", "r"))

	if first:
		try:
			ll = len(data['level'])
			ml = len(data['level'][level]['missions'])
			sl = len(data['level'][level]['missions'][mission]['content'])
			return data['level'][level]['missions'][mission]['content'][step]['step'], ll, ml, sl
		except IndexError as error:
			return '您想要的攻略不存在。换个章节或关卡试试。', None, None, None
	return data['level'][level]['missions'][mission]['content'][step]['step']
