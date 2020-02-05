# https://app.codesignal.com/challenge/KkRXXEt9DwaHFYk2K


def isCryptSolution(crypt, solution):
    sdict = {i[0]:i[1] for i in solution}
    translate = lambda astring: "".join([sdict[i] for i in astring])
    for i in crypt:
        if len(i) > 1 and translate(i)[0] == '0':
            return False
    return int(translate(crypt[0])) + int(translate(crypt[1])) == int(translate(crypt[2]))

# shortened solution
def isCryptSolution(crypt, solution):
    sdict = dict(solution)
    tr = lambda s: "".join([sdict[i] for i in s])
    zeros = any(tr(i)[0] == '0' for i in crypt if len(i) > 1)
    return not zeros and int(tr(crypt[0])) + int(tr(crypt[1])) == int(tr(crypt[2]))