# Impacto de un Cambio en el Ciclo de Desarrollo

## 1. Información del cambio

**Sistema:** Gestión de Citas Médicas del Consultorio MATER  
**Identificador del cambio:** CHG-001  
**Caso seleccionado:** Rendimiento  
**Estado:** Planificado  
**Responsable:** Equipo de desarrollo  

## 2. Descripción del cambio

Se propone incorporar el siguiente requisito no funcional:

> El sistema deberá responder en un tiempo igual o menor a 2 segundos en al menos el 95 % de las consultas de disponibilidad de horarios.

Este cambio permitirá comprobar que la consulta de citas puede utilizarse sin retrasos durante la atención al paciente.

## 3. Justificación

Una consulta lenta puede ocasionar demoras en recepción, acumulación de pacientes y errores durante la asignación de horarios. Por esta razón, el rendimiento debe expresarse mediante una métrica verificable y relacionarse con requisitos, código y pruebas.

## 4. Impacto por fase

| Fase | ¿Qué cambia? | EC afectados | Riesgo si no se controla | Evidencia de validación |
|---|---|---|---|---|
| Requisitos | Se agrega el requisito no funcional de respuesta máxima de 2 segundos y su criterio de aceptación. | `SRS_v1.md` | El requisito puede quedar ambiguo y provocar diferentes interpretaciones. | Checklist y revisión del SRS |
| Diseño | Se revisa el mecanismo utilizado para buscar citas y verificar horarios disponibles. | `SRS_v1.md`, `appointment_validation.py` | Se puede utilizar una solución lenta o difícil de mantener. | Revisión técnica de la solución |
| Implementación | Se analiza o modifica la función que comprueba la disponibilidad de horarios. | `appointment_validation.py` | El cambio puede afectar la validación de citas existentes. | Commit del cambio y revisión de código |
| Pruebas | Se agrega una prueba que ejecuta 100 consultas y mide su tiempo de respuesta. | `test_appointment_validation.py` | Se puede afirmar que el sistema es rápido sin contar con evidencia verificable. | Captura de ejecución de pruebas |
| Despliegue | Se comprueba que la versión desplegada corresponda con los EC aprobados. | `README.md`, `config.example`, `CHANGELOG.md` | Se podría desplegar una versión diferente de la evaluada. | Revisión del tag y del historial |
| Mantenimiento | Se registra el cambio y se conserva la relación con la línea base anterior. | `CHANGELOG.md`, `CM_PLAN.md` | Se perdería la historia y la justificación del cambio. | Historial Git y comparación con `v1.0` |

## 5. Fase más costosa

La implementación se considera la fase más costosa porque el requisito de rendimiento puede obligar a modificar la lógica utilizada para consultar citas. Una modificación incorrecta podría afectar la validación de horarios o permitir citas duplicadas.

Además, después de cambiar el código es necesario ejecutar nuevamente las pruebas funcionales para confirmar que las funciones anteriores continúan trabajando correctamente.

## 6. Elementos de configuración involucrados

| EC | Cambio esperado |
|---|---|
| `SRS_v1.md` | Incorporar el requisito de rendimiento |
| `Quality_Model.md` | Mantener la métrica de máximo 2 segundos |
| `appointment_validation.py` | Revisar la función de consulta |
| `test_appointment_validation.py` | Agregar la prueba de rendimiento |
| `CHANGELOG.md` | Registrar el cambio posterior a la línea base |
| `CM_PLAN.md` | Mantener la trazabilidad del cambio |

## 7. Trazabilidad del cambio

| Cambio | Requisito | Código | Prueba | Evidencia |
|---|---|---|---|---|
| CHG-001 | RNF de rendimiento | `appointment_validation.py` | Prueba de 100 consultas | Commit posterior a `v1.0` |

## 8. Estado del cambio

El cambio será implementado después de establecer la línea base `v1.0`. Esto permitirá demostrar la diferencia entre la versión aprobada y la modificación posterior.