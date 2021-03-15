
with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    spis = []
    for line in f:
        spis.append((line.split()[0], line.split()[5].strip('"'), line.split()[6]))

print(spis)
