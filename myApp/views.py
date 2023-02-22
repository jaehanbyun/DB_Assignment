from django.shortcuts import render
from django.shortcuts import redirect
from django.db import connection
import json

def base(request):
    return render(request, 'myApp/base.html')

def display(request):
    outputProducts = []
    outputPCs = []
    outputLaptops = []
    outputPrinters = []
    with connection.cursor() as cursor:
        sqlQueryProducts = "SELECT maker, model, type FROM Product;"
        cursor.execute(sqlQueryProducts)
        fetchResultProducts = cursor.fetchall()

        sqlQueryPCs = "SELECT model, speed, ram, hd, price FROM PC;"
        cursor.execute(sqlQueryPCs)
        fetchResultPCs = cursor.fetchall()

        sqlQueryLaptops = "SELECT model, speed, ram, hd, screen, price FROM Laptop;"
        cursor.execute(sqlQueryLaptops)
        fetchResultLaptops = cursor.fetchall()

        sqlQueryPrinters = "SELECT model, color, type, price FROM Printer;"
        cursor.execute(sqlQueryPrinters)
        fetchResultPrinters = cursor.fetchall()

        connection.commit()
        connection.close()

        for temp in fetchResultProducts:
            eachRow = {'maker': temp[0], 'model': temp[1], 'type': temp[2]}
            outputProducts.append(eachRow)

        for temp in fetchResultPCs:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2]}
            outputPCs.append(eachRow)

        for temp in fetchResultLaptops:
            eachRow = {'model': temp[0], 'speed': temp[1], 'ram': temp[2], 'hd': temp[3], 'screen': temp[4],
                       'price': temp[5]}
            outputLaptops.append(eachRow)

        for temp in fetchResultPrinters:
            eachRow = {'model': temp[0], 'color': temp[1], 'type': temp[2], 'price': temp[3]}
            outputPrinters.append(eachRow)

    return render(request, 'myApp/display.html', {"products": outputProducts, "pcs": outputPCs, "laptops": outputLaptops,
                                               "printers": outputPrinters})


def createTable(request):
    with connection.cursor() as cursor:
        sqlQuery1 = '''CREATE TABLE if not exists Product (
                        maker VARCHAR(10) NOT NULL,
                        model INT NOT NULL PRIMARY KEY,
                        type VARCHAR(10)
                        );
                        '''
        cursor.execute(sqlQuery1)

        sqlQuery2 = '''CREATE TABLE if not exists PC (
                        model INT NOT NULL PRIMARY KEY,
                        speed FLOAT NOT NULL,
                        ram INT NOT NULL,
                        hd INT NOT NULL,
                        price INT NOT NULL 
                        );
                        '''
        cursor.execute(sqlQuery2)

        sqlQuery3 = '''CREATE TABLE if not exists Laptop (
                        model INT NOT NULL PRIMARY KEY,
                        speed FLOAT NOT NULL,
                        ram INT NOT NULL,
                        hd INT NOT NULL,
                        screen FLOAT NOT NULL, 
                        price INT NOT NULL 
                        );
                        '''
        cursor.execute(sqlQuery3)

        sqlQuery4 = '''CREATE TABLE if not exists Printer (
                        model INT NOT NULL PRIMARY KEY,
                        color BIT NOT NULL,
                        type VARCHAR(15) NOT NULL,
                        price INT NOT NULL
                        );
                        '''
        cursor.execute(sqlQuery4)

        connection.commit()
        connection.close()

    return redirect('base')

def insertTable(request):
    with connection.cursor() as cursor:
        with open('myApp/DBdata/Product.json', encoding='utf-8', mode='r') as p:
            json_data = json.load(p)
            json_line = json_data['Product']

            for a in json_line:
                maker = a['maker']
                model = a['model']
                type = a['type']

                sql = "INSERT INTO Product(maker, model, type) VALUES (%s, %s, %s)"
                val = (maker, int(model), type)

                cursor.execute(sql, val)

        with open('myApp/DBdata/PC.json', encoding='utf-8', mode='r') as c:
            json_data = json.load(c)
            json_line = json_data['PC']

            for a in json_line:
                model = a['model']
                speed = a['speed']
                ram = a['ram']
                hd = a['hd']
                price = a['price']

                sql = '''INSERT INTO PC(model, speed, ram, hd, price) VALUES (%s, %s, %s, %s, %s)'''
                val = (int(model), float(speed), int(ram), int(hd), int(price))

                cursor.execute(sql, val)

        with open('myApp/DBdata/Laptop.json', encoding='utf-8', mode='r') as l:
            json_data = json.load(l)
            json_line = json_data['Laptop']

            for a in json_line:
                model = a['model']
                speed = a['speed']
                ram = a['ram']
                hd = a['hd']
                screen = a['screen']
                price = a['price']

                sql = '''INSERT INTO Laptop(model, speed, ram, hd, screen, price) VALUES (%s, %s, %s, %s, %s, %s)'''
                val = (int(model), float(speed), int(ram), int(hd), float(screen), int(price))

                cursor.execute(sql, val)

        with open('myApp/DBdata/Printer.json', encoding='utf-8', mode='r') as t:
            json_data = json.load(t)
            json_line = json_data['Printer']

            for a in json_line:
                model = a['model']
                color = a['color']
                type = a['type']
                price = a['price']

                sql = '''INSERT INTO Printer(model, color, type, price) VALUES (%s, %s, %s, %s)'''
                val = (int(model), bool(color), type, int(price))

                cursor.execute(sql, val)

        connection.commit()
        connection.close()

    return redirect('base')

