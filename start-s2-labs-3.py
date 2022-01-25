# Author: CMOB 1/24/2022

def comes_after(st, l):
  res = ''
  l = l.lower()

  for i in range(0, len(st)):

    if i == len(st) - 1:
      break
    elif i != len(st):
      if st[i].lower() == l and st[i + 1].isalpha(): # if the letter in the word is equal to l
        res = res + st[i + 1] # add an additional iteration of the same letter

  return  res