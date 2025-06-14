class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre

class Curso:
    def __init__(self, nombre, materia):
        self.nombre = nombre
        self.materia = materia
        self.horarios = []
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def agregar_horario(self, horario):
        self.horarios.append(horario)

    def listar_estudiantes(self):
        print(f"Curso: {self.nombre} ({self.materia})")
        for estudiante in self.estudiantes:
            print(f" - {estudiante.nombre}")

    def listar_horarios(self):
        print(f"Horarios del curso {self.nombre}:")
        for horario in self.horarios:
            print(f" - {horario}")

class Horario:
    def __init__(self, dia, hora):
        self.dia = dia
        self.hora = hora

    def __str__(self):
        return f"{self.dia} a las {self.hora}"

# Crear estudiantes independientemente del curso
estudiante1 = Estudiante("Juan")
estudiante2 = Estudiante("luisa")

# Crear cursos, materias y horarios
curso_lit = Curso("Literatura", "Teoría Literaria")
curso_mat = Curso("Matemáticas", "Álgebra")

# Agregar estudiantes a los cursos
curso_lit.agregar_estudiante(estudiante1)
curso_mat.agregar_estudiante(estudiante2)

# Agregar horarios a los cursos
horario_lit = Horario("Lunes", "10:00 AM")
horario_mat = Horario("Miércoles", "2:00 PM")
curso_lit.agregar_horario(horario_lit)
curso_mat.agregar_horario(horario_mat)

# Listar estudiantes y horarios
curso_lit.listar_estudiantes()
curso_lit.listar_horarios()

curso_mat.listar_estudiantes()
curso_mat.listar_horarios()
