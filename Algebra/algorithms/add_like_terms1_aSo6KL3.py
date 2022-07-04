
import random

from rest_framework import response

#
# this function generates a question : adding 2 and 3 like terms with some subtraction
#  but answer always positive
#


def get_question():
    global question, answer

    q_list = ("x+2x", "3y+4y", "3a+a", "3p+2p", "2x+4x-3x",
              "5x-2x+x", "4a+2a-3a", "2q+3q", "4c-c+2c", "3c+3c-c",
              "q+q+2q", "p+10p-3p","a-a","6c-c","2a+3a",
              "2d+3d+4d", "2e-e", "4c-c-c", "x+2x+3x", "y+2y-y")
    ans_list = ("3x", "7y", "4a", "5p", "3x", 
                "4x", "3a", "5q", "5c","5c",
                "4q","8p","0", "5c","5a",
                "9d", "e", "2c", "6x", "2y")

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


def get_help(question, answer, effort):
    # this method returns checks the answer against the student effort and returns
    # either correct or help with what they did wrong

    # if the student just types in the question - this would be ok for sympy
    if effort == question:
        is_correct = False
        help_text="You can't just type in the question!  The answer is: "+str(answer)
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response


    # remove any extra spaces or brackets...
    is_correct = None
    help_text = ""
    chars_to_remove = "()' '"
    for character in chars_to_remove:
        effort = effort.replace(character, "")

    if effort == answer:
        is_correct = True
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response

    else:
        is_correct = False
        help_text = "Incorrect:  the correct answer is "+answer + \
            " So, you just need to add or subtract the" \
            "numbers in the question " + question +  \
            "\n And remember x is the same as 1x, so x+x=2x "
        response = {
            'is_correct': is_correct,
            'help_text': help_text
        }
        return response
