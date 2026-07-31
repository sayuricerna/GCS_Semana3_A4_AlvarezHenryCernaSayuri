"""Funciones básicas del sistema de citas ginecológicas MATER."""


ACTIVE_STATUSES = {"Pendiente", "Confirmada"}


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
    for appointment in existing_appointments:
        same_date = appointment["appointment_date"] == appointment_date
        same_time = appointment["appointment_time"] == appointment_time
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
        "appointment_date": appointment_date,
        "appointment_time": appointment_time,
        "status": "Pendiente",
    }

    existing_appointments.append(new_appointment)
    return new_appointment


def cancel_appointment(appointment):
    """Cambia el estado de una cita a Cancelada."""
    appointment["status"] = "Cancelada"
    return appointment