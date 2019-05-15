

def set_creator():
    tps = ['TP1']
    tp = 'a' \
         ''
    while tp:
        tp = input("enter test point: ")
        tps.append(tp)
        tps = list(set(tps))

    for item in tps:
        if item == '':
            tps.remove(item)
    tps = sorted(tps)
    print(tps)
    print(', '.join(tps))