import g4f

import os

from pdf_code.pdf_code import pdf_code # функция отвечает за вывод содержимого файла в консоль \ содержимое файла содерижиться в переменной content


def ask_gpt(message: list, language: str = "ru") -> str:
    response = g4f.ChatCompletion.create(
        model=g4f.models.gpt_4, 
        messages=message,
        language=language

    )
    print(response)
    return response

message = []

content = pdf_code()
# print(content)



# message.append({"role": "context", "content": content}) 

while True:
    question = input() 
    message.append({"role": "user", "content": question})

    answer = ask_gpt(message=message)
    message.append({"role": "assistant", "content": answer})
