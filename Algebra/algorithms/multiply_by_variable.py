#
# this function generates a question : multiply an algebraic expression by a variable
# e.g 3x(2x+3y)  or 2x(3x+2p+4)
#

import random 
from sympy import *
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    # question format +/-num1*v1(or v2)(num2*v1 +/-num3*v2 +/-num4) 
    # v1, v2, V3 are used so that we get a variety of variables in the questions
    v1=random.choice(symbols('x y'))
    v2=random.choice(symbols('x a p'))
    v3=random.choice(symbols('y b q'))

    num1=random.randint(2,5)
    num2=random.randint(1,5)
    num3=random.randint(1,5)
    num4=random.randint(0,3)
    
    ops = [("+"),("-")]
    
    op1 = random.choice(list(ops))
    op2 = random.choice(list(ops))
    op3 = random.choice(list(ops))
    op4 = random.choice(list(ops))

    #
    # this next section creates the question (for presentation to the student)
    # and the 4 symby terms which make up the answer
    # note the terms don't initially include a '+' if the term is positive so I had to add a '+' in
    #
    term1=Mul(num1,v1)
    
    if op1=="-":
        term1 = Mul(term1, -1)
    question=str(term1)+"("
    term2 = Mul(num2, v2)
    if op2=='-':
        term2=Mul(-1,term2)
    question=str(question)+str(term2)
        
    term3 = Mul(num3, v3)
    if op3=='-':
        term3=Mul(-1,term3)
        question=str(question)+str(term3)
    else:
        question=str(question)+str("+")+str(term3)
        

    # the 4th term can be a constant, including 0
    # if it is 0, then I leave it out of the expressions

    term4 = num4
    if num4>0:

        if op4=='-':
            term4=Mul(-1,num4)
            question=str(question)+str(term4)+")"
        else: 
            question=str(question)+str("+")+str(num4)+")"
        
        answer=Add(Mul(term1,term2), Mul(term1,term3), Mul(term1,term4))        
    if num4==0:
        answer=term1*term2+ term1*term3
        question=str(question)+")"

    # this line removes the * in the question for presentation to students
    question = question.translate({ord(c): None for c in '*'})
    #print ("ts  ", term1,term2,term3,term4)
    #print ("q  ",question)  
    #print ("ans... ",answer)
   
    return(question)


def get_answer():
    # this method returns the correct answer for the question raised

    # this line removes the * in the answer for presentation to students
    answer_str = str(answer)

    return(answer_str)

def get_instruction(): 
    # this method returns the instructions for this topic
    instructions = []
    instructions.append("This exercise is very similar to previous ones...    ")
    instructions.append("You need to know that 3a(2x) means 3a multiplied by 2x which equals 6ax  (or 6xa.. same thing)  ")
    instructions.append("Similarly, 4a(3x + 2y) means 4a multiplied by 3x and 4a multiplied by 2y ")
    instructions.append("and this is equal to 12ax + 8ay.   The 4a outside the brackets multiplies by everything inside" )
    instructions.append(" " )
    instructions.append("In this exercise you might be asked to EXPAND the brackets or SIMPLIFY " )
    instructions.append("Here is another example:  Expand  3a(2a-3b+5) " )
    instructions.append("This equals :  6a^2-9ab+15a   " )
    instructions.append(" " )
    instructions.append("Expand -3a(2a-4b)   This equals -6a^2 + 12ab" )
    instructions.append("So, you need to know that minus by minus equals plus... good luck!  "  )
    
    return(instructions)


    

def get_help(question, answer_str, effort):
    # this method checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # initiate the help text  
    help_text=""

    # this parses the answer back into a sympy expression
    answer_sym=parse_expr(answer_str, transformations=transformations)
    srepr(answer_sym)
    
    # this changes the student's effort into a sympy expression
    effort=effort.replace("^","**")
    try :
        sym_effort=parse_expr(effort, transformations=transformations)
    except:
        txt=answer_str.replace("**","^")
        txt=txt.replace("*","")
        help_text="Your answer is not a proper expression. The answer is : " + txt +"."
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
        # the student effort is incorrect

        # count the number of terms in the answer
        answer_list=answer_str.replace(" ","")
        answer_list=answer_list.replace("-"," -")
        answer_list=answer_list.replace("+"," +")
        # split returns a list of words 
        answer_list = answer_list.split()
        numterms_answer=len(answer_list)

        # count number of terms in the effort
        effort_list=effort.replace('-',' -')
        effort_list=effort_list.replace('+',' +')
        effort_list = effort_list.split()
        numterms_effort=len(effort_list)

        # at a minimum the effort should have the same number of terms
        h1,h2="",""
        if numterms_effort!=numterms_answer:
            h1=" For starters, you should have "+str(numterms_answer)+ " terms.  You have "+ str(numterms_effort)+"."

        # now compare each term
        h2=[]
        for i in range(numterms_answer):
            sym_ans_term=parse_expr(answer_list[i], transformations=transformations)
            for j in range(numterms_effort):
                sym_effort_term=parse_expr(effort_list[j], transformations=transformations)               

                if simplify(sym_ans_term-sym_effort_term==0):
                    txt=answer_list[i].replace("**","^")
                    txt=txt.replace("*","")
                    h2.append("You have the "+txt +" term correct. Good! ")
               
        h2_clean=str(h2)
        h2_clean=h2_clean.replace(']','')
        h2_clean=h2_clean.replace('[','')
        h2_clean=h2_clean.replace("'","")
        
       
        answer_str=answer_str.replace("**","^")
        answer_str=answer_str.replace("*","")

        help_text="Incorrect:  the correct answer is "+str(answer_str)+".\n" 
        if h1!="": help_text=help_text+ str(h1)
        if h2!="": help_text=help_text+ "\n"+ str(h2_clean)
       
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        




