# a = 10
# b = 24
# if a > 0 and b > 0 and isinstance(a, int) and isinstance(b, int):
#     print('OK')
# else:
#     print('Error')


# def abc(a, b):
#     if (not isinstance(a, int) or (not isinstance(b, int))):
#         return print('Error')
#     else:
#         return print('OK')


# print(abc(14.4, 3))


# def route_info(a):
#     if ('distance' in a) and (type(a['distance']) == int):
#         return f"Distance to your destination is {a['distance']}"

#     if ('speed' in a) and ('time' in a):
#         return f"Distance to your destination is {a['speed'] * a['time']}"
#     return 'no'


# print(route_info({'distance': 10}))
# print(route_info({'speed': 90, 'time': 3}))
# my_number = 10.4
# print('is int') if type(my_number) is int else print('is not int')

# my_img = ('1920', '1080', '121')

# print(f"{my_img[0]}x{my_img[1]}" if len(my_img) == 2 else print('Error'))

# if len(my_img) > 2:
#     info = f"{my_img[0]}x{my_img[1]}"
# else:
#     info = 'Error'

# print(info)

# a = 'Its very very very very very veryvery very very very very very very verylong str'

# abc = 'Its long str' if len(a) > 20 else 'not so big'

# print(len(a))
# print(abc)


# for el in [1, 'abc', True]:
#     print(type(el))
#     print(el)


abc = {'id': 24, 'password': 123, 'as': 1211}

for key_abc in abc.items():
    key, value = key_abc
    print(key, value)
