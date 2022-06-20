def isPrefix(word, prefix):
    if len(prefix) > len(word):
        return False
    for i in range(len(prefix)):
        if word[i] != prefix[i]:
            return False
    return True


def suffix(word, prefix):
    prefixLength = len(prefix)
    return word[prefixLength:]


def check(target, wordBank, store):
    if target == '':
        return True
    if target in store:
        return store[target]
    for word in wordBank:
        if isPrefix(target, word):
            store[target] = check(suffix(target, word), wordBank, store)
            if store[target]:
                return True
    store[target] = False
    return store[target]


def canConstruct(target, wordBank):
    store = {}
    return check(target, wordBank, store)


print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("stakeboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(canConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
