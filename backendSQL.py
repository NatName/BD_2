import psycopg2


def insert_one(connection, name, street):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO public.\"Shop\" (\"ShopId\", \"ShopName\", \"ShopStreet\") VALUES (%s,%s,%s)"""
        record_to_insert = (6, name, street)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        cursor.close()

    except (Exception, psycopg2.Error) as error:
        if connection:
            print("Failed to insert record into table", error)
