def split_before_each_uppercases(formula):
    pass # Replace the `pass` with your code


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
