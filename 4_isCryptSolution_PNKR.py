#Week-4 challange : https://app.codesignal.com/challenge/KkRXXEt9DwaHFYk2K
#Solution passed the time limit
def isCryptSolution(crypt, solution):
    d = {}
    for i in solution:
        d[i[0]] = i[1]
    for word in crypt:
        decrypt = ''
        for char in word:
            decrypt += str(d[char])
        if decrypt[0] == '0' and len(decrypt) != 1:
            return False
        d[word] = int(decrypt)
    if d[crypt[0]] + d[crypt[1]] == d[crypt[2]]:
        return True
    else:
        return False
