#!/usr/bin/env python3

class MyString:

  def __init__(self, value = ""):
    self._value = value

  def get_value(self):
    return self._value

  def set_value(self,value):
    if type(value) == str:
      return self._value == value  
    else:
      print('The value must be a string.')
            
  value = property(get_value, set_value)

  def is_sentence(self):
      if self._value.endswith("."):
        return True
      return False
  
  def is_question(self):
      if self._value.endswith("?"):
          return True
      return False
  
  def is_exclamation(self):
      if self._value.endswith("!"):
          return True
      return False
  
  def count_sentences(self):
    checker = ["?","!"]
    value = self._value
    for fullstop in checker:
      value = value.replace(fullstop, ".")

    print(value)

    number = 0
    list_of_sentence = [broken_sentence.strip() for broken_sentence in value.split(".")]
    for word_count in list_of_sentence:
      if word_count != "":
        number += 1
    return number

