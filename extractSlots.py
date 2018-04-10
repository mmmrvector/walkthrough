# -*- coding: utf-8 -*-
import re

def extractSlots(text):
	#打开芭乐攻略
	pattern = re.compile('打开(芭乐|八路)攻略')
	result = re.match(pattern, text)
	if result:
		return 7, None
	'''
	pattern = re.compile('(芭乐攻略|八路攻略)?(上一部|上一步)')
	result = re.match(pattern, text)
	if result:
		return 3, None

	pattern = re.compile('(芭乐攻略|八路攻略)?(侠盗飞车五|侠盗猎车五)的第(?P<first_index>.+)关')
	result = re.match(pattern, text)
	if result:

		first_index = result.group("first_index")
		if (first_index == '一'):
			first_index = 1
		elif first_index == '二':
			first_index = 2
		elif first_index == '三':
			first_index = 3
		else:
			first_index = 4

		return 1, ('侠盗飞车五', first_index, 1)

	pattern = re.compile('(芭乐攻略|八路攻略)?(看门狗二|看萌狗二|开门狗二)的第(?P<first_index>.+)关')
	result = re.match(pattern, text)
	if result:

		first_index = result.group("first_index")
		if(first_index == '一'):
			first_index = 1
		elif first_index == '二':
			first_index = 2
		elif first_index == '三':
			first_index = 3
		else:
			first_index = 4

		return 1, ('看门狗二', first_index, 1)

	pattern = re.compile('(芭乐攻略|八路攻略)?(使命召唤十四|使命召唤|使命召唤二战|使命召唤十四二战)的第(?P<first_index>.+)关')
	result = re.match(pattern, text)
	if result:
		first_index = result.group("first_index")
		if (first_index == '一'):
			first_index = 1
		elif first_index == '二':
			first_index = 2
		elif first_index == '三':
			first_index = 3
		else:
			first_index = 4

		return 1, ('使命召唤十四', first_index, 1)

	pattern = re.compile('(芭乐攻略)?(侠盗猎车|侠盗飞车)五')
	result = re.match(pattern, text)
	if result:
		return 1, ('侠盗猎车五', 1, 1)

	pattern = re.compile('(芭乐攻略|八路攻略)?(看门狗二|看萌狗二|开门狗二)')
	result = re.match(pattern, text)
	if result:
		return 1, ('看门狗二', 1, 1)

	pattern = re.compile('(芭乐攻略|八路攻略)?(使命召唤十四|使命召唤|使命召唤二战|使命召唤十四二战)')
	result = re.match(pattern, text)
	if result:
		return 1, ('使命召唤十四', 1, 1)
	'''
	pattern_gta5 = re.compile('侠盗飞车五|侠盗猎车五|GTA5')
	pattern_watchdog = re.compile('看门狗二|看萌狗二|开门狗二|开门口二|看门口二|门狗二')
	pattern_call = re.compile('使命召唤十四|使命召唤|使命召唤二战|使命召唤十四二战')

	#通过游戏名和关卡名查询游戏通关攻略
	pattern = re.compile('(芭乐攻略)?(帮我)?(找|查|搜|查找|查询|看)?(一下|下)?(?P<game>.+)(的)?第(?P<first_index>.+)(关|章|节|关卡|站|个任务|场)第(?P<second_index>.+)(关|章|节|关卡|站|个任务|场)(的攻略)?')
	result = re.match(pattern, text);
	if result:
		game = result.group("game")
		first_index = result.group("first_index")
		if (first_index == '一'):
			first_index = 1
		elif first_index == '二':
			first_index = 2
		elif first_index == '三':
			first_index = 3
		else:
			return 0, None
		second_index = result.group("second_index")
		if (second_index == '一'):
			second_index = 1
		elif second_index == '二':
			second_index = 2
		elif second_index == '三':
			second_index = 3
		else:
			return 0, None
		if re.match(pattern_gta5, game):
			game = '侠盗猎车五'
			return 1, (game, first_index, second_index)
		elif re.match(pattern_watchdog, game):
			game = '看门狗二'
			return 1, (game, first_index, second_index)
		elif re.match(pattern_call, game):
			game = '使命召唤十四'
			return 1, (game, first_index, second_index)

	pattern = re.compile('(芭乐攻略)?(帮我)?(找|查|搜|查找|查询|看)?(一下|下)?(?P<game>.+)(的)?第(?P<first_index>.+)(关|章|节|关卡|站|个任务|场)(的攻略)?')
	result = re.match(pattern, text);
	if result:
		game = result.group("game")
		first_index = result.group("first_index")
		if (first_index == '一'):
			first_index = 1
		elif first_index == '二':
			first_index = 2
		elif first_index == '三':
			first_index = 3
		else:
			return 0, None
		if re.match(pattern_gta5, game):
			game = '侠盗猎车五'
			return 1, (game, first_index, 1)
		elif re.match(pattern_watchdog, game):
			game = '看门狗二'
			return 1, (game, first_index, 1)
		elif re.match(pattern_call, game):
			game = '使命召唤十四'
			return 1, (game, first_index, 1)
			
	pattern = re.compile('(芭乐攻略)?(帮我)?(找|查|搜|查找|查询|看)?(一下|下)?(?P<game>.+)(的攻略)?')
	result = re.match(pattern, text)
	if result:
		game = result.group("game")
		print(game)
		if re.match(pattern_gta5, game):
			game = '侠盗猎车五'
			return 1, (game, 1, 1)
		elif re.match(pattern_watchdog, game):
			game = '看门狗二'
			return 1, (game, 1, 1)
		elif re.match(pattern_call, game):
			game = '使命召唤十四'
			return 1, (game, 1, 1)

	#下一步
	pattern = re.compile('(芭乐攻略)?(下一步|下一关|接下来|然后)(怎么办|怎么搞|是什么|怎么做|怎么干|干什么|搞什么|做什么)?')
	if re.match(pattern, text):
		return 2, None

	#重复当前步骤
	pattern = re.compile('(芭乐攻略)?(刚才|上一步|上一部|上一关)(怎么办|怎么搞|是什么|怎么做|怎么干|干什么|搞什么|做什么)?.*')
	if re.match(pattern, text):
		return 3, None 

	#停止提供服务
	pattern = re.compile('(芭乐攻略)?(停|停下来|别说了|住嘴|闭嘴|退出).*')
	if re.match(pattern, text):
		return 4, None

	#通过游戏名和角色名查询角色技能
	pattern = re.compile('(芭乐攻略)?(帮)?(我)?(找|查|搜)((一)?下)?(?P<game>.+)(中|(里)?面)?的(?P<role>.+)的技能.*')
	result = re.match(pattern, text)
	if result:
		game = result.group("game")
		role = result.group("role")
		return 5, (game, role)
	return 0, None

'''
text1 = "芭乐游戏攻略帮我找侠盗联盟5的第3关第2关的攻略"
text6 = "芭乐游戏攻略帮我找侠盗联盟5的第3关的攻略"
text2 = "下一步"
text3 = "上一步"
text4 = "停"
text5 = "帮我找王者荣耀中的孙权的技能"
print(extractSlots(text1))
print(extractSlots(text2))
print(extractSlots(text3))
print(extractSlots(text4))
print(extractSlots(text5))
print(extractSlots(text6))
'''