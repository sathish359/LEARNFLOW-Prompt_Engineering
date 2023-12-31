# chatbot

# dictionary to store responses
responses = {
  "hello": "Hello! How can I help you today?",
  "how are you": "I'm just a computer program, so I don't have feelings. But I'm here to help you! What can I do for you?",
  "what is your name": "I'm a chatbot, so I don't have a name. But you can call me Chatbot!",
  "bye": "Goodbye! Have a great day!"
}

# main loop
while True:
  # get user input
  user_input = input("User: ").lower()

  # check if the user's input is in the dictionary of responses
  if user_input in responses:
    # print the corresponding response
    print(f"Chatbot: {responses[user_input]}")
  else:
    # if the user's input is not recognized, ask them to try again
    print("Chatbot: I'm sorry, I didn't understand that. Could you please try again?")
