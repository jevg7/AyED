import controllers.dao as dao
import model.clases as c

notas = dao.Promedio()

david = c.Estudiante("001", "David", "Espinoza", "ISI")
alg = c.Asignatura("Alg y Est", "Segunda facil", 6)

nota = c.Nota(david, alg, 85)

notas.agregar_nota(nota)