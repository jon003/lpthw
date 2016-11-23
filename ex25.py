def break_words(stuff):
  """ This function will break up words for us."""
  words = stuff.split(' ')
  return words

def sort_words(words):
  """ Sorts the words."""
  return sorted(words)
  
def print_first_word(words):
  """ prints the first word """
  word = words.pop(0)
  print word
  
def print_last_word(words):
  """ prints the last word """
  word = words.pop(-1)
  print word
  
def sort_sentence(sentence):
  """Takes in a full sentence and returns the sorted words."""
  words = break_words(sentence)
  return sort_words(words)
  
def print_first_and_last(sentence):
  """ Prints the first and last words of the sentence."""
  words = break_words(sentence)
  print_first_word(words)
  print_last_word(words)

def print_first_and_last_sorted(sentence):
  """ Prints the first and last words of the sorted sentence."""
  words = sort_sentence(sentence)
  print_first_word(words)
  print_last_word(words)
  
# study drills
# 1. done
# 2. done
# 3. from ex25 import *.  nice
# 4. i broke it a bit getting it ready.
