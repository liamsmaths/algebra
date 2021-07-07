#
#  Expand brackets :(ax+by)^2
#

import random
import operator
#from sympy import symbols, simplify

def get_question(): 
    global num1, num2, op, question
    num1=random.randint(1,3)
    num2=random.randint(1,4)
    ops = {'+':operator.add,'-':operator.sub }
    op = random.choice(list(ops.keys()))
    question = "(" + str(num1)+ "x" +op +str(num2)+"y)^2"
    return(question)


def get_answer():
    global answer
    # this method returns answer to the specific question that was generated before
    answer=str(num1*num1)+"x^2" +str(op) +str(2*num1*num2)+"xy+" +str(num2*num2)+"y^2"
    return(answer)


def get_instruction(): 
    # this method returns the instructions for this topic
    eg1= f"(x+2y)\u00B2"
    xsquared = f"x\u00B2"
    eg2= f"x\u00B2 +4xy+ 4y\u00B2"

    instructions = """ When expanding brackets like   """ + "\n" + eg1 + "\n" +"\n"+ "this is the same as " \
    "\n" +"(x+2y)(x+2y) \n   " \
    " \n = x(x+2y)  + 2y(x+2y)   \n  \n = x*x  + x*2y  + 2y*x + 2y*2y   \n \n \
    = x^2 + 4xy + 4y^2 \n \n" \
    "Note:  You cant type the " +xsquared +" \
    so you need to type x^2 and the same for y^2  \n Get the ^ symbol by pressing <shift> and 8.   \n "

    return(instructions)


def get_help(effort):
    
    # this method returns an auto-generated help based on the question and answer
    if len(effort)<6:
        return("error, Your response is too short")  # if they click on check without entering anything sufficient
    
    chars_to_remove = "()' '"
    for character in chars_to_remove:
      effort = effort.replace(character, "")

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
        return("correct") 

    else :  # the student effort was incorrect - give some feedback 
        helptext=""
        if t1ok==0:
            helptext="You got the 1st term wrong... The coefficient should be "+str(num1*num1)+" \n" \
                            " which you get by squaring " +str(num1) 
                            
        if t2ok==0:
            helptext=helptext+"\n\n You got the 2nd term wrong... The coefficient should be "+str(2*num1*num2)+" \n" \
                            "which you get by multiplying 2 * :" +str(num1) +" * "+str(num2) +" and then just type in xy"

        if t3ok==0:
            helptext
            helptext=helptext+"\n\n You got the 3nd term wrong... It should be " +term3 +" the coefficient should be "+str(num2*num2)+" \n" \
                            "which you get by multiplying :" +str(num2) +" * "+str(num2) +" and then the y^2"
        
    return(helptext)





    

