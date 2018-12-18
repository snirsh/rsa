import pandas as pd
import glob


def main():
    merged_file = pd.DataFrame()
    for input_file in glob.glob('input*.xlsx'):
        df = pd.read_excel(input_file)
        merged_file = merged_file.append(df, ignore_index=True)
    writer = pd.ExcelWriter('merged_input.xlsx')
    merged_file.to_excel(writer, sheet_name='sheet1')
    writer.save()
    data = pd.read_excel('merged_input.xlsx')
    print("total rows: {0}".format(len(data)))
    print(list(data)[0])


if __name__ == '__main__':
    main()
