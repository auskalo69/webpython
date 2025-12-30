from MySQLdb import connect


def sql_execute(datos_acceso, sql, parametros=()): 
    conexion = connect(**datos_acceso)
    cursor = conexion.cursor()
    cursor.execute(sql, parametros)

    if not sql.upper().find('SELECT') > -1:
        conexion.commit()
        data = cursor.lastrowid
    else:
        data = cursor.fetchall()

    cursor.close()
    conexion.close()

    return data    
