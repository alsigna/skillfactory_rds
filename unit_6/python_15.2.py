def safe_exec(ext_func):
  try:
    return ext_func()
  except:
    print("division by zero")
    return 0

def zero_div():
    return 5/0
print(safe_exec(zero_div))

def normal_div():
    return 5/1
print(safe_exec(normal_div))