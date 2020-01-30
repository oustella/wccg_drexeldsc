#Week-3 challange : https://app.codesignal.com/challenge/ns25kwheaFf9WLZ45
#Solution1 passed the time limit
def burningTheWood(n, wmap, start, k):
    op = [start]
    while k > 0:
        start = set(op)
        for i in wmap:
            if i[0] in start or i[1] in start:
                op.extend(i)
        k -= 1
    return sorted(list(set(op)))
