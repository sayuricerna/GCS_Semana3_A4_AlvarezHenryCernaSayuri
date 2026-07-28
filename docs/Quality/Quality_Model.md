# Modelo de Calidad del Software

## 1. Información general

**Sistema:** Gestión de Citas Médicas del Consultorio MATER  
**Modelo seleccionado:** ISO/IEC 25010  
**Versión:** 1.0  
**Estado:** Aprobado  

## 2. Objetivo

Establecer características y métricas verificables para evaluar la calidad del sistema de gestión de citas médicas.

Las métricas permiten transformar expresiones generales como “el sistema debe ser rápido” o “debe ser seguro” en criterios que puedan comprobarse mediante pruebas, revisiones o evidencias del repositorio.

## 3. Atributos de calidad

| Atributo | Definición | Métrica verificable | EC que lo soporta |
|---|---|---|---|
| Adecuación funcional | Capacidad del sistema para cumplir las funciones solicitadas. | El 100 % de las pruebas de validación y disponibilidad de citas deberá aprobarse. | `SRS_v1.md`, `/src`, `/tests` |
| Fiabilidad | Capacidad de mantener el funcionamiento esperado sin producir resultados incorrectos. | El sistema deberá rechazar el 100 % de los intentos de registrar una cita duplicada. | `/src`, `/tests` |
| Usabilidad | Facilidad con la que el usuario puede comprender y utilizar el sistema. | Al menos 4 de 5 usuarios deberán comprender los mensajes de validación sin recibir ayuda adicional. | `SRS_v1.md`, `README.md` |
| Eficiencia de desempeño | Capacidad de responder en un tiempo adecuado utilizando los recursos disponibles. | Al menos el 95 % de 100 consultas de disponibilidad deberá responder en un máximo de 2 segundos. | `/src`, `/tests` |
| Seguridad | Protección de la información frente a accesos o exposiciones no autorizadas. | El repositorio deberá contener 0 contraseñas, tokens, credenciales o datos médicos reales. | `/config`, `/src`, `CM_PLAN.md` |
| Mantenibilidad | Facilidad para modificar o corregir el sistema sin afectar sus funciones. | El 100 % de las funciones críticas deberá contar con al menos una prueba automatizada relacionada. | `/src`, `/tests`, `CM_PLAN.md` |

## 4. Métricas estrella

### Métrica estrella 1: prevención de citas duplicadas

El sistema deberá rechazar el 100 % de los intentos de asignar al mismo médico dos citas en la misma fecha y hora.

**Importancia:** esta métrica evita conflictos de horario y problemas en la atención de los pacientes.

**Evidencia:** resultado de la prueba `test_occupied_slot`.

### Métrica estrella 2: tiempo de consulta de disponibilidad

Al menos el 95 % de 100 consultas de disponibilidad deberá responder en un tiempo igual o menor a 2 segundos.

**Importancia:** esta métrica permite que la recepcionista consulte los horarios sin retrasos durante la programación de citas.

**Evidencia:** prueba de rendimiento que se agregará como cambio controlado después de establecer la línea base `v1.0`.

## 5. Método de validación

| Métrica | Método | Evidencia esperada |
|---|---|---|
| Pruebas funcionales aprobadas | Ejecución de pruebas automatizadas | Captura de terminal |
| Citas duplicadas rechazadas | Caso de prueba con horario ocupado | Resultado correcto |
| Mensajes comprensibles | Revisión con usuarios | Checklist de evaluación |
| Respuesta máxima de 2 segundos | Medición de 100 consultas | Captura de la prueba |
| Ausencia de credenciales | Revisión del repositorio | Lista de verificación |
| Funciones críticas probadas | Comparación entre código y pruebas | Matriz de trazabilidad |