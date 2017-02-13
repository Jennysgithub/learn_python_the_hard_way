from sys import argv
script, output_filename = argv

def ask_a_question(msg):
   return raw_input(msg)
    
   
def write_questions_and_answers_to_file(
    q1, q2, q3, q1_user_answer, q2_user_answer, q3_user_answer, output_filename
    ):
    fh = open(output_filename, "w")    
  
    line1 = "Question: {}\n".format(q1)
    line2 = "Answer: {}\n\n".format(q1_user_answer)
    line3 = "Question: {}\n".format(q2)
    line4 = "Answer: {}\n\n".format(q2_user_answer)
    line5 = "Question: {}\n".format(q3)
    line6 = "Answer: {}\n\n".format(q3_user_answer)
    
    fh.write(line1)
    fh.write(line2)
    fh.write(line3)
    fh.write(line4)
    fh.write(line5)
    fh.write(line6)
    
    fh.close()
    

    
q1 = ask_a_question("Please ask me a question, really, anything!: ")
q2 = ask_a_question("Ask me another question, pleeeease: ")
q3 = ask_a_question("Ok, ask me one last question, thanks!: ")

print "Now it's time to answer your own questions ..."

q1_user_answer = ask_a_question(q1)
q2_user_answer = ask_a_question(q2)
q3_user_answer = ask_a_question(q3)

write_questions_and_answers_to_file(q1, q2, q3, q1_user_answer, q2_user_answer, q3_user_answer, output_filename)
