

#
# this function generates a question : multiply two algebraic terms  with the same variable  (so x^2)
# e.g 3x(2x)  or -2y(3y)
#

import random 
from sympy import symbols, simplify
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    # question format +/-num1*v1(num2*v1) 
    v1=random.choice(symbols('x y a b'))
    
    num1=random.randint(1,6)
    num2=random.randint(1,6)
    ops = [("+"),("-")]
    
    op1 = random.choice(list(ops))
    op2 = random.choice(list(ops))
    #
    # this next section creates the question (for presentation to the student)
    # and the 2 symby terms which make up the answer
    #
    
    term1=num1*v1    
    if op1=="-":
        term1 = term1* -1
    question=str(term1)
    term2 = num2* v1
    if op2=='-':
        term2=-1*term2
    question=str(question)+str('(')+str(term2)+str(')')
        
    answer=term1*term2        
        
    # this line removes the * in the question for presentation to students.  Currently in form a*x*(b*y)
    question = question.translate({ord(c): None for c in '*'})
    
    return(question)


def get_answer():
    # this method returns the correct answer for the question raised

    answer_str = str(answer)
    return(answer_str)

def get_instruction(): 
    # this method returns the instructions for this topic
    instructions = []
    instructions.append("You need to know that 3x(2x) means 3x multiplied by 2x which equals 6x 'squared'  or 6x^2   ")
    instructions.append("Note that the ^ symbol means 'power' and ^2 means the 'power of 2' or 'squared'. So 3^2 means 3 squared or 3*3=9 ")
    instructions.append("Similarly, a^2 = a times a  or 'a squared' ")
    instructions.append("Example: Multiply 3x(2x): We multiply the 3 by 2 = 6 and we multiply the variables x by x = xx  or x^2 ")
    instructions.append("So 3x(2x) = 6x^2 " )
    instructions.append("And another example  3q(4q)= 12q^2 " )

    instructions.append("In this exercise you can be asked to EXPAND,  SIMPLIFY or just MULTIPLY" )
    instructions.append(" " )
    instructions.append("Another example:  -2d(3d) = -6d^2  "  )
    instructions.append("To get the ^ symbol:   Press shift and the 6 key.  Good luck!  "  )
    
    return(instructions)


    

def get_help(question, answer_sym, effort):
    # this method checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # initiate the help text  
    help_text=""

    # this changes the answer into a sympy expression
    answer_sym=parse_expr(answer_str, transformations=transformations)

    # this converts answers like 4*x**2  to 4x^2 for display to student
    answer_str=str(answer_sym)
    answer_str=answer_str.replace("**","^")
    answer_str=answer_str.replace("*","")
    
    # this changes the student's effort into a sympy expression
    effort=effort.replace("^","**")
    try :
        sym_effort=parse_expr(effort, transformations=transformations)
    except:
        help_text="Your answer is not a proper expression. The answer is : " + answer_str +"."
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                    


    if effort==question :
        help_text="You can't just type in the question!  Multiply it out! The answer is: " + answer_str+"."
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                 
    
    if effort.find('(')>0:
        help_text="There should be no brackets in your answer?  Just Multiply it out.  The answer is: "+answer_str+"."
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

        # if effort and answer have differnt signs 
        if (effort[0]!="-" and answer_str[0]=="-") or (effort[0]=="-" and answer_str[0]!="-"):
 
            if t1[0]=="-" and t2[0]=="-":
                h1="You got the wrong sign. Remember negative by negative equals positive and both "+t1 +" and "+t2 +" are negatives so your answer should be positive."

            elif t1[0]=="-" :
                h1="You got the wrong sign. Remember a negative by a positive equals a negative and "+t1 +" is negative and "+t2 +" is positive"
            elif t2[0]=="-" :
                h1="You got the wrong sign. Remember a negative by a positive equals a negative and "+t2 +"  is negative and "+t1 + "is positive"

        # effort has correcct signs so the multiplication is incorrect
        else:
            h1="You got the multiplication incorrect: "+t1+" * "+t2 +" = "+ answer_str


        help_text="Incorrect:  the correct answer is "+answer_str+".\n" 
        
        help_text=help_text+h1
       
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        




