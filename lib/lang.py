
def getGender(word: str, langCode: str):
    shortCode = langCode[:2]
    if shortCode == "ru":
        femAdjectives = ["ая"]
        maleAdjectives = ["ый","ий"]
        itAdjectives = ["ый"]
        femNoun = ["а","я"]
        maleNoun = ["н",""]
        itNoun = ["о"]
        if word[-2:] in femAdjectives or word[-1:] in femNoun: return "female"
        if word[-2:] in maleAdjectives or word[-1:] in maleNoun: return "female"
        if word[-2:] in itAdjectives or word[-1:] in itNoun: return "female"
    if shortCode == "es":
        pass
