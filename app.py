import streamlit as st

# Lista para almacenar los alumnos
alumnos = []

# Función para agregar un nuevo alumno
def agregar_alumno(nombre, apellido, asistencia, nota_tp, nota_recuperatorio):
    alumno = {
        "nombre": nombre,
        "apellido": apellido,
        "asistencia": asistencia,
        "nota_tp": nota_tp,
        "nota_recuperatorio": nota_recuperatorio,
        "nota_final": (nota_tp + nota_recuperatorio) / 2
    }
    alumnos.append(alumno)
    st.success(f"Alumno {nombre} {apellido} agregado exitosamente.")

# Función para mostrar el listado completo de alumnos
def mostrar_alumnos():
    if not alumnos:
        st.warning("No hay alumnos registrados.")
    else:
        for alumno in alumnos:
            st.write(f"{alumno['nombre']} {alumno['apellido']} - "
                     f"Asistencia: {alumno['asistencia']}%, "
                     f"Nota TP: {alumno['nota_tp']}, "
                     f"Nota Recuperatorio: {alumno['nota_recuperatorio']}, "
                     f"Nota Final: {alumno['nota_final']}")

# Función para buscar un alumno por nombre y apellido
def buscar_alumno(nombre, apellido):
    for alumno in alumnos:
        if alumno["nombre"] == nombre and alumno["apellido"] == apellido:
            return alumno
    return None

# Función para actualizar los datos de un alumno
def actualizar_alumno(nombre, apellido, asistencia=None, nota_tp=None, nota_recuperatorio=None):
    alumno = buscar_alumno(nombre, apellido)
    if alumno:
        if asistencia is not None:
            alumno["asistencia"] = asistencia
        if nota_tp is not None:
            alumno["nota_tp"] = nota_tp
        if nota_recuperatorio is not None:
            alumno["nota_recuperatorio"] = nota_recuperatorio
        # Recalcular la nota final
        alumno["nota_final"] = (alumno["nota_tp"] + alumno["nota_recuperatorio"]) / 2
        st.success(f"Datos de {nombre} {apellido} actualizados correctamente.")
    else:
        st.error(f"Alumno {nombre} {apellido} no encontrado.")

# Función para eliminar un alumno
def eliminar_alumno(nombre, apellido):
    alumno = buscar_alumno(nombre, apellido)
    if alumno:
        alumnos.remove(alumno)
        st.success(f"Alumno {nombre} {apellido} eliminado.")
    else:
        st.error(f"Alumno {nombre} {apellido} no encontrado.")

# Interfaz de Streamlit
st.title("Gestión de Alumnos")

# Formulario para agregar o actualizar alumnos
st.header("Agregar o Actualizar Alumno")
nombre = st.text_input("Nombre")
apellido = st.text_input("Apellido")
asistencia = st.number_input("Asistencia (%)", min_value=0, max_value=100, value=0)
nota_tp = st.number_input("Nota TP", min_value=0.0, max_value=10.0, value=0.0)
nota_recuperatorio = st.number_input("Nota Recuperatorio", min_value=0.0, max_value=10.0, value=0.0)

if st.button("Agregar Alumno"):
    agregar_alumno(nombre, apellido, asistencia, nota_tp, nota_recuperatorio)

if st.button("Actualizar Alumno"):
    actualizar_alumno(nombre, apellido, asistencia, nota_tp, nota_recuperatorio)

# Mostrar alumnos
st.header("Listado de Alumnos")
if st.button("Mostrar Alumnos"):
    mostrar_alumnos()

# Eliminar alumno
st.header("Eliminar Alumno")
nombre_eliminar = st.text_input("Nombre (Eliminar)")
apellido_eliminar = st.text_input("Apellido (Eliminar)")
if st.button("Eliminar Alumno"):
    eliminar_alumno(nombre_eliminar, apellido_eliminar)
