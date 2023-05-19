import pandas as pd
def endString( chel):
    workingString = ""
    LowPointDict = {"Маскулинность/Феминность":[0,12],
                        "Манипулятивность": [1,13],
                    "Установка на успех": [1,14],
                        "Напористость": [0,13],
                        "Агрессивность": [0,13]}

    lowPointsCounter = 0

    highStimul = False
    if chel.dictResults["Поиск стимуляции"] >= 26:
        highStimul = True


    for key in chel.dictResults:
        if key in LowPointDict:
            value = chel.dictResults[key]
            range_values = LowPointDict[key]
            if range_values[0] <= value <= range_values[1]:
                lowPointsCounter += 1

    print(f"Number of values within the specified ranges: {lowPointsCounter}")


    print(chel.dictResults, "/n")
    print(lowPointsCounter, "/n")
    print(highStimul, "/n")

    excel_file = pd.ExcelFile("CommentFilter.xlsx")

    sheet_names = excel_file.sheet_names

    counter = 0
    recomendationList = []
    # Iterate through each sheet
    for sheet_name in sheet_names:


        if sheet_name == "Заключительная рекомендация":
            # general comment
            dataframe = pd.read_excel(excel_file, sheet_name)

            # generalRecommendation
            column_name = dataframe.columns[1]
            recomendationList = dataframe.iloc[0].values.tolist()

    print(chel.dictResults)
    print(chel.name," low: ", lowPointsCounter, "high stimul? ", highStimul)

    # high
    if lowPointsCounter == 1 or highStimul:
        workingString += recomendationList[3]
        print("high")

    # low
    elif (lowPointsCounter == 2 and highStimul) or lowPointsCounter >= 3 :
        workingString += recomendationList[1]
        print("Low")

    # norm
    elif lowPointsCounter <= 2 or (lowPointsCounter == 1 and highStimul):
        workingString += recomendationList[2]
        print("mid")
    else:
        print("something wrong")


    return workingString
