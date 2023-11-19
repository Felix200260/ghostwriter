message = []

content = pdf_code()
# print(content)



message.append({"role": "context", "content": content}) 

while True:
    question = input() 
    message.append({"role": "user", "content": question})

    answer = ask_gpt(message=message)
    message.append({"role": "assistant", "content": answer})