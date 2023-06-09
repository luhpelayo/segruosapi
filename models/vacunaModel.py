from database.db import get_connection
from .entities.Vacuna import Vacuna


class VacunaModel:
	@classmethod
	def get_vacuna(self, ci):
		try:
			sQuery = f"SELECT v.idvac, v.nombre, v.dosis_requeridas, v.paciente_id FROM persona p ,vacuna v, paciente a where p.ci=a.ci_persona  and v.paciente_id = a.idpac and p.ci =  {ci};"
			connection = get_connection()
			vacunas = []
			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				resultset = cursor.fetchall()
				for row in resultset:
					vacuna = Vacuna(row[0], row[1], row[2], row[3])
					vacunas.append(vacuna.to_JSON())
				connection.close()
			return vacunas
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def add_vacuna(self, vacuna):
		try:
			connection = get_connection()
			sQuery = f"INSERT INTO public.vacuna(nombre, dosis_requeridas, ci_persona) VALUES('{vacuna.nombre}','{vacuna.dosis}',{vacuna.ci})"
			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()
			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def update_vacuna(self, vacuna):
		try:
			connection = get_connection()
			sQuery = f"UPDATE vacuna SET nombre='{vacuna.nombre}', direccion='{vacuna.direccion}', lat={vacuna.lat}, longi={vacuna.long} WHERE idh = {vacuna.id}"

			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()

			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)

	@classmethod
	def delete_vacuna(self, vacuna):
		try:
			connection = get_connection()
			sQuery = f"DELETE FROM vacuna WHERE idh = {vacuna.id}"

			with connection.cursor() as cursor:
				cursor.execute(sQuery)
				affected_rows = cursor.rowcount
				connection.commit()

			connection.close()
			return affected_rows
		except Exception as ex:
			raise Exception(ex)