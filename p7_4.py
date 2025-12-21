def raise_to_degrees(number,max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1

res = raise_to_degrees(122345, 50)
print(res)
for _ in res:
    print(_)
    print("----")