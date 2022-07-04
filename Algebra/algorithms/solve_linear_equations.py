

#
# This function generates a linear equation - e.g.  3x+1=10  (The coefficient will always be positive)
#  
#

import random 
from sympy import symbols, simplify
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application, parse_expr
transformations = (standard_transformations +(implicit_multiplication_application,))



def get_question():
    global question, answer

    v1=random.choice(symbols('x y a b p r'))
    
    num1=random.randint(1,6)
    list=(-2,-1,1,2,3,4)
    num2=random.choice(list)
    sol_num=random.randint(1,6)
    result_num=num1*sol_num+num2
      
    #
    # this next section creates the question (for presentation to the student)
    # and the 2 symby terms which make up the answer
    #
    
    # the next 2 lines deal with the sign of num2
    snum2=num2
    if num2>0: snum2=str("+")+str(num2) 
    question="solve :"+str(num1)+str(v1)+str(snum2)+str('=')+str(result_num)
    # this line removes the * in the question for presentation to students.  Currently in form a*x*(b*y)
    question = question.translate({ord(c): None for c in '*'})

    answer=sol_num     
       
    return(question)


def get_answer():
    # this method returns the correct answer for the question raised

    answer_str = str(answer)
    return(answer_str)

def get_instruction(): 
    # this method returns the instructions for this topic
    instructions = []
    instructions.append("When you are asked to 'solve' and equation, you need to work out the value of the variable(s) which    ")
    instructions.append("satisfy the equation.  e.g. Solve:  2x+5=11   ")
    instructions.append("So, what value must x be to 'satisfy' the equation? The answer is 3 because 2*3 + 5=11.   ")
    instructions.append("But we need a way to do these questions when they aren't so simple.  " )
    instructions.append("ok. here is a way you can use: " )
    instructions.append("Solve   2x + 1 = 9 " )
    instructions.append("            -1   -1  subtract 1 from each side of the equation " )
    instructions.append("     => 2x     = 8"  )
    instructions.append("        /2        /2  divide both sides by 2 "  )
    instructions.append("     =>  x     = 4   "  )
    
    return(instructions)


    

def get_help(question, answer, effort):
    # this method checks the answer(passed to this as a string) against the student effort and returns
    # either correct or help with what they did wrong
    # question:   solve:  3x+4=13
    # answer :    3
    # effort :    3 (hopefully)

    # initiate the help text  
    help_text=""

        
    if effort==question :
        help_text="You can't just type in the question!  solve it! The answer is: " + answer+"."
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                 
    
    if effort.find('(')>0:
        help_text="There should be no brackets in your answer?  You need to solve it.  The answer is: "+answer+"."
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                 


    if answer == effort:
        is_correct = True
        help_text="Correct, well done"
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
        
    else:
        # the student effort is incorrect 
        # get the various terms from the question 
        q_t1=question[7:9]
        q_t1_num=int(q_t1[0:len(q_t1)-1])
        equals=question.find("=")
        q_t2=int(question[9:equals])
        q_sol=int(question[equals+1:])
        if q_t2<0: 
            q_t2_sign="neg"
            action1=" add "
            action2=" to "
            state=" negative "
        else: 
            q_t2_sign="pos"
            action1=" subtract "
            action2=" from"
            state=" positive "
       



        question1=question[7:]
        h1="Incorrect:  The answer is "+str(answer) +"." 
        h2=" We start by getting rid of the "+str(q_t2) +" from the equation.  As "+ str(q_t2) +" is "+ str(state) +" we "  
        h2=h2+action1 +" it (" +str(q_t2)+")"+action2 +" both sides.  This gives us:" + str(q_t1) +"=" +str(q_sol-q_t2)  +"."
        if q_t1_num==1:
            h2 =h2+" So we now know that the answer " +q_t1[1:] +"="+str(answer)
        else:
            h2=h2+" Then we need to divide both sides by "+str(q_t1[0:len(q_t1)-1])+" which gives us the answer "+q_t1[1:] +"="+str(answer)
        help_text=help_text+h1 +h2
       
              
        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response                      
        
            
        




