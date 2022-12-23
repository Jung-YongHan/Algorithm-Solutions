for _ in range(int(input())):
    h, w, n = map(int, input().split())
    if n%h==0:
        floor = h
        room = n//h
    else: 
        floor = n%h
        room = n//h+1
    print(str(floor*100+room))