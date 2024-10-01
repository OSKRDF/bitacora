import pymysql



host = 'db-bitacora.clmee0uoed5e.us-east-2.rds.amazonaws.com'
user = 'oscar'
password = "12345678"
db_name = "bitacora_db"

def connection_SQL():
    try:
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
         )
        print("Succesfull connection to database")
        return connection
    except Exception as err:
        print("Error",err)
        return None


def insert (code, name, lastname, project, hours, date):
    try:

        #instruction = "INSERT INTO bitacora_db VALUES("+code+",'"+name+"','"+lastname+"','"+project+"','"+hours+"','"+date+"');"
        instruction = f"INSERT INTO bitacora_db (code, name, lastname, project, hours, date) VALUES ('{code}', '{name}', '{lastname}', '{project}', {hours}, '{date}');"
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        connection.commit()
        print("User added")
        return "ok" 

    except Exception as err:
        print("Error",err)
        return None

#insert()

def consult(code):
    try:
        print("codigo"+code);
        #instruction = "SELECT * FROM users WHERE id=" + id
        instruction = "SELECT * FROM bitacora_db WHERE code=" + code
        connection = connection_SQL()
        cursor = connection.cursor()
        cursor.execute(instruction)
        result = cursor.fetchall()
        return result
    except Exception as err:
        print("Error", err)
        return None