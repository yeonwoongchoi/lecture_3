import math as mt

# def math_pow():
#     for i in range(2,11):
#         result = mt.pow(4,i)
#         result_words = '4**{} ={}'.format(i,result)
#         print(result_words)

# math_pow()



def math_pow_input(n=None):
    number = int(input('숫자를 입력하세요'))
    for i in range(2,11):
        result = mt.pow(number,i)
        result_words = '{}**{} ={}'.format(number,i,result)
        print(result_words)
