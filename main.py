# For when school, or admin blocks websites such as ChatGPT.
# by @alphaotuken 
import openai
import subprocess
from colorama import Fore, Style
import pwinput
import json
import os


def askquestion(question, engine):
  completion = openai.Completion.create(
    engine=engine,
    prompt=question,
    max_tokens=2048,
    n=1,
    stop=None,
    temperature=0.5,
  )

  response = completion.choices[0].text
  return response


if __name__ == "__main__":
  print(Fore.GREEN + 'Made by @alphaotuken on Replit \n' + Style.RESET_ALL)

  print(
    'I know, this is a turnoff but sadly, you cannot use J4E without an API key.'
  )

  print(
    '\nWhy do I need this? We cannot use a private API key due to rate limits and privacy. You can find your api key at: '
    + Fore.BLUE + 'https://beta.openai.com/account/api-keys' + Style.RESET_ALL)

  print(
    '\nBut, there is a solution! If you go to this replit: ' + Fore.BLUE +
    'https://replit.com/@alphaotuken/ChatGDP-Unblocked?v=1' +
    Style.RESET_ALL +
    ' and enter the link above, you can login to your account and find or create your API Key. For any issues you can check'
  )
  key = pwinput.pwinput(prompt='\nEnter API Key: ', mask='*')
  openai.api_key = key

  print("""
  GPT-3 Models:
  \ttext-davinci-003 (default, reccommended.)
  \ttext-curie-001
  \ttext-babbage-001  
  \ttext-ada-001   
  """)
  model_engine = input('Select engine: ')
  if not model_engine:
    model_engine = 'text-davinci-003'

  print(
    Fore.GREEN +
    "Chat commands: \n\tExit - Straight forward. \n\tNano - To open the nano interface for longer messages"
    + Style.RESET_ALL)
  print("Hi, I'm a J4E based AI. How can I help you today?")

  while True:
    question = input("You: ")

    if question.lower() == "exit":
      print("Bye! Have a great day.")
      break
    elif question.lower() == "nano":
      subprocess.call(['sh', './nano.sh'])

      print(
        Fore.GREEN +
        "\nTo use the text you just inputted, put [nano] somewhere in the text you're about to input. e.g 'Rewrite this email: [nano]' "
      )

      question = input("You: ")
      with open("./lines.txt", "r") as c:
        contents = c.read()
      question = question.replace('[nano]', contents)

    response = askquestion(question, model_engine)
    print("J4E: " + response)
