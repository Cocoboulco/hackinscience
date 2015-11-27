f = "abcdefghijklmnopqrstuvwxyz"
for a in range(0, 26): 
    for b in range(a+1, 26):
        print(f[a] + f[b])
