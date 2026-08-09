# Historial de Cambios

Todos los cambios importantes del Sistema de Gestión de Citas Médicas del Consultorio MATER se registran en este archivo.

## [1.1.1] - 2026-08-09

### Corregido

- CR-004-SEM4-ALVAREZ-CERNA: `is_slot_available` y `register_appointment` ahora normalizan (quitan espacios) la fecha y la hora antes de compararlas, evitando citas duplicadas cuando el mismo horario se registra con espacios adicionales (por ejemplo, cuando distintas recepcionistas atienden en horas pico).

### Agregado

- Dos pruebas de regresión que cubren el caso de horario con espacios extra.

### Validación

- Las nueve pruebas automatizadas finalizaron correctamente.
- El cambio corresponde al tag `v1.0.1`, posterior a la línea base `v1.0`.

## [1.1.0] - 2026-07-31

### Agregado

- Prueba de rendimiento para la consulta de disponibilidad.
- Ejecución de 100 consultas para verificar el tiempo de respuesta.
- Validación de que al menos el 95 % de las consultas responde en un máximo de 2 segundos.

### Validación

- Las siete pruebas automatizadas finalizaron correctamente.
- El cambio fue realizado después de la línea base `v1.0`.

## [1.0.0] - 2026-07-31

### Agregado

- Estructura inicial del repositorio.
- Especificación de requisitos del sistema.
- Plan de Gestión de Configuración.
- Identificación de ocho Elementos de Configuración.
- Modelo de calidad basado en ISO/IEC 25010.
- Análisis del impacto del cambio durante el ciclo de desarrollo.
- Código para validar y registrar citas.
- Validación para evitar citas duplicadas.
- Función para cancelar citas.
- Seis pruebas automatizadas.
- Archivo de configuración de ejemplo.
- Archivo `.gitignore` para excluir archivos temporales de Python.

### Validación

- Las seis pruebas automatizadas finalizaron correctamente.
- El repositorio no contiene datos reales de pacientes ni credenciales.
- La versión está preparada para establecer la línea base `v1.0`.