import random

EnglishMonths_to_FrenchMonths = {
    "January": "Janvier",
    "February": " Février",
    "March": " Mars",
    "April": " Avril",
    "May": " Mai",
    "June": " Juin",
    "July": " Juillet",
    "August": " Août",
    "September": " Septembre",
    "November": " Novembre",
    "December": " Décembre",
}

list = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'November', 'December']
random.shuffle(list)
print(list)
list.pop(0)
#%%
random.shuffle(EnglishMonths_to_FrenchMonths)
print(EnglishMonths_to_FrenchMonths)
#%%
