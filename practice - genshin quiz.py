from quiz_ques import questions

q_prompts = [
    "What is Venti's true identity? \n(a) Drunk Man  (b) Wind Spirit  (c) Klee's Mum\n\nAnswer: ",
    "Where do Zhongli works as a human now? \n(a) Wangsheng Funeral Parlor  (b) Cat Tail's Bar  (c) Port Ormos\n\nAnswer: ",
    "Can Raiden Shogun cook? \n(a) Yes  (b) Who knows  (c) No\n\nAnswer: ",
    "Nahida's archon name based on a demon is ____. \n(a) Baal  (b) Kusanali  (c) Buer\n\nAnswer: ",
    "Who tried to kill Furina? \n(a) Neuvilette  (b) Arlecchino  (c) Traveler\n\nAnswer: ",
]

ans_key = [
    questions(q_prompts[0], "b"),
    questions(q_prompts[1], "a"),
    questions(q_prompts[2], "c"),
    questions(q_prompts[3], "c"),
    questions(q_prompts[4], "b"),
]

def quiz (ans_key):
    score = 0
    for questions in ans_key:
        answer = input(questions.ques)
        if answer.lower() == questions.ans:
            score += 1
    print("Congratulations, you got " + str(score) + "/" + str(len(q_prompts)) + " score.")

quiz(ans_key)