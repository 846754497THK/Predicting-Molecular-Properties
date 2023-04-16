import os
import pandas as pd

data = pd.read_csv('structures.csv')
for rowNum, rowData in data.iterrows():
    if rowNum < 100:
        fileName = rowData['molecule_name']
        if not os.path.exists(f'structures/{fileName}.xyz'):
            with open(f'structures/{fileName}.xyz', 'w') as file:
                file.write('1\n\n')
        else:
            with open(f'structures/{fileName}.xyz', 'r+') as file:
                atomNum = int(file.readline())
                file.seek(0)
                file.writelines([f'{atomNum + 1}'])
        with open(f'structures/{fileName}.xyz', 'a') as file:
            file.writelines([f"{rowData['atom']} {rowData['x']} {rowData['y']} {rowData['z']}\n"])
    else:
        break




import os
import pandas as pd

data = pd.read_csv('structures.csv')
for rowNum, rowData in data.iterrows():
  fileName = rowData['molecule_name']
  if not os.path.exists(f'structures/{fileName}.xyz'):
    with open(f'structures/{fileName}.xyz', 'w') as file:
      file.write('1\n\n')
  else:
    with open(f'structures/{fileName}.xyz', 'r+') as file:
      atomNum = int(file.readline())
      file.seek(0)
      file.writelines([f'{atomNum + 1}'])
    with open(f'structures/{fileName}.xyz', 'a') as file:
      file.writelines([f"{rowData['atom']} {rowData['x']} {rowData['y']} {rowData['z']}\n"])