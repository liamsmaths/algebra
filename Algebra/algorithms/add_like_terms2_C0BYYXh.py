
import random


#
# this function generates a question : adding 2 and 3 like terms (and constants) with where some answers are negative and zero
#

def get_question():
    global question, answer 
        
    q_list=("x-2x","3y-5y","3a+a","3p+2p-5p","2a+a-5a", "5x-2x-3x", "c+c-5c", "b+b+b+5+2", "2d+2d+3d-2d", "4a+3b-4", "a+2a+5", "2+4x+x+3")
    ans_list=("-x","-2y","4a","0", "-2a", "0", "-3c", "3b+7", "5d", "7b-4", "3a+5", "5x+5")

    length=len(q_list)
    choice=random.randrange(0,length)
    question=q_list[choice]
    answer=ans_list[choice]
    print (type(question))
    return(question)


def get_answer():
    # this method returns the correct answer for the question raised
    return(answer)

def get_instruction(): 
    # this method returns the instructions for this topic
    
    instructions = []
    instructions.append("If you have 2 euros and you owe someone 5 euros,")
    instructions.append("then its like you are minus 3 euros ") 
    instructions.append("So ")
    instructions.append("1x - 3x = -2x   and ") 
    instructions.append("4b - 5b = -b (note that b = 1b, so we don't have to write the 1 ") 
    instructions.append("And sometimes when we add and subtract all the like terms we get ZERO ")  
    instructions.append("4x - 4x = 0x  or just 0 ") 
    instructions.append("3b + b -4b = 0b  or usually we just write 0" )
    instructions.append("because   0b = 0 ")
    
    return(instructions)


def get_help(question, answer, effort):
    # this method  checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # remove any extra spaces or brackets or number 1... 
    chars_to_remove = "()' '1"
    for character in chars_to_remove:
      effort = effort.replace(character, "")

    helpflag=0
    # if the coefficient is 0 and variable is included, then make the effort = 0 (drop the var)
    if effort[0:1]==str(0) and  len(effort)>1:
        helpflag=1
        help_text="Correct but note its better to just write 0 instead of " +str(effort)
        effort=0
        

    if str(effort)==str(answer):
        if effort==0 and helpflag==1 :
            is_correct = True
            response = {
                'is_correct': is_correct,
                'help_text': help_text
            }
            return (response)
        else:
            is_correct = True
            response = {
                'is_correct': is_correct,
                'help_text': "Correct - Well done"
            }
            return response
        
    else:
        
        help_text="Incorrect:  the correct answer is "+answer + \
        " So, you just need to add or subtract the" \
        " numbers with the same variable in the question "+ question+  \
        "\n And remember x is the same as 1x, so x+x=2x "

        is_correct = False
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response



        return (help_txt)
    





