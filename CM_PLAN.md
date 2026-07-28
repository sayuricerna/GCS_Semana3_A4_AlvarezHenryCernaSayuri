
---

# 2. `CM_PLAN.md`

Este es el documento principal de los **Elementos de Configuración**.

```md
# Plan de Gestión de Configuración

## 1. Información general

**Proyecto:** Sistema de Gestión de Citas Médicas del Consultorio MATER  
**Versión:** 1.0  
**Estado:** Aprobado para línea base  
**Repositorio:** GitHub  
**Equipo responsable:** Henry Alvarez y Sayuri Cerna  

## 2. Propósito

El presente Plan de Gestión de Configuración establece los Elementos de Configuración que deben ser identificados, versionados y controlados durante el desarrollo del sistema de citas médicas del Consultorio MATER.

El control de estos elementos permite mantener la integridad del proyecto, registrar los cambios realizados y conservar evidencia verificable de los requisitos, código, pruebas y criterios de calidad.

## 3. Elementos de Configuración

| ID | EC | Ubicación | ¿Por qué es un EC? | Quién lo modifica |
|---|---|---|---|---|
| EC-01 | `SRS_v1.md` | `/docs/SRS/` | Define los requisitos del sistema; cualquier cambio modifica el alcance, el código y las pruebas. | Analista / Product Owner |
| EC-02 | `Quality_Model.md` | `/docs/Quality/` | Establece los atributos y métricas verificables para evaluar la calidad del sistema. | Analista de calidad / QA |
| EC-03 | `Lifecycle_Impact.md` | `/docs/Lifecycle/` | Documenta cómo un cambio afecta las diferentes fases del ciclo de desarrollo. | Líder del proyecto |
| EC-04 | `appointment_validation.py` | `/src/` | Contiene la lógica para validar citas y verificar la disponibilidad de horarios. | Desarrollador |
| EC-05 | `test_appointment_validation.py` | `/tests/` | Valida el comportamiento del código y permite detectar errores o regresiones. | QA / Desarrollador |
| EC-06 | `config.example` | `/config/` | Define parámetros que afectan el funcionamiento del sistema sin exponer datos sensibles. | DevOps / Desarrollador |
| EC-07 | `CM_PLAN.md` | `/` | Identifica los EC, sus responsables, ubicación y reglas para controlar cambios. | Líder del proyecto |
| EC-08 | `CHANGELOG.md` | `/` | Registra las versiones y modificaciones realizadas durante la evolución del proyecto. | Equipo de desarrollo |

## 4. Identificación y versionado

Cada Elemento de Configuración debe:

1. Tener un identificador único.
2. Estar almacenado dentro del repositorio.
3. Tener un responsable asignado.
4. Contar con historial de versiones.
5. Relacionarse con un requisito, una métrica de calidad o una evidencia.
6. Ser incluido en un commit con un mensaje descriptivo.

## 5. Reglas para controlar cambios

- Todo cambio debe registrarse mediante un commit.
- Los mensajes de commit deben explicar claramente la modificación.
- Los cambios en requisitos deben reflejarse en código y pruebas cuando corresponda.
- No se deben subir contraseñas, tokens o credenciales reales.
- Antes de aprobar una versión deben revisarse los EC relacionados.
- Los cambios posteriores a la línea base deben quedar registrados en `CHANGELOG.md`.
- La versión inicial aprobada se identificará mediante el tag `v1.0`.

## 6. Convención de commits

Se utilizarán los siguientes prefijos:

| Prefijo | Uso |
|---|---|
| `chore:` | Creación de estructura o tareas generales |
| `docs:` | Creación o actualización de documentación |
| `feat:` | Implementación de una funcionalidad |
| `test:` | Creación o actualización de pruebas |
| `fix:` | Corrección de un error |
| `config:` | Cambios en parámetros de configuración |

## 7. Línea base

La línea base `v1.0` representa la versión aprobada de los requisitos, código, pruebas, configuración, modelo de calidad y análisis del ciclo de desarrollo.

Después de establecer la línea base, cualquier modificación deberá quedar registrada mediante un nuevo commit y una actualización del historial de cambios.

## 8. Trazabilidad básica

| Requisito | Código relacionado | Prueba relacionada | Evidencia |
|---|---|---|---|
| RF-001 Validar datos de la cita | `appointment_validation.py` | `test_valid_appointment` | Resultado de la prueba |
| RF-002 Rechazar datos incompletos | `appointment_validation.py` | `test_appointment_with_missing_data` | Resultado de la prueba |
| RF-003 Verificar disponibilidad | `appointment_validation.py` | `test_available_slot` | Resultado de la prueba |
| RF-004 Evitar citas duplicadas | `appointment_validation.py` | `test_occupied_slot` | Resultado de la prueba |