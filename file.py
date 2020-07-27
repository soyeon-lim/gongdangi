import pandas as pd 
f  = pd.read_csv("wyw.csv", encoding='utf-8', sep='|')


questions = {} 
i = 1; 

for index, l in f.iterrows():
    if l[1] != '':
        t_ans = l[1]
    else: continue
    t_score = 0 if pd.isna(l[2]) else int(l[2])
    t_expl = l[0]
    questions[l[-1]] = {"answer": t_ans, "score": t_score, "explanation":t_expl}

q_list = []
for key in questions.keys(): 
    for i in range(5-questions[key]["score"]):
        q_list.append(key)


print(questions)


