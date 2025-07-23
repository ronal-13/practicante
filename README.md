-------------------------------------------
# AGENDA DE TAREAS - GRUPO 1

----------------------------

## Instalación y Ejecución Local

### Requisitos Previos
- Python 3.8 o superior
- Pip (gestor de paquetes de Python)

### Instalación

1. **Instala las dependencias**:
   ```
   pip install -r requirements.txt
   ```

2. **Configura la base de datos**:
   ```
   cd agenda
   python manage.py migrate
   ```

3. **Recolecta archivos estaticos** (esto prueba la configuracion de WhiteNoise):
   ```
   python manage.py collectstatic --no-input
   ```

4. **Si se quiere ejecutar de manera local**:
   ```
   python manage.py runserver
   ```

Accede a la aplicación en tu navegador: http://localhost:8000

----------------------------
## Roles del Equipo

| Integrante           | Rol Scrum     |
|--------------------- |---------------|
| **Junior Sulca**     | Scrum Master  |
| **Victor Bazan**     | Product Owner |
| **Tracy Moriano**    | Developer     |
| **Jordan Rojas**     | Developer     |
| **Alee Sayes**       | Developer     |
| **Ronal Asencio**    | Developer     |
-------------------------------------------------------------

## HISTORIAS DE USUARIOS:
🧩 HU1 - Crear nueva tarea
Descripción:
Como usuario, quiero registrar una tarea con título, prioridad, estado y fecha límite, para no olvidar lo que tengo que hacer.

Criterios de Aceptación:

Validar errores en los campos.

Definir el estado de la tarea (Pendiente, En progreso, Completada).

Confirmación visual al guardar.

Prioridad: Alta

🧩 HU2 - Ver lista de tareas
Descripción:
Como usuario, quiero ver todas mis tareas para saber qué pendientes tengo.

Criterios de Aceptación:

Mostrar título, prioridad, estado y fecha.

Resaltar las tareas próximas a vencer.

Prioridad: Alta

🧩 HU3 - Ver detalles de tarea
Descripción:
Como usuario, quiero ver todos los datos de una tarea para tener claridad completa.

Criterios de Aceptación:

Mostrar toda la información de la tarea.

Incluir botón para volver o editar.

Prioridad: Media

🧩 HU4 - Editar tarea
Descripción:
Como usuario, quiero poder editar una tarea para actualizar o corregir cualquier dato.

Criterios de Aceptación:

Permitir editar todos los campos.

Mostrar los datos actuales precargados.

Confirmación visual al guardar los cambios.

Prioridad: Media

🧩 HU5 - Filtrar tareas por estado
Descripción:
Como usuario, quiero filtrar las tareas por estado o prioridad, para organizar mejor mis pendientes.

Criterios de Aceptación:

Filtro por estado: Pendiente, Completada.

Filtro por prioridad: Alta, Media, Baja.

Prioridad: Baja

🧩 HU6 - Eliminar tarea
Descripción:
Como usuario, quiero eliminar una tarea que ya no necesito.

Criterios de Aceptación:

Botón de eliminar visible en el detalle o lista.

Confirmación antes de borrar definitivamente.

Prioridad: Baja

INSTALACIONES:

1. Python Django
2. Bootstrap
--------------------------------
