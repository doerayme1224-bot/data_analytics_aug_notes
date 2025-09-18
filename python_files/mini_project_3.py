# project 3
### Return the count of a given substring from a string


def substring_count(string, substring) -> int:
  """
  Creator: Charles
  Input: A string and a substring
  Output: The number of times that the substring appeares in the string
  """
  return string.count(substring)
sentence= 'hi there, hi how are you, hi i\'m doing well, hi and bye'
substring_count(sentence, 'hi')



