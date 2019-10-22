import psycopg2


def insert_one_shop(connection, name, street):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO public.\"Shop\" (\"ShopName\", \"ShopStreet\") 
            VALUES (%s,%s)"""
        record_to_insert = (name, street)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def insert_many_random_shops(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute("INSERT INTO public.\"Shop\"(\"ShopName\", \"ShopStreet\") select left(md5(random()::text), 10),"
                       "left(md5(random()::text), 10) from generate_series(1, {})".format(count))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def update_one_shop(connection, shopId, name, street):
    try:
        cursor = connection.cursor()
        sql_update_query = """UPDATE public.\"Shop\" SET \"ShopName\"='{}', \"ShopStreet\"='{}' WHERE \"ShopId\"={}""" \
            .format(name, street, shopId)
        cursor.execute(sql_update_query)
        connection.commit()

    except (Exception, psycopg2.Error) as err:
        print("Error while updating PostgresSQL table", err)


def insert_one_customer(connection, name, phone, sex):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO public.\"Customer\" (\"CustomerName\", \"CustomerPhone\", \"CustomerSex\") 
            VALUES (%s,%s,%s)"""
        record_to_insert = (name, phone, sex)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def insert_many_random_customers(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO public.\"Customer\"(\"CustomerName\", \"CustomerPhone\", \"CustomerSex\") select left(md5(random()::text), 10),"
            "  format('+380 %s%s %s%s%s %s%s %s%s', a[1], a[2], a[3], a[4], a[5], a[6], a[7], a[8], a[9]),"
            " ('male') from (select ARRAY (SELECT trunc(random() * 10)::int FROM   generate_series(1, 9)) AS a,generate_series(1, {})) sub;".format(
                count))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def update_one_customer(connection, customerId, name, phone, sex):
    try:
        cursor = connection.cursor()
        sql_update_query = """UPDATE public.\"Customer\" SET \"CustomerName\"='{}', \"CustomerPhone\"='{}', \"CustomerSex\"='{}'
            WHERE \"CustomerId\"={}""" \
            .format(name, phone, sex, customerId)
        cursor.execute(sql_update_query)
        connection.commit()

    except (Exception, psycopg2.Error) as err:
        print("Error while updating PostgresSQL table", err)


def insert_one_item(connection, name, price, quantity, color, material, description):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO public.\"Item\" (\"ItemName\", \"ItemPrice\", \"ItemQuantity\", \"ItemColor\", \"ItemMaterial\", \"ItemDescriptions\") 
            VALUES (%s,%s,%s,%s,%s,%s)"""
        record_to_insert = (name, price, quantity, color, material, description)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def insert_many_random_items(connection, count):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO public.\"Item\"(\"ItemName\", \"ItemPrice\", \"ItemQuantity\", \"ItemColor\", \"ItemMaterial\", \"ItemDescriptions\") select left(md5(random()::text), 10), floor(random() * 100 + 100)::int, floor(random() * 10 + 1)::int, left(md5(random()::text), 10), left(md5(random()::text), 10), left(md5(random()::text), 100) from generate_series(1, {})".format(
                count))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def update_one_item(connection, itemId, name, price, quantity, color, material, description):
    try:
        cursor = connection.cursor()
        sql_update_query = """UPDATE public.\"Item\" SET \"ItemName\"='{}', \"ItemPrice\"='{}', \"ItemQuantity\"='{}', \"ItemColor\"='{}', \"ItemMaterial\"='{}', \"ItemDescriptions\"='{}'
            WHERE \"ItemId\"={}""" \
            .format(name, price, quantity, color, material, description, itemId)
        cursor.execute(sql_update_query)
        connection.commit()

    except (Exception, psycopg2.Error) as err:
        print("Error while updating PostgresSQL table", err)


def insert_one_order(connection, itemId, shopId, customerId, date):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO public.\"Order\" (\"ItemId\", \"ShopId\", \"CustomerId\", \"OrderDate\") 
            VALUES (%s,%s,%s,%s)"""
        record_to_insert = (itemId, shopId, customerId, date)
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def insert_many_random_orders(connection, count, itemId, customerId, shopId):
    try:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO public.\"Order\"(\"CustomerId\", \"ItemId\", \"ShopId\", \"OrderDate\") select {}, {}, {}, "
            "date((current_date - '15 years'::interval) + trunc(random() * 365) * '1 day'::interval + "
            "trunc(random() * 14) * '1 year'::interval ) from generate_series(1, {})".format(
                itemId, customerId, shopId, count))
        connection.commit()
        cursor.close()
    except (Exception, psycopg2.Error) as err:
        if connection:
            print("Failed to insert record into table", err)


def update_one_order(connection, orderId, itemId, shopId, customerId, date):
    try:
        cursor = connection.cursor()
        sql_update_query = """UPDATE public.\"Order\" SET \"ItemId\"='{}', \"ShopId\"='{}', \"CustomerId\"='{}', \"OrderDate\"='{}'
                WHERE \"OrderId\"={}""" \
            .format(itemId, shopId, customerId, date, orderId)
        cursor.execute(sql_update_query)
        connection.commit()

    except (Exception, psycopg2.Error) as err:
        print("Error while updating PostgresSQL table", err)


def delete_one(connection, anyId, nameTable):
    try:
        cursor = connection.cursor()
        ps_delete_query = """DELETE FROM public.\"{}\" WHERE \"{}Id\"={};""".format(nameTable, nameTable, anyId)
        cursor.execute(ps_delete_query)
        connection.commit()

    except (Exception, psycopg2.Error) as err:
        print("Error while connecting to PostgresSQL", err)


def select_all(connection, tableName):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * from \"{}\"".format(tableName)

        cursor.execute(postgreSQL_select_Query)
        records = cursor.fetchall()
        return records

    except (Exception, psycopg2.Error) as err:
        print("Error fetching data from PostgresSQL table", err)


def select_one(connection, tableName, itemId):
    try:
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT * from \"{}\" WHERE \"{}Id\"={}".format(tableName, tableName, itemId)

        cursor.execute(postgreSQL_select_Query)
        record = cursor.fetchall()
        return record

    except (Exception, psycopg2.Error) as err:
        print("Error fetching data from PostgresSQL table", err)
