
#
# this function generates a question : multiply an algebraic expression by an integer
# e.g 3(2x+3y)
#

import random 
from sympy import symbols, simplify
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    # question format +/-num1(num2*v1 +/-num3*v2 +/-num4) 
    # v1 and v2 are used so that we get a variety of variables in the questions
    v1=random.choice(symbols('x a p'))
    v2=random.choice(symbols('y b q'))

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
    term1=num1
    if op1=="-":
        term1 = num1* -1
    question=str(term1)+"("
    term2 = num2* v1
    if op2=='-':
        term2=-1*term2
    question=str(question)+str(term2)
        
    term3 = num3* v2
    if op3=='-':
        term3=-1*term3
        question=str(question)+str(term3)
    else:
        question=str(question)+str("+")+str(term3)
        

    # the 4th term can be a constant, including 0
    # if it is 0, then I leave it out of the expressions

    term4 = num4
    if num4>0:
        
        if op4=='-':
            term4=-1*num4
            question=str(question)+str(term4)+")"
        else: 
            question=str(question)+str("+")+str(num4)+")"
        
        answer=term1*(term2+ term3 +term4)        
        
    if num4==0:
        answer=term1*(term2+ term3)
        question=str(question)+")"

    # this line removes the * in the question for presentation to students
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
    instructions.append("You need to know that 3(2x) means 3 multiplied by 2x which equals 6x  ")
    instructions.append("Similarly, 4(3x + 2y) means 4 multiplied by 3x and 4 multiplied by 2y ")
    instructions.append("and this is equal to 12x + 8y.   The 4 outside the brackets multiplies by everything inside" )
    instructions.append(" " )
    instructions.append("In this exercise you are asked to EXPAND the brackets or SIMPLIFY " )
    instructions.append("Here is another example:  Expand  3(2a-3b+5) " )
    instructions.append("This equals :  6a-9b+15   " )
    instructions.append(" " )
    instructions.append("Expand -3(2a-4b)   This equals -6a + 12b" )
    instructions.append("So, you need to know that minus by minus equals plus... good luck!  "  )
    
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
            if answer_list[i] not in (effort_list):
                 h2.append("You dont have the "+str(answer_list[i]) +" term correct. ")
               
        h2_clean=str(h2)
        h2_clean=h2_clean.replace(']','')
        h2_clean=h2_clean.replace('[','')
        h2_clean=h2_clean.replace("'","")
        
        
        '''

        POSSIBLY OF USE LATER WHEN I NEED TO IMPROVE FEEDBACK
        
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
          
        '''
        
        help_text="Incorrect:  the correct answer is "+str(answer_str)+".\n" 
        if h1!="": help_text=help_text+ str(h1)
        if h2!="": help_text=help_text+ "\n"+ str(h2_clean)
       
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        




