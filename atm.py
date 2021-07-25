# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
amount = 225
papers = [1, 5, 10, 50, 100, 200]
money_dict = {}

for paper in reversed(papers):
    result = divmod(amount, paper)
    needed_papers = result[0]
    amount = result[1]
    money_dict.update({paper: needed_papers})

print(money_dict)    
