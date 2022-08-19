# 10.3
# Дан словарь:
# days = { 1:'Sun', 2:'Mon', 3:'Tue', 4:'Wed', 5:'Thu', 6:'Fri', 7:’Sat’}
# Записать его в файл построчно.

days = {1: 'Sun', 2: 'Mon', 3: 'Tue', 4: 'Wed', 5: 'Thu', 6: 'Fri', 7: 'Sat'}
with open("ДЗ_11.txt", "w") as f:
    for k, v in days.items():
        f.write("{}:{}\n".format(k,v))
print()
print("Wow")
