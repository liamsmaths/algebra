
import random


#
# this function generates a question : adding 2 and 3 like terms with where some answers are negative and zero
#

def get_question():
    global question, answer

    q_list = ("x-2x", "3y-5y", "3a+a", "3p+2p-5p", "2a+a-5a",
              "5x-2x-3x", "c+c-5c", "b+b+b-2b", "2d+2d+3d-2d")
    ans_list = ("-x", "-2y", "4a", "0", "-2a", "0", "-3c", "b", "5d")

    length = len(q_list)
    choice = random.randrange(0, length)
    question = q_list[choice]
    answer = ans_list[choice]

    return(question)


def get_answer():
    # this method returns the correct answer for the question raised
    return(answer)


def get_instruction():
    # this method returns the instructions for this topic

    # instructions = "If you have 2 euros and you owe someone 5 euros,  \n \
    # then its like you are minus 3 euros  \n \n \
    # So \n \
    # 1x - 3x = -2x   and   \n  \
    # 4b - 5b = -b (note that b = 1b, so we don't have to write the 1 \n \n \
    # And sometimes when we add and subtract all the like terms we get ZERO.. \n \
    # 4x - 4x = 0x  or just 0 \n\
    # 3b + b -4b = 0b  or usually we just write 0 \n \
    # as   0b = 0 \n  \n  \
    # Click here for Video : https://youtu.be/rOiBoXoZCbs"

    instruction_list = []

    instruction_list.append(
        "If you add 1 apple plus 3 apples you get 4 apples.")
    instruction_list.append(
        "The same thing goes for adding variables like x and y.")
    instruction_list.append("So")
    instruction_list.append("1x + 3x = 4x   and")
    instruction_list.append(
        "4b - b = 3b (note that b = 1b, we just don't have to write the 1")
    instruction_list.append(
        "However if we add 1 apple and 1 orange we dont get 2 apples or 2 oranges")
    instruction_list.append(
        "Its the same with x and y.  2x+3y = 2x+3y  -> you can only add LIKE terms")
    return instruction_list

   # return(instructions)


def get_help(question, answer, effort):
    # this method  checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # remove any extra spaces or brackets or number 1...
    chars_to_remove = "()' '1"
    for character in chars_to_remove:
        effort = effort.replace(character, "")

    helpflag = 0
    # if the coefficient is 0 and variable is included, then make the effort = 0 (drop the var)
    if effort[0:1] == str(0) and len(effort) > 1:
        helpflag = 1
        help1 = "Correct but note its better to just write 0 instead of " + \
            str(effort)
        effort = 0

    if str(effort) == str(answer):
        if effort == 0 and helpflag == 1:
            return (help1)
        else:
            return ("correct")

    else:

        help_txt = "Incorrect:  the correct answer is "+answer + \
            " So, you just need to add or subtract the" \
            " numbers in the question " + question +  \
            "\n And remember x is the same as 1x, so x+x=2x "
        return (help_txt)
