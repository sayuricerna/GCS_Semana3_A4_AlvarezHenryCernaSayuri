# Sistema de Gestión de Citas Médicas del Consultorio MATER

## Descripción

Este repositorio contiene un paquete mínimo, auditable y trazable para el Sistema de Gestión de Citas Médicas del Consultorio MATER.

El proyecto se desarrolla como parte de la asignatura Gestión de la Configuración del Software y aplica la identificación de Elementos de Configuración, control de versiones, trazabilidad, calidad del software y análisis del ciclo de desarrollo.

El sistema propuesto busca facilitar el registro y control de citas médicas, verificar la disponibilidad de horarios y evitar que un mismo médico tenga dos citas programadas en la misma fecha y hora.

## Caso seleccionado

El caso seleccionado corresponde a un sistema de citas médicas para el Consultorio MATER.

El proceso general comprende:

1. Registro de los datos de la cita.
2. Validación de la información ingresada.
3. Verificación de la disponibilidad del horario.
4. Confirmación o rechazo de la cita.
5. Consulta de las citas programadas.

## Objetivo del proyecto

Construir un paquete mínimo de software que permita demostrar la relación entre los Elementos de Configuración, los atributos de calidad y las fases del ciclo de desarrollo, manteniendo evidencia verificable mediante Git y GitHub.

## Funcionalidades consideradas

- Validar los datos obligatorios de una cita.
- Verificar la disponibilidad de un horario.
- Evitar citas duplicadas para el mismo médico.
- Rechazar citas con datos incompletos.
- Mantener requisitos, código, pruebas y configuración bajo control de versiones.
- Registrar los cambios realizados durante el desarrollo.

## Estructura del repositorio

```text
GCS_Semana3_A4_AlvarezHenryCernaSayuri/
│
├── docs/
│   ├── SRS/
│   │   └── SRS_v1.md
│   ├── Quality/
│   │   └── Quality_Model.md
│   └── Lifecycle/
│       └── Lifecycle_Impact.md
│
├── src/
│   └── appointment_validation.py
│
├── tests/
│   └── test_appointment_validation.py
│
├── config/
│   └── config.example
│
├── CM_PLAN.md
├── CHANGELOG.md
└── README.md