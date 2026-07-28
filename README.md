# MATER - Sistema de Gestión de Citas Ginecológicas

## Descripción

MATER es un mini-sistema diseñado para apoyar la gestión de citas médicas
del consultorio ginecológico MATER. El proyecto permitirá representar el
registro de pacientes, la solicitud de citas, la validación de horarios,
la confirmación de la atención y la consulta del estado de las citas.

Este repositorio fue creado como parte de una práctica de Gestión de
Configuración de Software, calidad del software y ciclo de desarrollo.

## Objetivo

Construir un paquete mínimo, auditable y trazable para el sistema de citas
ginecológicas MATER, mediante el control de documentos, configuración,
código, pruebas y cambios utilizando Git y GitHub.

## Caso seleccionado

El caso seleccionado es un sistema de citas médicas para un consultorio
ginecológico.

El proceso principal es:

Registro de paciente → solicitud de cita → validación de horario →
confirmación de cita → atención o cancelación.

## Problema

La gestión manual de las citas puede provocar errores en los horarios,
duplicación de reservas, pérdida de información y dificultad para conocer
el estado de cada atención.

El sistema MATER busca representar un proceso organizado y controlado para
la administración de citas ginecológicas.

## Actores

- Paciente.
- Recepcionista.
- Médico ginecólogo.
- Administrador.

## Funciones principales

- Registrar pacientes.
- Consultar horarios disponibles.
- Solicitar una cita.
- Confirmar una cita.
- Cancelar una cita.
- Reprogramar una cita.
- Consultar el estado de una cita.
- Evitar citas duplicadas en el mismo horario.
- Consultar la agenda del consultorio.
- Registrar la atención de la paciente.

## Tipos de citas

- Consulta ginecológica general.
- Control prenatal.
- Papanicolaou.
- Ecografía ginecológica.
- Planificación familiar.

## Estados de una cita

- Pendiente.
- Confirmada.
- Atendida.
- Cancelada.
- No asistió.

## Estructura del repositorio

- `docs/SRS`: requisitos del sistema.
- `docs/Quality`: modelo y métricas de calidad.
- `docs/Lifecycle`: análisis del impacto de cambios.
- `src`: artefactos relacionados con la implementación.
- `tests`: artefactos relacionados con la validación.
- `config`: parámetros de configuración.
- `CM_PLAN.md`: Plan de Gestión de Configuración.
- `CHANGELOG.md`: historial de cambios.
- `README.md`: descripción general del proyecto.

## Gestión de Configuración

Los documentos y artefactos del proyecto se controlan mediante Git. Cada
cambio importante debe registrarse con un commit claro y relacionarse con
los requisitos, la calidad o la evidencia de validación.

La versión aprobada del proyecto será identificada mediante el tag `v1.0`,
que representará la línea base del sistema.

## Integrantes

- Henry Alvarez.
- Sayuri Cerna.

## Proyecto académico

Práctica aplicada: Elementos de Configuración, Calidad del Software y Ciclo
de Desarrollo con evidencia en Git.