def inserteach(request):
    type = request.GET.get('thing')
    content = request.GET.get('text1')
    print(type)
    print(content)
    content = json.loads(content)
    with connection.cursor() as cursor:
        if type=="Product" :
            maker = content['maker']
            model = content['model']
            type = content['type']

            sql = "INSERT INTO Product(maker, model, type) VALUES (%s, %s, %s)"
            val = (maker, int(model), type)

            cursor.execute(sql, val)

        elif type=="PC":
            model = content['model']
            speed = content['speed']
            ram = content['ram']
            hd = content['hd']
            price = content['price']

            sql = '''INSERT INTO PC(model, speed, ram, hd, price) VALUES (%s, %s, %s, %s, %s)'''
            val = (int(model), float(speed), int(ram), int(hd), int(price))

            cursor.execute(sql, val)

        elif type=="Laptop":
            model = content['model']
            speed = content['speed']
            ram = content['ram']
            hd = content['hd']
            screen = content['screen']
            price = content['price']

            sql = '''INSERT INTO Laptop(model, speed, ram, hd, screen, price) VALUES (%s, %s, %s, %s, %s, %s)'''
            val = (int(model), float(speed), int(ram), int(hd), float(screen), int(price))

            cursor.execute(sql, val)

        elif type=="Printer":
            model = content['model']
            color = content['color']
            type = content['type']
            price = content['price']

            sql = '''INSERT INTO Printer(model, color, type, price) VALUES (%s, %s, %s, %s)'''
            val = (int(model), bool(color), type, int(price))

            cursor.execute(sql, val)

        connection.commit()
        connection.close()

    return redirect('base')


def resultview1(request):
    output = []
    with connection.cursor() as cursor:
        sql = '''SELECT AVG(hd) FROM PC;'''
        cursor.execute(sql)
        fetchResult = cursor.fetchall()
        connection.commit()
        connection.close()
        for temp in fetchResult:
            eachRow = {'hd': float(temp[0])}
            print(eachRow)
            output.append(eachRow)

    return render(request, 'myApp/View1.html', {"output": output})


def resultview2(request):
    output = []
    with connection.cursor() as cursor:
        sql = '''SELECT Product.maker, AVG(Laptop.speed) AS AvgSpeed
                    FROM Product, Laptop
                    WHERE Product.model = Laptop.model
                    GROUP BY Product.maker
                    ORDER BY maker;'''
        cursor.execute(sql)
        fetchResult = cursor.fetchall()
        connection.commit()
        connection.close()

    for temp in fetchResult:
        eachRow = {'maker': temp[0], 'AvgSpeed': temp[1]}
        output.append(eachRow)

    return render(request, 'myApp/View2.html', {"output": output})


def resultview3(request):
    output = []
    with connection.cursor() as cursor:
        sql = '''select D.maker, C.price
                    FROM Laptop C, (
                          SELECT  B.maker, COUNT(B.model) as cnt 
                             FROM Laptop A, Product B
                             WHERE A.model = B.model
                          GROUP BY B.maker) D,
                            Product E
                    WHERE D.maker = E.maker
                    AND C.model = E.model
                    AND D.cnt = 1;'''
        cursor.execute(sql)
        fetchResult = cursor.fetchall()
        connection.commit()
        connection.close()

    for temp in fetchResult:
        eachRow = {'maker': temp[0], 'price': temp[1]}
        output.append(eachRow)

    return render(request, 'myApp/View3.html', {"output": output})


def resultview4(request):
    output = []
    with connection.cursor() as cursor:
        sql = '''select E.maker, D.model, D.price 
                        FROM (
                              select A.maker,  MAX(B.price) as price
                              FROM product A, printer B
                              WHERE A.model = B.model
                              GROUP BY A.maker ) C,
                                printer D,
                                product E
                        WHERE C.maker = E.maker
                        and C.price = D.price
                        and D.model = E.model;'''
        cursor.execute(sql)
        fetchResult = cursor.fetchall()
        connection.commit()
        connection.close()

    for temp in fetchResult:
        eachRow = {'maker': temp[0], 'model': temp[1], 'price': temp[2]}
        output.append(eachRow)

    return render(request, 'myApp/View4.html', {"output": output})
