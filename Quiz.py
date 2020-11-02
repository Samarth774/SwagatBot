# region Quiz
# qfile = open("quiz.txt", "r", encoding="utf8")
# quizdata = qfile.readlines()
# qfile.close()

# question = []
# answers = []
# num = "0123456789"
# que, option = "", []


# def extractQue(que):
#     quecount = que.count("?")
#     defque = ""
#     for x in range(0, quecount):
#         defque += que.split("?")[x]+"?"
#     return defque


# def extractOption(que):
#     que = que.replace("\n", "")
#     # q = que[len(extractQue(que)):]
#     alloption = que.split("(")
#     for x in range(0, len(alloption)):
#         alloption[x] = "("+alloption[x]

#     return alloption[1:]


# def extractAns(option):
#     if option.startwith("(1"):
#         pass
#         # for quiz in range(0, len(quizdata)):
#         #     a = quizdata[quiz].replace("\n", "")
#         #     if a != "":
#         #         quizdata[quiz] = a
#         #     else:
#         #         quizdata.pop(quizdata)

#         # for quiz in quizdata:
#         #     quiz = quiz.replace("\n", "")
#         #     # print(quiz)


#         #     if quiz[:1] in num and quiz != '':
#         #         print("QUE:", quiz)
#         #         questions.append(quiz)
#         #     elif quiz != '':
#         #         print("Option:", extractOption(quiz))
#         #         xa.append(quiz)
# temp = ''
# dic = {"QUE": '', "ANS": []}
# # qutions
# for quiz in quizdata:
#     quiz = quiz.replace("\n", "")
#     que = False

#     for nu in range(0, len(num)):

#         if quiz.startswith(num[nu]):
#             que = True
#             if dic["QUE"] != "":
#                 print(dic)
#                 question.append(dic)
#             dic["QUE"] = ''
#             dic["ANS"] = []
#             dic["QUE"] = (str(nu) + " " + quiz.split(str(nu))[1])

#     if que == False:
#         dic["ANS"].append(extractOption(quiz))

# print(question)
# # print(questions)

# # print("====Quetion====")
# # print(extractQue(guj))
# # print("====Option====")
# # print(extractOption(guj))

# endregion

qfile = open("quiz.txt", "r", encoding="utf8")
quizdata = qfile.readlines()
# quizdata = ""
# for x in qfile.readlines():
#     quizdata += x
# quizdata = quizdata.replace("\n", '')
qfile.close()

# print(quizdata)

# print("="*50)

answers, questions = [], []
write = []


def extractANS():
    with open("answer.txt", 'r') as f:
        for x in f.readlines():
            write.append(int(x))


def extractOption(que):
    que = que.replace("\n", "")
    # q = que[len(extractQue(que)):]
    if not que.startswith("("):
        return
    alloption = que.split("(")
    for x in range(0, len(alloption)):
        alloption[x] = "("+alloption[x]

    return alloption[1:]


lsst = []


def extractQue(que):
    if que.startswith(" "):
        que = ''+que[1:]
    if que.startswith(tuple("0123456789")) and "." in que[1:3]:
        return que


def start():
    tmplist = []
    for x in quizdata:
        x = x.rstrip("\n")
        quee = extractQue(x)

        if x == "##":
            answers.append(tmplist)
            tmplist = []
        elif quee != None:
            if len(tmplist) > 0:
                answers.append(tmplist)
            tmplist = []
            questions.append(quee)
        elif extractOption(x) != None:
            tmplist.extend(extractOption(x))
    extractANS()
    # print(answers)
    # return questions, answers


start()

print(len(questions))
# print(questions[0])
# print(answers[0])
# print(questions[1])
# print(answers[1])
# print(questions[2])
# print(answers[2])
