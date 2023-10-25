  # practice 1-1
def Function1_1(list):
    list = [10, 15, 21, 28, 33, 40]
    list_output = []
    for element in list:
        if element%2==0:
            list_output.append(element)
    print (list_output)

Function1_1([10, 15, 21, 28, 33, 40])

  # practice 1-2
def Function1_2(list, sequence):
    print(sorted(list, key = lambda x: x, reverse = True)[sequence-1])  # key 可省略

Function1_2([10, 40, 30, 20, 50], 2)

  # practice 2
def Function2(scores):
    top_score = 0
    for score in scores:
        if top_score<(sum(score[1:])/len(score[1:])):
            top_score=(score[1]+score[2]+score[3])/3
    print (top_score)

scores = (
        ('Justin', 89, 90, 100), 
        ('Tom', 92, 87, 100), 
        ('Jane', 90, 90, 100), 
        ('Philip', 89, 95, 100)
    )
Function2(scores)

  # practice 3-1
def Function3_1(dict, quantity):
    dict = {'a':5, 'b': 1, 'c': 3, 'd': 4, 'e': 2}
    ranked_list = sorted(dict.items(), key=lambda x: x[1], reverse=True)[:quantity]
    print ([data[0] for data in ranked_list])

Function3_1({'a':5, 'b': 1, 'c': 3, 'd': 4, 'e': 2}, 3)

  # practice 3-2
def Function3_2(dict, value):
    dict = {1: 'Apple', 2: 'Orange', 3:'Pineapple', 4: 'watermalon'}
    for i in range(1,len(list(dict))):
        if len(dict[i])<value: 
            del dict[i]
    print (dict)

Function3_2({1: 'Apple', 2: 'Orange', 3:'Pineapple', 4: 'watermalon'}, 6)