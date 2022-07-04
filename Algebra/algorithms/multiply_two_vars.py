

#
# this function generates a question : multiply two algebraic terms
# e.g 3x(2x)  or 2x(3y)
#

import random 
from sympy import symbols, simplify
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    # question format +/-num1*v1(or v2)(num2*v1 +/-num3*v2 +/-num4) 
    # v1 and v2 are used so that we get a variety of variables in the questions
    v1=random.choice(symbols('x a p'))
    v2=random.choice(symbols('y b q'))

    num1=random.randint(2,5)
    num2=random.randint(1,5)
    ops = [("+"),("-")]
    
    op1 = random.choice(list(ops))
    op2 = random.choice(list(ops))
    #
    # this next section creates the question (for presentation to the student)
    # and the 4 symby terms which make up the answer
    # note the terms don't initially include a '+' if the term is positive so I had to add a '+' in
    #
    
    term1=num1*v1    
    if op1=="-":
        term1 = term1* -1
    question=str(term1)+"*"
    term2 = num2* v2
    if op2=='-':
        term2=-1*term2
    question=str(question)+str('(')+str(term2)+str(')')
        
    answer=term1*term2        
        
    # this line removes the * in the question for presentation to students
    #question = question.translate({ord(c): None for c in '*'})
       
    # this line removes the * in the question for presentation to students.  Currently in form a*x*(b*y)
    question = question.translate({ord(c): None for c in '*'})
    
    return(question)


def get_answer():
    # this method returns the correct answer for the question raised

    # this line removes the * in the answer for presentation to students
    answer_str = str(answer)
    answer_str = answer_str.translate({ord(c): None for c in '*'})
 
    return(answer_str)

def get_instruction(): 
    # this method returns the instructions for this topic
    instructions = []
    instructions.append("You need to know that 3p(2x) means 3p multiplied by 2x which equals 6px  ")
    instructions.append("How is this done?: We multiply the 3 by 2 = 6 and we multiply the variables p by x = px ")
    instructions.append("You also need to know that a*a = a^2  (a squared) " )
    instructions.append("so  2q(3q)=6q^2 " )

    instructions.append("In this exercise you are asked to EXPAND the brackets or SIMPLIFY " )
    instructions.append(" " )
    instructions.append("Expand -3a(4b)   This equals -12ab" )
    instructions.append("Another example:  -2d(3d) = -6d^2  "  )
    instructions.append("The ^ symbol means squared.  Press shift and the 6 key.  Good luck!  "  )
    
    return(instructions)


    

def get_help(question, answer_str, effort):
    # this method checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # initiate the help text  
    help_text=""

    # this parses the student's effort into a sympy expression
    effort=effort.replace("^","**")
    try :
        sym_effort=parse_expr(effort, transformations=transformations)
    except:
        help_text="Your answer is not a proper expression. The answer is : " + answer_str
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                    

    # this parses the answer back into a sympy expression
    answer_sym=parse_expr(answer_str, transformations=transformations)

    if effort==question :
        help_text="You can't just type in the question!  Multiply it out! The answer is: " + answer_str
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                 
    
    if effort.find('(')>0:
        help_text="There should be no brackets in your answer?  Just Multiply it out.  The answer is: "+answer_str
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                 


    if simplify(answer_sym-sym_effort) == 0:
        is_correct = True
        help_text="Correct, well done"
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
        
    else:
        # the student effort is incorrect  (and not just a copy of the question which will cheat sympy!)
        # get the 2 terms from the question 
        h1=""
        t1=question[0:question.find('(')]
        t2=question[question.find('(')+1:-1]
        
        if t1[0]=="-" and t2[0]=="-":
            h1=" Remember negative by negative equals positive and both "+t1 +" and "+t2 +" are negatives"

        elif t1[0]=="-" or t2[0]=="-":
            h1=" Remember a negative by a positive equals a negative and one of  "+t1 +" or "+t2 +" is negative"

        help_text="Incorrect:  the correct answer is "+answer_str+".\n" 
        help_text=help_text+" which we get by multiplying "+t1 +" by "+t2
        help_text=help_text+h1
       
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        




