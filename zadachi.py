# функция которая принимает значение в int, работает с этим значением как со строкой, и выдает инт
# def square_digits(num):
#     t1 = ''
#     for i in str(num):
#         t1 += str(int(i)**2)
#     return int(t1)
#
# print(square_digits(521221))


# задачка с тиктока на короновирус
# from turtle import *
# color('green')
# bgcolor('black')
# speed(11)
# hideturtle()
# b = 0
# while b < 200:
#     right(b)
#     forward(b * 3)
#     b += 1


# СРЕЗЫ
# def how_many_years (date1, date2):
#     a = int(date1[:4])
#     b = int(date2[:4])
#     if a > b:
#         c = a - b
#     else:
#         c = b - a
#     return c
#
# print(how_many_years('1221441','199911412'))

# функция должна в итоге получится сумма кубов каждого числа
# def sum_cubes(n):
#     num = 0
#     a = 0
#     while num <= n:
#         b = num ** 3
#         a += b
#         num += 1
#     return a
#
#
# print(sum_cubes(10))


# фунция которая вызывается как add (a)(b) (внутренняя функция)
# def add(a):
#     def adds(b):
#         return a + b
#     return adds

# задача
# def simple_multiplication(number):
#     return number * 8 if number%2==0 else number * 9


# функция переобразования списка в строку с помощью метода .join
# def html_special_chars(data):
#     data1 = []
#     data2 = ''
#     for i in data:
#         if i == '<':
#             i = "&lt;"
#             data1.append(i)
#         elif i == '>':
#             i = '&gt;'
#             data1.append(i)
#         elif i == '"':
#             i = '&quot;'
#             data1.append(i)
#         elif i == '&':
#             i = '&amp;'
#             data1.append(i)
#         else:
#             data1.append(i)
#     print(data1)
#     data2 = ''.join(data1)
#     return data2
#
# print(html_special_chars('<QwQaQd>"Qad&'))

MORSE_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

def decodeMorse(morse_code):
    morse_code = morse_code.split()
    c = []
    n = 1
    a = ''
    for i in MORSE_CODE.values():
        if i == morse_code[:n]:
            c.append(i)
            n += 1
            a = ''.join(c)
        return a
