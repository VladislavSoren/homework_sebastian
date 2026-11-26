scores = {"Аня": 85, "Боря": 90, "Вера": 78}
scoresnew = {"Аня": 85, "Боря": 90, "Вера": 78}
for name, score in scores.items():    
    result = score - 10
    scores[name] = result
    namenew = name + "2"
    scoresnew[namenew] = result
print (scoresnew)