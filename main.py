

import pandas as pd


# Read the CSV file into a DataFrame
df = pd.read_csv('Test.csv')

nameColumn = "Укажи здесь свои данные, чтобы мы могли отправить тебе результаты. [Имя и фамилия]"

RowIndex = 0
# Access a cell value by column name and index
nameSurname = df.loc[RowIndex, nameColumn]

# Print the cell value
print(nameSurname)

emailColumn = "Укажи здесь свои данные, чтобы мы могли отправить тебе результаты. [Email адрес]"

email = df.loc[RowIndex, emailColumn]



# Print the cell value
print(email)

firstQuestion = "Если кто-то захочет вас прогнать, вы почувствуете необходимость что-то предпринять в связи с этим?"
lastQuestion = "Вы любили в детстве играть с оружием? "


firstAnswer = df.loc[RowIndex, firstQuestion]


# Print the cell value
print(firstAnswer)

startColumnIndex = df.columns.get_loc(firstQuestion)

endColumnIndex = df.columns.get_loc(lastQuestion)

i = startColumnIndex
while i<= endColumnIndex :
    cell_value = df.iloc[RowIndex, i]
    print(df.columns[i] + cell_value + "\n")
    i += 1








