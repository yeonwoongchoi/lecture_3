import random as rd




# def human_vs_monster():
#     print(type(rd.randint(1,3)))
#     monster = rd.randint(1,10)
#     human = rd.randint(1,6)
#     command = input('공격은 hit 입력,무시하기는 ig입력')
#     if(command == 'hit'):
#         if(monster >=human):
#         print('U Lose!')
#         else:
#         print('U Win')
#     elif(command == 'ig'):
#         print('Bye!!')


# human_vs_monster()



# def random_monster():
#     print(type(rd.randint(1,3)))
#     monster = rd.randint(1,10)
#     human = rd.randint(1,6)
#     command = input('공격은 hit 입력,무시하기는 ig')
#     if(command == 'hit'):
#         if(monster >=human):
#             print('U Loose!!')
#         else:
#             print('U Win!!')
#     elif(command == 'ig'):
#         print('Bye!!')

# random_monster

def lotto_number():
    number = list(range(1,46))
    selec_num = rd.randint(1,8)
    first_num = number[rd.randint(1,8)-1]
    second_num = number[rd.randint(9,16)-1]
    third_num = number[rd.randint(17,24)-1]
    fourth_num = number[rd.randint(25,32)-1]
    fifth_num = number[rd.randint(33,40)-1]
    sixth_num = number[rd.randint(41,45)-1]
    
    print('오늘 선택당한 숫자는?!?!')
    print(first_num,second_num,third_num,fourth_num,fifth_num,sixth_num)
lotto_number()