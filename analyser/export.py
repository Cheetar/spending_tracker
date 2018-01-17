import os

from django.conf import settings

import xlwt


def export_spendings_to_excel(board):
    """ Makes an excel file based on spendings in given board. Returns path to that file.
    """

    style_normal = xlwt.easyxf('font: name Times New Roman')
    style_income = xlwt.easyxf('font: name Times New Roman,color-index green')
    styles = [style_normal, style_income]

    wb = xlwt.Workbook()
    ws = wb.add_sheet(board.name)

    ws.write(0, 0, 'Spending')
    ws.write(0, 1, 'Cost')
    ws.write(0, 2, 'Category')
    ws.write(0, 3, 'Date')

    spendings = board.spendings
    for i in range(len(spendings)):
        spending = spendings[i]
        ws.write(i + 1, 0, str(spending.name), styles[int(spending.is_income)])
        ws.write(i + 1, 1, str(spending.cost) + board.currency, styles[int(spending.is_income)])
        ws.write(i + 1, 2, str(spending.category), styles[int(spending.is_income)])
        ws.write(i + 1, 3, str(spending.date), styles[int(spending.is_income)])

    directory = settings.BASE_DIR + '/media/exports/'
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = board.name + '.xls'
    path = directory + filename
    wb.save(path)
    return path
