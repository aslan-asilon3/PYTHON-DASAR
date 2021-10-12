def minimum(lst):
    try:
        return min(lst)
    except ValueError:
        print('List tidak berisi data')

z = [30,50,100,240,2]
print(minimum(z))