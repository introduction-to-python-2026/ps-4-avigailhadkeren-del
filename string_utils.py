def split_before_each_uppercases(formula):
  start = 0
  end = 0
  split_formula = []
  for char in formula [1:]:
    end += 1
    if char.isupper():
      substring = formula[start:end]
      split_formula.append(substring)
      start =end
    
  substring = formula[start:]
  if substring is not None and substring != "":
    split_formula.append(substring)
  
  return (split_formula)  


def split_at_first_digit(formula):
  digit_location = 1
  for char in formula[1:]:
    if char.isdigit() == True:
      break
    digit_location += 1

  if digit_location == len(formula):
    prefix = formula 
    numeric = 1
  else:
    prefix = formula[:digit_location]
    numeric = int(formula[digit_location:])

  return (prefix, numeric)
