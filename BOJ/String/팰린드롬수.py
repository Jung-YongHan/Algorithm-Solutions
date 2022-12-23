# 1259

while True:
    try:
        num = list(input())
        if num[0] == '0': 
            break

        l, r = 0, len(num)-1
        is_avl = True
        while l < r:
            if num[l] != num[r]:
                is_avl=False
                break
            l += 1
            r -= 1

        print('yes') if is_avl else print('no')

    except EOFError:
        break