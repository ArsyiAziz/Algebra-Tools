from openpyxl import Workbook
import argparse


def coset_addtion_table(m, num_elements):
    counter = 0
    cosets = addition_coset_finder(m, num_elements)
    
    for coset in cosets:
        workbook = Workbook()
        sheet = workbook.active
        sheet[convert_to_cell(1, 1)] = "+"


        # try:
        for i in range(len(coset)):
            sheet[convert_to_cell(2+i, 1)] = coset[i] #Collumn
            sheet[convert_to_cell(1, 2+i)] = coset[i]  #Row
        for i in range(len(coset)):
            for j in range(len(coset)):
                col_num = int(sheet[convert_to_cell(2+j, 1)].value)
                row_num = int(sheet[convert_to_cell(1, 2+i)].value)
                sum = col_num+row_num
                cell = convert_to_cell(2+i, 2+j)
                sheet[cell] =  sum

        filename = "{} + {}Z.xlsx".format(counter, m)
        workbook.save(filename=filename)
        print("Saved as {}".format(filename))
        counter += 1
        # except:
        #     print("Selected m value is too large to process")
        
       


def addition_coset_finder(m, num_elements):
    cosets = []
    for i in range(m):
        elements = []
        for j in range(-num_elements, num_elements):
            elements.append("{}".format(i + m*j))
        cosets.append(elements)
    return cosets

def convert_to_cell(collumn, row):
    collumn -= 1
    if collumn/26 < 1:
        collumn = chr(ord('A')+collumn)
    else: 
        collumn = "{}{}".format(
            chr(ord('A')+(collumn//26)-1), chr(ord('A')+collumn % 26))
    return "{}{}".format(collumn, row)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This script creates the addition table for each coset of Zm')
    parser.add_argument('m', type=int,
                        help='input m')
    parser.add_argument('num_elements', type=int,
                        help='input number of elements to display')
    args = parser.parse_args()
    coset_addtion_table(args.m, args.num_elements)
