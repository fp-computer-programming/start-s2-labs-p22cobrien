# Author: CMOB 1/24/2022

rows = [["Mateo", "Jason", "Jordan", "Mohamed", "Michael", "Charlie", "Declan"], ["Sean", "Luis", "Ryan", "James", "Jack"], ["Aiden", "Ian", "Colin","Tim", "Cam"], ["Larry", "Spencer", "Chris", "Ryan", "Nolan"]]
last_initials = ["B.","D.","H.","E.","G.","G.","H.","R.","M.","L.","I.","I.","N.","N.","O.","P.","P.","X.","T.","S.","S.","P."]

for row in rows: # for each of nested list in rows
    for index, value in enumerate(row): # for each value in row
        row[index] = "{0} {1}".format(value,last_initials[0]) # take the value and add the first value from last_initials to the value
        del last_initials[0] # delete the just used value from last_initials


print(rows) # print new rows w/ updated names

