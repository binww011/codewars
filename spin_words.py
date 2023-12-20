def spin_words(sentence):
  words = sentence.split(' ')
  for i in range(0, len(words)):
    if len(words[i]) >= 5:
      words[i] = str(words[i][::-1])
  return " ".join(words)
