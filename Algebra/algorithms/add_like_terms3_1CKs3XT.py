
#
# this function generates a question : adding like terms with more than 1 variable  e.g 3a+4b-2a+5b
#
#  NEED To complete HELP method 

import random 
from sympy import symbols, simplify
#from sympy import *
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
#from sympy.parsing.sympy_parser import parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    # v1 and v2 are used so that we get a variety of variables in the questions
    v1=random.choice(symbols('x a p'))
    v2=random.choice(symbols('y b q'))

    num1=random.randint(1,5)
    num2=random.randint(1,5)
    num3=random.randint(1,5)
    num4=random.randint(1,5)
    
    ops = [("+"),("-")]
    
    op2 = random.choice(list(ops))
    op3 = random.choice(list(ops))
    op4 = random.choice(list(ops))

    #
    # this next section creates the question (for presentation to the student)
    # and the 4 symby terms which make up the answer
    # note the terms don't initially include a '+' if the term is positive so I had to add a '+' in
    #
    term1 = num1* v1
    question=term1
    term2 = num2* v2
    if op2=='-':
        term2=-1*term2
        question=str(question)+str(term2)
    else:
        question=str(question)+str("+")+str(term2)
        
    term3 = num3* v1
    if op3=='-':
        term3=-1*term3
        question=str(question)+str(term3)
    else:
        question=str(question)+str("+")+str(term3)
        
    
    term4 = num4* v2
    if op4=='-':
        term4=-1*term4
        question=str(question)+str(term4)
    else: 
        question=str(question)+str("+")+str(term4)

    # this line removes the * in the question for presentation to students
    question = question.translate({ord(c): None for c in '*'})
 
    # this is the answer - sympy form.. with '*' 
    answer=term1+ term2+ term3+ term4 
     
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
    instructions.append("Just like in the previous exercises if we are asked to  ")
    instructions.append("Simplify:   1x+3x+5a-2a ")
    instructions.append("We add up the x's and then we add up the y's " )
    instructions.append("In this case, we get 1x+3x=4x and 5a-2a=3a " )
    instructions.append("so the answer is 4x+3a" )
    instructions.append(" " )
    instructions.append("Again, note x=1x   and a=1a etc  " )
    instructions.append("So, If you are asked to simplify a+2a+b-3b"  )
    instructions.append("The answer is 3a-2b   "  )
    
    return(instructions)


    

def get_help(question, answer_str, effort):
    # this method checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # initiate the help text  
    help_text=""
     
    # this parses the student's effort into a sympy expression
    sym_effort=parse_expr(effort, transformations=transformations)

    # this parses the answer back into a sympy expression
    answer_sym=parse_expr(answer_str, transformations=transformations)

         
    if simplify(answer_sym-sym_effort) == 0:
        is_correct = True
        help_text="Correct, well done"
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
 
    else:
        # the student effort is incorrect
        # get variables from question
        q = question.translate({ord(c): None for c in '12345'})
        var1=q[0]
        var2=q[2]
        
        #get coefficients in answer...  this method finds the variable (var1 or var2) of power 1
        dig1=answer_sym.coeff(var1,1)
        dig2=answer_sym.coeff(var2,1)
        #(dig1, var1, dig2, var2) - this is the set of variables which comprise the answer

            
        # now compare to the effort and diagnose the problem(s)
        # firstly, check the correct variable(s)
        vars_ok,var1_ok,var2_ok=1,1,1
        h1,h2,h3="","",""
        if dig1>0 and var1 not in effort:
            var1_ok=0
        if dig2>0 and var2 not in effort:
            var2_ok=0
        if var1_ok==1 and var2_ok==1 :
            vars_ok=1   #variables are ok
        else:
            h1="To start with you You didn't use the correct variables!  "+str(var1)+ " and "+ str(var2)
            vars_ok=0

        
        # now check the digits.. but only proceed if they got the correct variable(s)
        # we know they have the the digits incorrect 
        if vars_ok==1:
            
            # use answer_sym (dig1, var1, dig2, var2) and sym_effort 
            sym_effort_dig1=sym_effort.coeff(var1,1)
            sym_effort_dig2=sym_effort.coeff(var2,1)
            if sym_effort_dig1!=dig1:
                h2="You got the coefficient for the variable "+ str(var1)+ " wrong. You got "+ str(sym_effort_dig1)+ " and it should be "+ str(dig1) 
            if sym_effort_dig2!=dig2:
                h3="You got the coefficient for the variable "+ str(var2)+ " wrong. You got "+ str(sym_effort_dig2)+ " and it should be "+ str(dig2)
          
        
        
        help_text="Incorrect:  the correct answer is "+str(answer_str)+" \n" 
        if vars_ok==0: help_text=help_text+ str(h1)
        if h2!="": help_text=help_text+ "\n"+ str(h2)
        if h3!="": help_text=help_text+" \n"+ str(h3)
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        
    




