import sqlite3


class SQL_Requests():
    def __init__(self):
        self.conn = sqlite3.connect('control_robindb.sqlite')
        self.cur = self.conn.cursor()

    def muestraMedicamentos(self, mascota_id):
        self.cur.execute(
            '''SELECT medicamentos.nombre_med, vacunas_realizadas.fecha_realizada,
            vacunas_realizadas.descripcion, vacunas_realizadas.fecha_futura
            FROM Vacunas_Realizadas JOIN Medicamentos JOIN Tipo_med JOIN mascotas JOIN tipo_mascotas
            ON medicamentos.id = vacunas_realizadas.med_id AND vacunas_realizadas.tipo_med_id = tipo_med.id
            AND mascotas.tipo_mascota_id = tipo_mascotas.id AND mascotas.id = vacunas_realizadas.mascota_id
            WHERE tipo_med.id = 1 AND vacunas_realizadas.mascota_id = ?''', (mascota_id,))
        return self.cur.fetchall()

    def muestraVacunas(self, mascota_id):
        self.cur.execute(
            '''SELECT medicamentos.nombre_med, vacunas_realizadas.fecha_realizada,
            vacunas_realizadas.descripcion, vacunas_realizadas.fecha_futura
            FROM Vacunas_Realizadas JOIN Medicamentos JOIN Tipo_med JOIN mascotas JOIN tipo_mascotas
            ON medicamentos.id = vacunas_realizadas.med_id AND vacunas_realizadas.tipo_med_id = tipo_med.id
            AND mascotas.tipo_mascota_id = tipo_mascotas.id AND mascotas.id = vacunas_realizadas.mascota_id
            WHERE tipo_med.id = 2 AND vacunas_realizadas.mascota_id = ?''', (mascota_id,))
        registros = self.cur.fetchall()
        if registros is None:
            return False
        else:
            return registros

    def muestraInfo(self, mascota_id):
        self.cur.execute(
            '''SELECT tipo_mascotas.nombre, mascotas.nombre, razas.raza, mascotas.color, sexo.nombre, strftime('%d-%m-%Y',mascotas.nacimiento) as fecha, pesos.peso
                FROM mascotas
                JOIN tipo_mascotas, Pesos, sexo, Razas ON tipo_mascotas.id = mascotas.tipo_mascota_id
                AND mascotas.id = pesos.mascota_id AND mascotas.sexo_id = sexo.id AND mascotas.raza = razas.id
                WHERE mascotas.id = ?
                ORDER BY  pesos.fecha_peso DESC LIMIT 1''', (mascota_id,))
        registros = self.cur.fetchone()
        if registros is None:
            return False
        else:
            return registros

    def insertaMed(self, nombre_med, tipo_med):
        self.cur.execute('''SELECT id FROM Tipo_med WHERE nombre_tipo = ?''', (tipo_med,))
        tipo_med_id = self.cur.fetchone()[0]
        self.cur.execute('''INSERT INTO Medicamentos(nombre_med,tipo_med_id)
                         VALUES (?,?)''', (nombre_med, tipo_med_id))
        self.conn.commit()

    def insertaVa(self, nombre_med, tipo_med, fecha_fut, descripcion):
        self.cur.execute('''SELECT id FROM Tipo_med WHERE nombre_tipo = ?''', (tipo_med,))
        tipo_med_id = self.cur.fetchone()[0]
        self.cur.execute('''SELECT id FROM Medicamentos WHERE nombre_med = ? ''', (nombre_med,))
        try:
            med_id = self.cur.fetchone()[0]
        except:
            return False
        self.cur.execute('''INSERT INTO Vacunas_Realizadas(med_id,tipo_med_id,descripcion,fecha_futura)
                         VALUES (?,?,?,?)''', (med_id, tipo_med_id, descripcion, fecha_fut))
        self.conn.commit()

    def registraMascota(self, nombre, especie, sexo, nacimiento, raza, peso, color):
        self.cur.execute('''SELECT id FROM tipo_mascotas WHERE nombre = ? ''', (especie,))
        tipo_mascota_id = self.cur.fetchone()[0]
        self.cur.execute('''INSERT INTO Mascotas(nombre,raza,color,sexo,nacimiento,tipo_mascota_id)
                         VALUES(?,?,?,?,?,?)''', (nombre, raza, color, sexo, nacimiento, tipo_mascota_id))
        self.cur.execute(
            '''SELECT id from Mascotas
            WHERE  nombre = ?
            ORDER BY id DESC LIMIT 1''', (nombre,))
        mascota_id = self.cur.fetchone()[0]
        self.cur.execute('''INSERT INTO Pesos(Peso,mascota_id) VALUES(?,?)''', (peso, mascota_id))
        self.conn.commit()

    def medsYTipos(self):
        self.cur.execute(
            '''SELECT medicamentos.nombre_med, tipo_med.nombre_tipo
            FROM Medicamentos JOIN Tipo_med ON Tipo_med.id = Medicamentos.tipo_med_id''')
        return self.cur.fetchall()

    def eliminarRegistros(self, id):
        self.cur.execute('''DELETE FROM Vacunas_Realizadas WHERE mascota_id = ?''', (id,))
        self.cur.execute('''DELETE FROM mascotas WHERE id = ? ''', (id,))
        self.cur.execute('''DELETE FROM Pesos WHERE mascota_id = ? ''', (id,))
        self.conn.commit()

    def todasMascotas(self):
        self.cur.execute('''SELECT mascotas.nombre FROM mascotas''')
        return self.cur.fetchall()

    def obtienePeso(self, mascota_id):
        self.cur.execute('''SELECT peso, fecha_peso FROM Pesos WHERE mascota_id = ? ORDER BY fecha_peso ASC''',
                         (mascota_id,))
        return self.cur.fetchall()

    def editaMascota(self, nombre, especie, sexo, nacimiento, raza, peso, color, mascota_id):
        self.cur.execute('''SELECT id FROM tipo_mascotas WHERE nombre = ? ''', (especie,))
        tipo_mascota_id = self.cur.fetchone()[0]
        self.cur.execute(
            '''UPDATE Mascotas
            SET nombre = ?,
            raza = ? ,
            color = ?,
            sexo = ?,
            nacimiento = ?,
            tipo_mascota_id = ?
            WHERE id = ?''', (nombre, raza, color, sexo, nacimiento, tipo_mascota_id, mascota_id))
        self.cur.execute('''SELECT id FROM Pesos WHERE mascota_id = ? ORDER BY fecha_peso DESC LIMIT 1''',(mascota_id,))
        peso_id = self.cur.fetchone()[0]
        self.cur.execute('''UPDATE Pesos SET Peso = ?, mascota_id = ? WHERE id = ?''', (peso, mascota_id, peso_id))
        self.conn.commit()

    def datosEspecies(self):
        self.cur.execute('SELECT * FROM tipo_mascotas')
        return self.cur.fetchall()

    def datosSexo(self):
        self.cur.execute('SELECT * FROM sexo')
        return self.cur.fetchall()

    def datosRaza(self):
        self.cur.execute('SELECT * FROM Razas')
        return self.cur.fetchall()

    def ingresarPeso(self,peso,fecha,mascota_id):
        self.cur.execute('INSERT INTO Pesos(peso,fecha_peso,mascota_id) VALUES(?,?,?)',(peso,fecha,mascota_id))
        self.conn.commit()