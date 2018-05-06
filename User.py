from enum import Enum

Intent = Enum('Intent',('Start', 'Exit', 'Unclear', 'Query', 'NextStep', 'Repeat', 'AskPos', 'QueryRole'))

class NotExistError(Exception):
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo
class NextNullError():
    def __init__(self, ErrorInfo):
        super().__init__(self)
        self.errorinfo = ErrorInfo
    def __str__(self):
        return self.errorinfo

class Record(object):
    """docString"""
    #info内容：(game, level, mission, step)/(game, chara, kind)
    def __init__(self, *info):
        self.setInfo(*info)
    def __str__(self):
        if self.type == 0:
            return self.game + '的' + self.chara + '的' + self.kind
        elif self.type == 1:
            return self.game + '的第' + str(self.level) + '章第' + str(self.mission) + '关的第' + str(self.step) + '步'
    def setInfo(self, *info):
        if len(info) == 3:
            self.type = 0           #网游类
            self.game = info[0]
            self.chara = info[1]
            self.kind = info[2]
        elif len(info) == 4:
            self.type = 1           #流程类
            self.game = info[0]
            self.level = info[1]
            self.mission = info[2]
            self.step = info[3]

            gameData = Game(self.game)
            self.levellength, self.missionlength, self.steplength =
                gameData.getLens(self.level, self.mission, self.step)
            if self.levellength == None:
                raise NotExistError('查询的关卡不存在')
        else:
            raise ValueError('Wrong Arguments')
    def setKind(self, kind):
        self.kind = kind
    def update(self):
        if self.type == 0:
            raise AttributeError()
        if self.step == self.steplength:
            if self.mission == self.missionlength:
                if self.level == self.levellength:
                    return False
                else:
                    self.level += 1
                    self.mission = 1
                    self.step = 0
            else:
                self.mission += 1
                self.step = 0
        else:
            self.step += 1
        return True

class User(object):
    """docString"""
    def __init__(self, uid):
        self.__id = uid
        self.__records = {}
        self.__currecord = None
    # 传入的info同上
    def __query(self, info):
        game = info[0]
        if game in self.__records:
            self.__records[game].setInfo(*info)
            self.__currecord = self.__records[game]
            return self.__records[game]
        else:
            self.__currecord = Record(*info)
            self.__records[game] = self.__currecord
            return self.__currecord
    def __nextstep(self, info):
        if self.__currecord.update() == True:
            return self.__currecord
        else:
            raise NextNullError('没有下一步了')
    def __repeat(self, info):
        return self.__currecord
    def __queryrole(self, info):
        if info[0] == None:
            self.__currecord.setKind(info[2])
            return self.__currecord
        else:
            self.__currecord = Record(*info)
            self.__records[info[0]] = self.__currecord
            return self.__currecord
    def getUserRecord(self, intent, info):
        methoddict = {
            Intent.Query: self.__query,
            Intent.NextStep: self.__nextstep,
            Intent.Repeat: self.__repeat,
            Intent.AskPos: self.__repeat,
            Intent.QueryRole: self.__queryrole
        }
        return methoddict[intent](info)

testuser = User(517)
print(testuser.getUserRecord(Intent.Query, ('看门狗2',2,1,1)))
print(testuser.getUserRecord(Intent.NextStep, None))
print(testuser.getUserRecord(Intent.Repeat, None))
print(testuser.getUserRecord(Intent.AskPos, None))

print(testuser.getUserRecord(Intent.NextStep, None))
print(testuser.getUserRecord(Intent.AskPos, None))

print(testuser.getUserRecord(Intent.NextStep, None))
print(testuser.getUserRecord(Intent.AskPos, None))

print(testuser.getUserRecord(Intent.NextStep, None))
print(testuser.getUserRecord(Intent.AskPos, None))

print(testuser.getUserRecord(Intent.NextStep, None))
print(testuser.getUserRecord(Intent.AskPos, None))
