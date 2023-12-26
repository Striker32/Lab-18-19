import psycopg2
from psycopg2.extensions import register_type, UNICODE
CONN_STR = "host='10.163.31.228' dbname='rpr' user='pryashin_m' password='e285adfb'"

def print_cars():
    register_type(UNICODE)
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.execute('select * from car')
    cols = cur.description
    row = cur.fetchone()
    while row:
        for i in range(len(cols)):
            print(row[i])
        print('#'*10)
        row = cur.fetchone()
    cur.close()
    conn.close()

def car_add (car_name, model, date, colour, category, price):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.callproc('car_add', [car_name, model, date, colour, category, price])
    conn.commit()
    cur.close()
    conn.close()

def car_delete (car_name):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.callproc('car_delete', [car_name])
    conn.commit()
    cur.close()
    conn.close()

def car_update_date (car_name, date):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.callproc('car_update_date', [car_name, date])
    conn.commit()
    cur.close()
    conn.close()

def car_update_price (car_name, price):
    conn = psycopg2.connect(CONN_STR)
    cur = conn.cursor()
    cur.callproc('car_update_price', [car_name, price])
    conn.commit()
    cur.close()
    conn.close()

def run():
    choice = 0
    choices = {
        1: lambda: print_cars(), ## car_name, model, date, colour, category, price
        2: lambda: car_add(input('car name (text id): '), input('model (text: BMW, Nissan): '),
                              input('date (date: 2018-05-08): '), input('colour (text): '),
                              input('category(text): '), input('price (int): ')),
        3: lambda: car_delete(input('car name: ')),
        4: lambda: car_update_date(input('car_name: '), input('date: ')),
        5: lambda: car_update_price(input('car_name: '), input('price: ')),
    }
    while (choice != 6):
        print()
        print('1. print cars')
        print('2. add car')
        print('3. delete car')
        print('4. change car date')
        print('5. change car price')
        print('6. EXIT')
        choice = int(input())
        if choice in choices:
            choices[choice]()
        else:
            print('Wrong  input!')


if __name__ == '__main__':
    run()