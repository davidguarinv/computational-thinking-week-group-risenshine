def solution_station_5():
    LT_groups = {
    "LT1": ["Daeho", "David G", "Kaisa", "Oliver", "Sara", "Dan", "Ivar", "Lotte", 
            "Riya", "Vassil", "Twan", "Ester", "Karolina", "Lena", "Margarita", 
            "Anna P", "Kien", "Klaudia", "Maliah", "Todd"],
    "LT2": ["Oumaima", "Mathilde", "Marie", "Anita", "Ziyan", "Bernardo", 
            "Eleanor", "Lorijn", "Maria P", "Younes", "Yvan", "Henning", "Liangyu", 
            "Maciej", "Toprak", "Chris", "GengXin", "Mingze", "Phoebe"],
    "LT3": ["Betija", "Haider", "Kacper", "Sophie P", "Amir", "Baltasar", "Isar", 
            "Jelle", "Nicolas", "David C", "Ipek", "Juan", "Marfa", "Maria L", 
            "Alissa", "Leopoldo", "Mies", "Jiaying", "Kaixin", "Mai", "Sem", "Tibbe"],
    "LT4": ["Justus", "Julia", "Philip", "Uli", "Vanessa", "Anna A", "Ekaterina", 
            "Thessa", "Tongfei", "Yang", "Benedikt", "Jan", "Nadee", "Osjah", "Tim", 
            "Eliana", "Joana", "Peilin", "Pija", "Wenhao"],
    "LT5": ["Afua", "Cristina", "Greta", "Jace", "Laura", "Anna V", "Bassant", "Ivan", 
            "Juriaan", "Kiavash"],
    "LT6": ["Keitaro", "Nohemi", "Norina", "Yifan", "Yinan", "Luo", "Nikola", 
            "Olesya", "Sophie M", "Tom"]
}

def get_LT(name):
    for group, names in LT_groups.items():
        if name in names:
            return group
    return "Not found"
