import pandas as pd


kursifilm = pd.read_csv('datakursi2.csv')
dfkf = pd.DataFrame(kursifilm)

locfilm = (dfkf["studio"])
daftarkursi = locfilm.tolist()

print(list(dict.fromkeys(daftarkursi)))

new_menu = [1,1,1,1,1,1]

final_new_menu = list(dict.fromkeys(new_menu))

print(final_new_menu)