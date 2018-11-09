# ----記帳程式
# 讀取檔案
# 讓user輸入商品與價格
# 印出所有購買記錄
# 寫入檔案

import os

def read_file(filename, products):
    with open(filename, 'r', encoding='UTF-8') as f:
        for line in f:
            if '商品, 價格' in line:
                continue
            else:
                name, price = line.strip().split(',')
                products.append([name, price])
    return products

def user_input(products):
    while True:
        name = input('請輸入商品名稱: ')
        if name == 'q':
            break
        price = input('請輸入商品價格: ')
        products.append([name, price])
    return products

def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])

def write_file(filename, products):
    with open(filename, 'w', encoding='UTF-8') as f:
        f.write('商品, 價格\n')
        for p in products:
            f.write(p[0]+','+p[1]+'\n')



def main():
    filename = 'products.csv'
    products = []
    if os.path.isfile(filename):
        print('我找到了!')
        products = read_file(filename, products)
    else:
        print('找不到檔案!')
    products = user_input(products)
    print_products(products)
    write_file(filename, products)

main()