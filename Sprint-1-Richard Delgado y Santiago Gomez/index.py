import pandas as pd

db = pd.read_csv('Base-de-datos-STI.csv')

def ordenar (dataframe, column, organization):

    if organization == 'ascendente':
        activeOrg = True
    elif organization == 'descendente':
        activeOrg = False
    else:
        return ValueError('Debes especificar si quieres ordenarlo de forma ascendente o descendente')
    
    dbOrdenada = dataframe.sort_values(by = column, ascending = activeOrg).reset_index(drop = True)
    
    return dbOrdenada

column_selection = input('escribe el nombre de la columna que quieres ordenar: ')
organize_selecction = input('escribe si quieres ordenar de forma "ascendente" o "descendente": ')

newDB = ordenar(db, column_selection, organize_selecction)

print(newDB)