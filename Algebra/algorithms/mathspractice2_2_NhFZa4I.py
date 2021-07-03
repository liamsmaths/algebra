#
#  Expand brackets :(ax+by)^2
#


def get_question():
    # return "this method returns a unique question"
    import random
    import operator

    num1 = random.randint(1, 3)
    num2 = random.randint(1, 4)
    ops = {'+': operator.add, '-': operator.sub}
    op = random.choice(list(ops.keys()))

    question = "(" + str(num1) + "x" + op + str(num2)+"y)^2"
    print(question)

    return(question)


# get_question()
def get_answer():
    return "this method returns an ans"


def get_hint():
    return "this method returns an instruction to solve the question generated above"


def get_instruction():
    return "this returns an instruction to solve the questions"
