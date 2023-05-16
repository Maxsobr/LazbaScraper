import pandas as pd

def generateComments(chel):
    stringResult = ""
    stringResult += "Здравствуй, {}!".format(chel.name)
    print(stringResult)

    excel_file = pd.ExcelFile("CommentFilter.xlsx")

    # Get the list of sheet names
    sheet_names = excel_file.sheet_names

    counter = 0
    # Iterate through each sheet
    for sheet_name in sheet_names:
        counter +=1

        if sheet_name != "Заключительная рекомендация":


            # general comment
            dataframe = pd.read_excel(excel_file, sheet_name)

            column_name = dataframe.columns[1]


            print(column_name)
            print("-" * 30)

        #   choosing comment

        #   splitting from to
            cell_value = dataframe.iloc[0, 1]
            split_parts = cell_value.split("-")

            before = int(split_parts[0])
            after = int(split_parts[1])


            print(before)
            print(after)




    return stringResult