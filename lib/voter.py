
# opts = [
#     [
#         "choose type of authentication",
#         [
#         "cookie",
#         "credentials",
#         "nothing"
#         ]
#     ],
#         [
#         "choose type of authentication",
#         [
#         "cookie",
#         "credentials",
#         "nothing"
#         ]
#     ],
# ]

def askForOptions(options: list):
    answers = []
    for opt in options:
        print(opt[0])
        for k in range(len(opt[1])):
            print(str(k)+" -",opt[1][k])
        inp = input(":")
        if inp=="":inp=1
        answers.append(inp)
    return answers
