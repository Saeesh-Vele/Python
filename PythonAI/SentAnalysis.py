pos_words=['good' , 'happy' , 'great' , 'love']
neg_words=['bad' , 'sad' , 'terrible' , 'hate']
def sent_analysis(text):
    score=0
    words=text.lower().split()

    for word in words:
        if word in pos_words:
            score+=1
        elif word in pos_words:
            score-=1

    if score>0:
        return "Positive"
    elif score<0:
        return "Negative"
    else:
        return "Neutral"
print(f"Review: ",sent_analysis("I really love this not great product"))
            
