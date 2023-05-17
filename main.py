# -*- coding: utf-8 -*-

import pandas as pd
import GenerateComments as gn
import ChartGeneration as chartGeneration
import ending as end
from docx import Document

# Read the CSV file into a DataFrame
df = pd.read_csv('Test.csv')

nameColumn = "Укажи здесь свои данные, чтобы мы могли отправить тебе результаты. [Имя и фамилия]"

RowIndex = 0
# Access a cell value by column name and index
# nameSurname = df.loc[RowIndex, nameColumn]

# Print the cell value
# print(nameSurname)

emailColumn = "Укажи здесь свои данные, чтобы мы могли отправить тебе результаты. [Email адрес]"

# email = df.loc[RowIndex, emailColumn]



# Print the cell value
# print(email)

firstQuestion = "Если кто-то захочет вас прогнать, вы почувствуете необходимость что-то предпринять в связи с этим?"
# lastQuestion = "Вы любили в детстве играть с оружием"


# firstAnswer = df.loc[RowIndex, firstQuestion]


# Print the cell value
# print(firstAnswer)

startColumnIndex = df.columns.get_loc(firstQuestion)

# endColumnIndex = df.columns.get_loc(lastQuestion)
#
# i = startColumnIndex
# while i<= endColumnIndex :
#     cell_value = df.iloc[RowIndex, i]
#     print(df.columns[i] + cell_value + "\n")
#     i += 1


# Specify the file path
file_path = 'Calculation rule.xlsx'

# # Loop through each sheet and perform operations
# for sheet_name, sheet_data in all_sheets.items():
#     # Process the data from each sheet
#     print(f"Sheet Name: {sheet_name}")
#     print(sheet_data.head())  # Example: printing the first few rows
#     print('-' * 30)




my_dict = {}
tempEvaluation = 0



def evaluateScore(sheetIndex, file_path, resultSheet,startColumnIndex, ChelRowIndex):

    startColumnIndex -=1



    xl = pd.ExcelFile(file_path)

    sheet_names = xl.sheet_names
    sheet_name = sheet_names[sheetIndex]
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    # print(f"Sheet Name: {sheet_name}")
    # print(df.head())

    totalPoints = 0
    for index, row in df.iterrows():

        if resultSheet.iloc[ChelRowIndex, startColumnIndex + int (row['Вопрос'])] == "Да" and row['Правильный ответ'] == "+":
            totalPoints+=1
        elif resultSheet.iloc[ChelRowIndex, startColumnIndex + int (row['Вопрос'])] == "Нет" and row['Правильный ответ'] == "-":
            totalPoints+=1
        elif resultSheet.iloc[ChelRowIndex, startColumnIndex + int(row['Вопрос'])] == "Не уверен" :
            totalPoints += 0

    my_dict = {}

    # Add elements dynamically
    my_dict[sheet_name] = totalPoints
    return my_dict


        # Access row data using column names or indices
        # print(f"Row {index + 1}: {row['Вопрос']}, {row['Правильный ответ']})  # Example

    # if resultSheet.
    #
    #     cell_value = df.iloc[RowIndex, i]
    #     print(df.columns[i] + cell_value + "\n")

class Chel:
    def __init__(self, name, email, dictResults):
        self.name = name
        self.email = email
        self.dictResults = dictResults

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, Results: {self.dictResults}"

    def clean(self):
        newDict = {}
        for key, value in self.dictResults.items():

            if key == "Маскулинность - феминность":
                newDict["Маскулинность / феминность"] = value
            elif key != "Догматизм":
                newDict[key] = value


        self.dictResults = newDict
        # newDict = {}
        # for key, value in self.dictResults[0].items():
        #     if "Догматизм" in self.dictResults:
        #         self.dictResults[0].pop("Догматизм")
        #     if "Маскулинность - феминность" in self.dictResults:
        #         self.dictResults[0]["Маскулинность / феминность"] = self.dictResults[0].pop("Маскулинность - феминность")
        # #
        #     if key != "Догматизм":
        #         newDict[key] = value
        #     elif key == "Маскулинность - феминность":
        #         newDict.pop("Маскулинность - феминность")
        #         newDict["Маскулинность / феминность"] = value
        #
        # self.dictResults = newDict
        #
        # print(newDict)

        # if "Догматизм" in self.dictResults:
        #     del self.dictResults.pop()["Догматизм"]
        # if "Маскулинность - феминность" in self.dictResults:
        #     self.dictResults["Маскулинность / феминность"] = self.dictResults.pop("Маскулинность - феминность")

ChelList = []

for index, row in df.iterrows():
    resultDict = {}
    for sheetIndex in range(7):
        resultDict.update(evaluateScore(sheetIndex, file_path, df, startColumnIndex, index))

    nameSurname = df.loc[index, nameColumn]
    # print(nameSurname, "\n")
    # print(resultDict)
    # print("-" * 30)
    email = df.loc[RowIndex, emailColumn]

    ChelList.append(Chel(nameSurname, email, resultDict))

for i in ChelList:
    i.clean()
    print(i)



chartGeneration.testChart(ChelList[0])
#
# for i in ChelList:
#     resultString = gn.generateComments(i)
#     end.endString(resultString, i)
#

# Adding a paragraph
#
for i in ChelList:
    resultString = gn.generateComments(i)

    resultString += end.endString(i)

    document = Document()

    # if
    document.add_paragraph(resultString)

    output_filename = '{}.docx'.format(
        i.name)  # Example with string formatting

    document.save(output_filename)














