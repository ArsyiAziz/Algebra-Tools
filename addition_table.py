from openpyxl import Workbook
import argparse

def multiplication_table(upper_range):
    workbook = Workbook()
    sheet = workbook.active
    sheet[convert_to_cell(1, 1)] = "+"
    #places the elements of Zˣm
    try:
        for i in range(upper_range):
            sheet[convert_to_cell(2+i, 1)] = i #Collumn
            sheet[convert_to_cell(1, 2+i)] = i  #Row
    except:
        print("Selected m value is too large to process")
        return

    #Calculates the product of each row-collumn pair
    for i in range(upper_range):
        for j in range(upper_range):
            col_num = sheet[convert_to_cell(2+j, 1)].value
            row_num = sheet[convert_to_cell(1, 2+i)].value
            sum_mod = (col_num+row_num)%upper_range
            cell = convert_to_cell(2+i, 2+j)
            sheet[cell] =  sum_mod

    filename = "Z{}.xlsx".format(upper_range)
    workbook.save(filename=filename)
    print("Saved as {}".format(filename))



def convert_to_cell(collumn, row):
    collumn -= 1
    if collumn/26 <1:
        collumn = chr(ord('A')+collumn)
    else:
        collumn = "{}{}".format(
            chr(ord('A')+(collumn//26)-1), chr(ord('A')+collumn%26))
    return "{}{}".format(collumn, row) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program creates the multiplication table of Zm')
    parser.add_argument('m', type=int,
                        help='input m')
    args = parser.parse_args()
    multiplication_table(args.m)
