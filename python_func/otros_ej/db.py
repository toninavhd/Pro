def fix_ids(db):
    # Creamos una copia de la base de datos original para no modificarla directamente
    new_db = db.copy()

    # Ordenamos los registros por el ID actual
    new_db.sort(key=lambda x: x['id_empleado'])

    # Asignamos nuevos IDs secuenciales empezando desde 1
    for i, registro in enumerate(new_db):
        registro['id_empleado'] = i + 1

    return new_db

