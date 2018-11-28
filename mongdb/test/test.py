# encoding:utf-8
import os
import json


settingFileName = 'CTA_setting.json'
    # JSON配置文件路径
jsonPathDict = {};


def getJsonPath(name, moduleFile):
    """
    获取JSON配置文件的路径：
    1. 优先从当前工作目录查找JSON文件
    2. 若无法找到则前往模块所在目录查找
    """
    currentFolder = os.getcwd()
    currentJsonPath = os.path.join(currentFolder, name)
    if os.path.isfile(currentJsonPath):
        jsonPathDict[name] = currentJsonPath
        return currentJsonPath

    moduleFolder = os.path.abspath(os.path.dirname(moduleFile))
    moduleJsonPath = os.path.join(moduleFolder, '.', name)
    jsonPathDict[name] = moduleJsonPath
    return moduleJsonPath


settingfilePath = getJsonPath(settingFileName, __file__)


def saveSetting(self):
    """保存策略配置"""
    with open(self.settingfilePath, 'w') as f:
        l = []

        for strategy in self.strategyDict.values():
            setting = {}
            for param in strategy.paramList:
                setting[param] = strategy.__getattribute__(param)
            l.append(setting)

        jsonL = json.dumps(l, indent=4)
        print jsonL
        f.write(jsonL)

saveSetting();
# ----------------------------------------------------------------------
