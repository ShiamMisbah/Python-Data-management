import openpyxl

workbook = openpyxl.load_workbook("Different_file_format_images.xlsx")

worksheet = workbook.active

worksheet_cell = worksheet.cell(1,3)
print(worksheet_cell.value)

workbook.save("Different_file_format_images.xlsx")