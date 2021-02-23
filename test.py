from cs50 import SQL
import re
import random

db = SQL("sqlite:///magic.db")

question = "Do I really exist?"

linguistics = {'Can this work?', 'Could this work?', 'Am- I working?', 'Are....#...', 'Is', 'Does', 'Do', 
'Did', 'Will', 'Would', 'Were', 'Was', 'Should', 'Shall', 'May', 
'Might', 'Must', 'Have', 'Has'}
#polar = question.split()
#if polar[0] in linguistics:
number = random.randint(1,21)
answer = db.execute("""SELECT answer 
FROM responces WHERE ID = :ID""", ID = number)
            
print(linguistics["number"])







