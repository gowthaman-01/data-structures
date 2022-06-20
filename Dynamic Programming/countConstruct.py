def isPrefix(word, prefix):
    if len(prefix) > len(word):
        return False
    for i in range(len(prefix)):
        if prefix[i] != word[i]:
            return False
    return True


def suffix(word, prefix):
    prefixLength = len(prefix)
    return word[prefixLength:]


def helper(target, wordBank, store):
    if target == "":
        return 1
    if target in store:
        return store[target]
    count = 0
    for word in wordBank:
        if isPrefix(target, word):
            count += helper(suffix(target, word), wordBank, store)
    store[target] = count
    return store[target]


def countConstruct(target, wordBank):
    store = {}
    return helper(target, wordBank, store)


print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(countConstruct("stakeboard", [
      "bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(countConstruct("enterapotentpot", [
      "a", "p", "ent", "enter", "ot", "o", "t"]))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
      ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))
