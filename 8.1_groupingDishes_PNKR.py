#https://app.codesignal.com/interview-practice/task/xrFgR63cw7Nch4vXo

def groupingDishes(dishes):
    dishes = sorted(dishes, key = lambda x: x[0])
    ing = [j for i in dishes for j in i[1:]]
    ing = list(set([i for i in ing if ing.count(i) > 1 ]))
    ing.sort()    
    ml = []
    for i in ing:
        t = [i]
        for x in dishes:
            if i in x[1:]:
                t.append(x[0])
        ml.append(t)      
    return ml