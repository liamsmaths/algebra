
#
# this function generates a question : adding like terms with more than 1 variable  e.g 3a+4b-2a+5b
#
#  NEED To complete HELP method

import random
import operator
from sympy import symbols, simplify
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application
from sympy.parsing.sympy_parser import parse_expr
transformations = (standard_transformations +
                   (implicit_multiplication_application,))


def get_question():
    global question, answer

    # v1 and v2 are used so that we get a variety of variables in the questions
    v1 = random.choice(symbols('x a p'))
    v2 = random.choice(symbols('y b q'))

    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)
    num4 = random.randint(1, 5)

    ops = {'+': operator.add, '-': operator.sub}
    op2 = random.choice(list(ops.keys()))
    op3 = random.choice(list(ops.keys()))
    op4 = random.choice(list(ops.keys()))

    #
    # this next section creates the question (for presentation to the student)
    # and the 4 symby terms which make up the answer
    # note the terms don't initially include a '+' if the term is positive so I had to add a '+' in
    #
    term1 = num1 * v1
    question = term1
    term2 = num2 * v2
    if op2 == '-':
        term2 = -1*term2
        question = str(question)+str(term2)
    else:
        question = str(question)+str("+")+str(term2)

    term3 = num3 * v1
    if op3 == '-':
        term3 = -1*term3
        question = str(question)+str(term3)
    else:
        question = str(question)+str("+")+str(term3)

    term4 = num4 * v2
    if op4 == '-':
        term4 = -1*term4
        question = str(question)+str(term4)
    else:
        question = str(question)+str("+")+str(term4)

    # this line removes the * in the question for presentation to students
    question = question.translate({ord(c): None for c in '*'})

    # this is the answer - sympy form.. with '*'
    answer = term1+term2+term3+term4

    return(question)


def get_answer():
    # this method returns the correct answer for the question raised
    return(answer)


def get_instruction():
    # this method returns the instructions for this topic
    instructions = []
    instructions.append(
        "Just like in the previous exercises if we are asked to  ")
    instructions.append("Simplify:   1x+3x+5a-2a ")
    instructions.append("We add up the x's and then we add up the y's ")
    instructions.append("In this case, we get 1x+3x=4x and 5a-2a=3a ")
    instructions.append("so the answer is 4x+3a")
    instructions.append(" ")
    instructions.append("Again, note x=1x   and a=1a etc  ")
    instructions.append("So, If you are asked to simplify a+2a+b-3b")
    instructions.append("The answer is 3a-2b   ")

    return(instructions)


def get_help(question, answer, effort):
    # this method checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # initiate the help text
    help_text = ""

    # this parses the student's effort into a sympy expression
    sym_effort = parse_expr(effort, transformations=transformations)

    # this line removes the * in the answer for presentation to students
    answer_str = str(answer)
    answer_str = answer_str.translate({ord(c): None for c in '*'})

    if simplify(answer-sym_effort) == 0:
        return("correct")

    else:
        # get variables from question
        q = question.translate({ord(c): None for c in '12345'})
        var1 = q[0]
        var2 = q[2]

        # get coefficients in answer...  this method finds the variable (var1 or var2) of power 1
        dig1 = answer.coeff(var1, 1)
        dig2 = answer.coeff(var2, 1)
        # (dig1, var1, dig2, var2) - this is the set of variables which comprise the answer

        # now compare to the effort and diagnose the problem(s)
        # firstly, check the correct variable(s)
        vars_ok, var1_ok, var2_ok = 1, 1, 1

        if dig1 > 0 and var1 not in effort:
            var1_ok = 0
        if dig2 > 0 and var2 not in effort:
            var2_ok = 0
        if var1_ok == 1 and var2_ok == 1:
            vars_ok = 1  # variables are ok
        else:
            help1 = "To start with you You didn't use the correct variables!  ", var1, " and ", var2

        '''
        # now check the digits.. but only proceed if they got the correct variable(s)
        # we know they have the the digits incorrect 
        if vars_ok==1:
            # find operator positions
            a,b=0,0
            pos_plus=[]
            pos_minus=[]
            plus_count=question.count("+")
            minus_count=question.count("-")
            for i in range (plus_count):
                a=question.find("+",a)
                pos_plus.append(a)
            for i in range (minus_count):
                b=question.find("-",b)
                pos_minus.append(b)

            print (pos_minus)
            print (pos_plus)
        '''

        if vars_ok == 0:
            help_text = help1
        help_text = help_text + "Incorrect:  the correct answer is "+str(answer_str)+" \n \
        So, you just need to add or subtract the numbers in the question " + str(question) + "\n \
        And just like 1 apple - 1 apple = 0 apples (or just 0) \n \
        Remember x is the same as 1x, so x+x=2x "

        return (help_text)
