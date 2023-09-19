import pandas as pd

def generateComments(chel):
    stringResult = ""
    stringResult += "Здравствуй, {}!\n\n".format(chel.name)
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

            # generalRecommendation
            # ИМЯ ПЕРВОЙ колонки
            column_name = dataframe.columns[1]


            print(column_name)
            print("-" * 30)

            stringResult += column_name

        #   choosing comment

            substring = sheet_name.split()[0]
            print(substring)
            matching_key = next((key for key in chel.dictResults.keys() if substring in key), None)

            print(matching_key, ";", chel.dictResults[matching_key])

            # Iterate through columns

            # get the first row
            first_row = dataframe.iloc[0]
            second_row = dataframe.iloc[1]
            print(second_row)

            print(first_row)

            # print("Lennnn", len(first_row))

            # go through all cells in the first row
            for i in range(1, len(first_row)):
                #   splitting from to

                cell_value = first_row[i]

                split_parts = cell_value.split("-")

                before = int(split_parts[0])
                after = int(split_parts[1])

                print("currrentKey", chel.dictResults[matching_key])
                print(before, ";", after)

                if chel.dictResults[matching_key] >= before and chel.dictResults[matching_key] <= after:
                    # generate comment
                    stringResult += second_row[i]

                    replacement = chel.dictResults[matching_key]
                    stringResult = stringResult.replace("«ЦИФРА»",
                                                        str(replacement)).replace(
                        "«ОЦЕНКА»", str(replacement))

                    break


            # «Цифра» замена на chel.dictResults[matching_key]
                # print(first_row[i])



            # print(resultReplaced)
            # matching_keys = [key for key in my_dict.keys() if substring in key]


            # if chel.

            print(before)
            print(after)









    return stringResult