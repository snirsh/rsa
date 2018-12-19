import pandas as pd
import glob
import xlrd


def main():
    merged_file = pd.DataFrame()
    for input_file in glob.glob('input*.xlsx'):
        df = pd.read_excel(input_file)
        merged_file = merged_file.append(df, ignore_index=True)
    writer = pd.ExcelWriter('merged_input.xlsx')
    merged_file.to_excel(writer, sheet_name='sheet1')
    writer.save()
    # data = pd.read_excel('merged_input.xlsx')
    # date is saved in list(data)[1]
    # tz is saved in list(data)[3]
    # status is saved in list(data)[11]
    # type is saved in list(data)[13]
    # location is saved in list(data)[54]
    # id_numbers = data[(list(data)[3])]


if __name__ == '__main__':
    main()
