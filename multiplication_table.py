from openpyxl import Workbook
import argparse

def multiplication_table(upper_range):
    workbook = Workbook()
    sheet = workbook.active
    sheet[convert_to_cell(1, 1)] = "*"
    elements = 0
    
    #places the elements of Zˣm
    try:
        for i in range(1, upper_range):
            if gcd(i, upper_range) == 1:
                sheet[convert_to_cell(2+elements, 1)] = i #Collumn
                sheet[convert_to_cell(1, 2+elements)] = i #Row
                elements += 1
    except:
        print("Selected m value is too large to process")
        return

    #Calculates the product of each row-collumn pair
    for i in range(elements):
        for j in range(elements):
            col_num = sheet[convert_to_cell(2+j, 1)].value
            row_num = sheet[convert_to_cell(1, 2+i)].value
            product_mod = (col_num*row_num)%upper_range
            cell = convert_to_cell(2+i, 2+j)
            sheet[cell] =  product_mod

    filename = "Zˣ{}.xlsx".format(upper_range)
    workbook.save(filename=filename)
    print("Saved as {}".format(filename))

def gcd(number_1, number_2):
    while number_2 != 0:
        if number_1 < number_2:
            tmp = number_1
            number_1 = number_2
            number_2 = tmp
        tmp = number_2
        number_2 = number_1 % number_2
        number_1 = tmp
    return number_1


def convert_to_cell(collumn, row):
    collumn -= 1
    if collumn/26 <1:
        collumn = chr(ord('A')+collumn)
    else:
        collumn = "{}{}".format(
            chr(ord('A')+(collumn//26)-1), chr(ord('A')+collumn%26))
    return "{}{}".format(collumn, row) 


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program creates the multiplication table of Zˣm')
    parser.add_argument('m', type=int,
                        help='input m')
    args = parser.parse_args()
    multiplication_table(args.m)
