# Especificación de Requisitos de Software

## 1. Información del documento

| Campo | Descripción |
|---|---|
| Sistema | MATER |
| Tipo de sistema | Gestión de citas ginecológicas |
| Versión del documento | 1.0 |
| Integrantes | Henry Alvarez y Sayuri Cerna |
| Estado | Versión inicial |

## 2. Propósito

El propósito de este documento es definir los requisitos funcionales y no
funcionales del sistema MATER, orientado a la gestión de citas de un
consultorio ginecológico.

Este documento sirve como referencia para identificar el alcance del
sistema, relacionar las funciones con los elementos de configuración y
establecer criterios que posteriormente puedan ser validados.

## 3. Alcance

El sistema MATER permitirá representar el registro de pacientes, la
consulta de horarios disponibles, la solicitud, confirmación, cancelación
y reprogramación de citas ginecológicas.

También permitirá consultar el estado de una cita y evitar que se registren
dos citas activas en la misma fecha y hora.

## 4. Actores

### Paciente

Solicita, consulta, cancela o reprograma una cita.

### Recepcionista

Registra pacientes, revisa horarios y confirma citas.

### Médico ginecólogo

Consulta su agenda y registra el estado de la atención.

### Administrador

Controla la información general, la configuración y los usuarios del sistema.

## 5. Flujo principal

1. La paciente proporciona sus datos.
2. La recepcionista registra a la paciente.
3. La paciente selecciona el tipo de consulta.
4. El sistema consulta los horarios disponibles.
5. La paciente selecciona una fecha y una hora.
6. El sistema valida que el horario esté disponible.
7. La cita se registra con estado Pendiente.
8. La recepcionista confirma la cita.
9. Después de la consulta, la cita se registra como Atendida o No asistió.

## 6. Requisitos funcionales

| ID | Requisito funcional |
|---|---|
| RF-01 | El sistema permitirá registrar los datos básicos de una paciente. |
| RF-02 | El sistema permitirá consultar pacientes previamente registradas. |
| RF-03 | El sistema permitirá seleccionar el tipo de consulta ginecológica. |
| RF-04 | El sistema permitirá consultar los horarios disponibles. |
| RF-05 | El sistema permitirá solicitar una cita médica. |
| RF-06 | El sistema permitirá confirmar una cita pendiente. |
| RF-07 | El sistema permitirá cancelar una cita. |
| RF-08 | El sistema permitirá reprogramar una cita. |
| RF-09 | El sistema permitirá consultar el estado de una cita. |
| RF-10 | El sistema permitirá consultar las citas asociadas a una paciente. |
| RF-11 | El sistema permitirá consultar la agenda del consultorio. |
| RF-12 | El sistema impedirá registrar dos citas activas en la misma fecha y hora. |
| RF-13 | El sistema permitirá cambiar el estado de una cita. |
| RF-14 | El sistema permitirá obtener un resumen de citas por estado. |

## 7. Requisitos no funcionales

| ID | Requisito no funcional |
|---|---|
| RNF-01 | El 95 % de las consultas de horarios deberá responder en un tiempo máximo de dos segundos. |
| RNF-02 | El sistema deberá impedir el 100 % de las citas duplicadas en el mismo horario. |
| RNF-03 | Todos los campos obligatorios deberán ser validados antes de registrar una cita. |
| RNF-04 | Los mensajes de validación deberán ser claros y comprensibles. |
| RNF-05 | No deberán almacenarse contraseñas ni claves reales en el repositorio. |
| RNF-06 | Los artefactos principales deberán mantenerse bajo control de versiones. |
| RNF-07 | Los cambios importantes deberán registrarse en `CHANGELOG.md`. |
| RNF-08 | Los requisitos, pruebas y elementos de configuración deberán mantener trazabilidad. |

## 8. Reglas de negocio

| ID | Regla |
|---|---|
| RN-01 | Cada paciente deberá tener una identificación única. |
| RN-02 | Una cita deberá estar asociada a una paciente registrada. |
| RN-03 | No se permitirá más de una cita activa en la misma fecha y hora. |
| RN-04 | Una cita cancelada liberará el horario reservado. |
| RN-05 | Los estados permitidos serán Pendiente, Confirmada, Atendida, Cancelada y No asistió. |
| RN-06 | Una cita solo podrá confirmarse si se encuentra en estado Pendiente. |

## 9. Criterios de aceptación

| Requisito | Criterio de aceptación |
|---|---|
| RF-01 | La paciente queda registrada cuando sus datos obligatorios están completos. |
| RF-04 | Se muestran solamente los horarios que se encuentran disponibles. |
| RF-05 | La cita se registra con fecha, hora, paciente, tipo de consulta y estado. |
| RF-07 | Una cita cancelada cambia correctamente su estado. |
| RF-08 | La nueva fecha y hora deben estar disponibles antes de reprogramar. |
| RF-12 | El sistema rechaza una segunda cita activa en el mismo horario. |
| RNF-01 | La consulta de horarios tarda dos segundos o menos en al menos el 95 % de las validaciones. |
| RNF-05 | No se encuentran contraseñas ni claves reales dentro del repositorio. |

## 10. Matriz inicial de trazabilidad

| Requisito | EC relacionado | Evidencia esperada |
|---|---|---|
| RF-01 | `SRS_v1.md`, `appointment_validation.py` | Revisión documental o prueba de validación |
| RF-04 | `SRS_v1.md`, `appointment_validation.py` | Validación de horarios |
| RF-05 | `SRS_v1.md`, `appointment_validation.py` | Registro de cita |
| RF-07 | `SRS_v1.md`, `test_appointment_validation.py` | Evidencia de cancelación |
| RF-12 | `appointment_validation.py`, `test_appointment_validation.py` | Prueba de citas duplicadas |
| RNF-01 | `Quality_Model.md`, `test_appointment_validation.py` | Evidencia de respuesta menor o igual a dos segundos |
| RNF-05 | `config.example` | Revisión de configuración |
| RNF-08 | `CM_PLAN.md`, `CHANGELOG.md` | Historial de commits y cambios |

## 11. Restricciones

- El proyecto se utilizará con fines académicos.
- Los datos utilizados serán ficticios.
- No se almacenarán datos médicos reales.
- Todos los artefactos deberán encontrarse dentro del repositorio.
- La línea base aprobada será identificada mediante el tag `v1.0`.

## 12. Aprobación

Este documento representa la versión inicial de los requisitos del sistema
MATER y será controlado como un Elemento de Configuración del proyecto.