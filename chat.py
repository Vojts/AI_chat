import openai
from dotenv import dotenv_values

config = dotenv_values('key.env')

openai.api_key = config['API_KEY']

def generate_response(prompt, model_select):
  response = openai.responses.create(
    model = model_select,
    max_output_tokens = 400,
    temperature = 0.4,
    input = prompt,
  )
  retrieve_text = response.output[0].content[0].text
  return retrieve_text


def models(selected_model):
  print("===================================")
  print("You have selected " + selected_model)
  print("===================================")
  question = input("What do you want to ask? ")
  print("===================================")
  print("GPT answered:" + generate_response(question, selected_model))
  print("^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^ ^")

  

main_menu = True

while main_menu:
  print("================================")
  print("Select GPT model you want to use")
  print("================================")
  print("1. gpt 4.1-mini")
  print("2. gpt 4.1")
  print("3. gpt o4-mini")
  print("4. Exit the program")
  print("================================")
  model_choice = input("enter your choice: ")
  if model_choice == "1":
    models("gpt-4.1-mini")
  elif model_choice == "2":
    models("gpt-4.1")
  elif model_choice == "3":
    models("o4-mini")
  elif model_choice == "4":
    print("Exiting the program...")
    break
  else:
    print("Invalid choice. Please try again.")
    continue