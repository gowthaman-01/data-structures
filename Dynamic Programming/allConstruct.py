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


def helper(target, wordBank, store):
    if target == "":
        return [[]]
    if target in store:
        return store[target]
    output = []
    for word in wordBank:
        if isPrefix(target, word):
            possible = helper(suffix(target, word), wordBank, store)
            for i in range(len(possible)):
                possible[i] = possible[i] + [word]
            output += possible
    store[target] = output
    return store[target]


def allConstruct(target, wordBank):
    store = {}
    return helper(target, wordBank, store)


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(allConstruct("stakeboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
