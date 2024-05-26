with open("madlibs/story.txt","r") as f:

    story=f.read()

words=set()
start_of_word = -1

for i,ch in enumerate(story):
    if ch=="<":
        start_of_word=i
    if ch==">" and i!=-1:
        word=story[start_of_word:i+1]
        words.add(word)
        start_of_word = -1

user_inputs={}

for word in words:
    user_input = input("Enter a word for" + word + ":")
    user_inputs[word] = user_input

for word in words:
    story = story.replace(word,user_inputs[word])
    
print(story)
