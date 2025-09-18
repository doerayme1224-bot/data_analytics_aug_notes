# project 7
### Display the current date and time

import datetime
def current_date_time():
  """
  Creator: Charles
  Input: None
  Output: The current date and time
  """
  now = datetime.datetime.now()
  print("Current date and time: ")
  print(now.strftime("%Y-%m-%d %H:%M:%S"))

current_date_time()