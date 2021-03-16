print("Enter the word: ")
Search = input()
dictionary = {"Literally": "in a Literal manner or Sense, Exactly.",
              "Irony": "sarcasm, Dryness.",
              "Patriarchy": "a male dominated society.",
              "Immolate": "to kill or offer as a sacrifice, especially by burning!"}
print("It means,")
print(dictionary.get(Search))
