#
#  Expand brackets :(ax+by)^2
#

import random
import operator
import math
#from sympy import symbols, simplify

def get_question(): 
    global num1, num2, op, question, answer
    
    num1=random.randint(1,3)
    num2=random.randint(1,4)
    ops = {'+':operator.add,'-':operator.sub }
    op = random.choice(list(ops.keys()))
    question = "(" + str(num1)+ "x" +op +str(num2)+"y)^2"
    
    return(question)


def get_answer():
    
    # this method returns answer to the specific question that was generated before
    answer=str(num1*num1)+"x^2" +str(op) +str(2*num1*num2)+"xy+" +str(num2*num2)+"y^2"
    return(answer)


def get_instruction(): 
    # this method returns the instructions for this topic
    eg1= f"(x+2y)\u00B2"
    xsquared = f"x\u00B2"
    ysquared = f"4y\u00B2"
    instr1= "When expanding brackets like, " +eg1+ " this is the same as "
    instr2=" Note:  You cant type the " + xsquared 
    
    instructions=[]
    instructions.append(instr1)
    instructions.append(" ")
    instructions.append("(x+2y)(x+2y)  which equals...")
    instructions.append(" x(x+2y)  + 2y(x+2y)   which equals ")
    instructions.append(" x*x  + x*2y  + 2y*x + 2y*2y  which equals  ")
    instructions.append(xsquared +"+4xy+"+ysquared)
    instructions.append(instr2 )
    instructions.append(" so you need to type x^2 and the same for y^2  ")
    instructions.append(" Get the ^ symbol by pressing <shift> and 6 ")

    return(instructions)


def get_help(question, answer, effort):
     
    # this method returns some help based on their effort

    # clean up effort in case they used brackets and spaces
    chars_to_remove = "()' '"
    for character in chars_to_remove:
      effort = effort.replace(character, "")

    # get the num1 and num2 from the question  (ax+by)^2
    num1=int(question[1])
    num2=int(question[4:5])
    op=question[3]

    
    #
    #  compare the 3 terms of solution and the operator (only the 2nd one as I use + for 1st coefficient ) vs student effort
    #

    term1=(str(num1*num1)+"x^2")
    term2=op+(str(2*num1*num2)+"xy")     # this adds the + or - to term2
    term2_2=op+(str(2*num1*num2)+"yx")
    term3=("+"+str(num2*num2)+"y^2")
    
    t1ok=0  # this sets correct terms flags=0
    t2ok=0
    t3ok=0

    if (effort.find(term1))>=0:
        t1ok=1
    elif (num1==1):  # take 1x^2 or x^2 as correct
        if (effort.find("x^2"))==0:   #  ie finds it at position 0 .. so this will fail nx^2 when n <>1
           t1ok=1
    
    if (effort.find(term2))>=0:
        t2ok=1
    elif (effort.find(term2_2))>=0:
        t2ok=1

    if (effort.find(term3))>=0:
        t3ok=1
    elif (num2==1):   # take 1y^2 or y^2 as correct
        effort_findnum=effort.find("y^2")-1
        if ((effort.find("y^2"))>=0 and (effort[effort_findnum]=="+")):  # there must be a y^2 and the character before is a +
            t3ok=1
    
    #  so if the 3 terms are found (=1) then the student effort is correct        
    if (t1ok==1 and t2ok==1 and t3ok==1):
        is_correct = True
        help_text="Correct, well done"
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
        

    else :  # the student effort was incorrect - give some feedback 
        help_text=""
        if t1ok==0:
            help_text="You got the 1st term wrong... The coefficient should be "+str(num1*num1)+" \n" \
                            " which you get by squaring " +str(num1) 
                            
        if t2ok==0:
            help_text=help_text+"\n\n You got the 2nd term wrong... The coefficient should be "+str(2*num1*num2)+" \n" \
                            "which you get by multiplying 2 * :" +str(num1) +" * "+str(num2) +" and then just type in xy"

        if t3ok==0:
            help_text=help_text+"\n\n You got the 3nd term wrong... It should be " +term3 +" the coefficient should be "+str(num2*num2)+" \n" \
                            "which you get by multiplying :" +str(num2) +" * "+str(num2) +" and then the y^2"
      

        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
        





    

