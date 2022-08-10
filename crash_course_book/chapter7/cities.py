prompt = "\n Please enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you're finished."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I would love to visit {city}")
