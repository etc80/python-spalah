print("Пообщайся со мной! Когда надоест, просто напиши 'пока'")

answers = {
    "привет": ["привет!", "здоровa!", "хай!", "ку", "прив!", "добрый вечер!"],
    "что делаешь?": ["ничего", "туплю"],
    "пока": ["пока", "бывай", "бай", "ну и ладно", "адью", "чао", "ну пока, коли не шутишь"],
    }


def randomize_list(list, randomizer):
    list_len = len(list)
    if(randomizer > list_len):
        return randomizer - ((randomizer) // list_len * list_len)
    else:
        return list_len - ((list_len) // randomizer * randomizer)


while True:
    question = input(">> ")
    if(question == 'пока'):
        print(answers['пока'][randomize_list(answers['пока'], len(question))])
        break
    ans_list = answers.get(question)
    rand_num = 0
    if(ans_list == None):
        answers.setdefault(question, [])
        print("...")
    elif(len(ans_list) == 0):
        print("мало данных")
    else:
        print(ans_list[randomize_list(ans_list, len(question))])
        rand_num = randomize_list(ans_list, len(question))
    if(rand_num % 2 == 0):
        what_to_ask = []
        for key in answers.keys():
            if(key[len(key)-1] == "?"):
                what_to_ask.append(key)

        start_point = randomize_list(what_to_ask, len(question))
        q = what_to_ask[start_point]
        print(q)
        answer = input(">>")
        answers[q].append(answer)
