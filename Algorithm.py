id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

zl = [0 for _ in range(len(id_list))]
bl = dict(zip(id_list, zl))
wl = [i.split() for i in report]
rl = []

for i, n in enumerate(wl):
    if n not in rl:
        rl.append(n)
        bl[n[1]] += 1
el = [n[0] for i, n in enumerate(wl) if bl[n[1]] >= k]
answer = [el.count(i) if el.count(i) else 0 for i in id_list]