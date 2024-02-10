Father = {
    "Mahmoud" : "Mah.43@gm",
    "Male" : 1978
}

Mother = {
    "Nada" : "N234@gm",
    "Female" : 1982
}

child1 = {
    "Yassin" : "Yassin.564@gm",
    "Male" : 2004
    
}
child2 = {
    "Rania" : "Rania.676@gm",
    "Female" : 2007
}
child3 = {
    "Nadia" : "Nadia.5r4@gm",
    "Female" : 2009
}

myfamily = {
    "Father" : Father,
    "Mother" : Mother,
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}

print(myfamily)
print(myfamily.keys())
print(myfamily.get("child1"))