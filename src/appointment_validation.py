"""Funciones básicas del sistema de citas ginecológicas MATER."""


ACTIVE_STATUSES = {"Pendiente", "Confirmada"}


def _normalize(value):
    """Normaliza texto para comparaciones (quita espacios al inicio/fin).

    CR-004-SEM4-ALVAREZ-CERNA: en horas pico, distintas recepcionistas podian
    registrar la misma cita con espacios adicionales en la fecha u hora
    (por ejemplo, " 09:00 " en lugar de "09:00"). Como la comparacion era
    con igualdad exacta de texto, el sistema no detectaba que era el mismo
    horario y permitia una cita duplicada.
    """
    return value.strip() if isinstance(value, str) else value


def validate_appointment_data(
    patient_id,
    patient_name,
    consultation_type,
    appointment_date,
    appointment_time,
):
    """Comprueba que todos los datos obligatorios estén completos."""
    required_data = [
        patient_id,
        patient_name,
        consultation_type,
        appointment_date,
        appointment_time,
    ]

    return all(
        isinstance(value, str) and value.strip()
        for value in required_data
    )


def is_slot_available(
    existing_appointments,
    appointment_date,
    appointment_time,
):
    """Verifica que no exista otra cita activa en la misma fecha y hora."""
    normalized_date = _normalize(appointment_date)
    normalized_time = _normalize(appointment_time)

    for appointment in existing_appointments:
        same_date = _normalize(appointment["appointment_date"]) == normalized_date
        same_time = _normalize(appointment["appointment_time"]) == normalized_time
        active_appointment = appointment["status"] in ACTIVE_STATUSES

        if same_date and same_time and active_appointment:
            return False

    return True


def register_appointment(
    existing_appointments,
    patient_id,
    patient_name,
    consultation_type,
    appointment_date,
    appointment_time,
):
    """Registra una cita nueva cuando los datos y el horario son válidos."""
    if not validate_appointment_data(
        patient_id,
        patient_name,
        consultation_type,
        appointment_date,
        appointment_time,
    ):
        raise ValueError("Todos los datos obligatorios deben estar completos.")

    if not is_slot_available(
        existing_appointments,
        appointment_date,
        appointment_time,
    ):
        raise ValueError("El horario seleccionado ya está ocupado.")

    new_appointment = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "consultation_type": consultation_type,
        "appointment_date": _normalize(appointment_date),
        "appointment_time": _normalize(appointment_time),
        "status": "Pendiente",
    }

    existing_appointments.append(new_appointment)
    return new_appointment


def cancel_appointment(appointment):
    """Cambia el estado de una cita a Cancelada."""
    appointment["status"] = "Cancelada"
    return appointment