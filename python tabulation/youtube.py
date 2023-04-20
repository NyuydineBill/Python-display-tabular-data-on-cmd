from tabulate import tabulate

students=[
    {"Name":"Nyuydine Bill","Department":"COME","Class":"A","Ranking":"A"},
    {"Name":"Edwin Bush","Department":"CHME","Class":"A","Ranking":"D"},
    {"Name":"Glory Henry","Department":"MATE","Class":"B","Ranking":"A"},
    {"Name":"Ayra Gold","Department":"PHYE","Class":"C","Ranking":"C"},
    {"Name":"Mark Jeffrey","Department":"COME","Class":"B","Ranking":"A"},
    {"Name":"Stone White","Department":"COME","Class":"A","Ranking":"C"},
]

print(tabulate(students,headers="keys",tablefmt="fancy_grid"))