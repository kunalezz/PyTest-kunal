import openpyxl

def get_test_data():
    wb = openpyxl.load_workbook('sampleSheet.xlsx')
    ws = wb["Sheet1"]

    data = []

    for i in ws.iter_rows(min_row=2, values_only=True):
        data.append(i)

    return data