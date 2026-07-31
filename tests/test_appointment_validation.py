"""Pruebas del sistema de citas ginecológicas MATER."""

import unittest
from time import perf_counter

from src.appointment_validation import (
    cancel_appointment,
    is_slot_available,
    register_appointment,
    validate_appointment_data,
)


class TestAppointmentValidation(unittest.TestCase):
    """Pruebas para validar y registrar citas."""

    def setUp(self):
        """Crea una cita existente antes de cada prueba."""
        self.existing_appointments = [
            {
                "patient_id": "P001",
                "patient_name": "María Pérez",
                "consultation_type": "Control prenatal",
                "appointment_date": "2026-08-10",
                "appointment_time": "09:00",
                "status": "Confirmada",
            }
        ]

    def test_complete_data_is_valid(self):
        """Comprueba que los datos completos sean aceptados."""
        result = validate_appointment_data(
            "P002",
            "Ana López",
            "Consulta general",
            "2026-08-10",
            "10:00",
        )

        self.assertTrue(result)

    def test_incomplete_data_is_invalid(self):
        """Comprueba que los datos incompletos sean rechazados."""
        result = validate_appointment_data(
            "",
            "Ana López",
            "Consulta general",
            "2026-08-10",
            "10:00",
        )

        self.assertFalse(result)

    def test_available_slot(self):
        """Comprueba que un horario diferente esté disponible."""
        result = is_slot_available(
            self.existing_appointments,
            "2026-08-10",
            "10:00",
        )

        self.assertTrue(result)

    def test_occupied_slot(self):
        """Comprueba que una cita activa duplicada sea rechazada."""
        result = is_slot_available(
            self.existing_appointments,
            "2026-08-10",
            "09:00",
        )

        self.assertFalse(result)

    def test_register_appointment(self):
        """Comprueba que una cita válida se registre como pendiente."""
        appointment = register_appointment(
            self.existing_appointments,
            "P002",
            "Ana López",
            "Consulta general",
            "2026-08-10",
            "10:00",
        )

        self.assertEqual(appointment["status"], "Pendiente")
        self.assertEqual(len(self.existing_appointments), 2)

    def test_cancel_appointment(self):
        """Comprueba que una cita pueda cambiar a cancelada."""
        appointment = self.existing_appointments[0]

        result = cancel_appointment(appointment)

        self.assertEqual(result["status"], "Cancelada")

    def test_availability_search_performance(self):
        """Verifica que el 95 % de 100 consultas responda en máximo 2 segundos."""
        successful_queries = 0
        total_queries = 100

        for _ in range(total_queries):
            start_time = perf_counter()

            is_slot_available(
                self.existing_appointments,
                "2026-08-10",
                "10:00",
            )

            elapsed_time = perf_counter() - start_time

            if elapsed_time <= 2:
                successful_queries += 1

        compliance_percentage = (
            successful_queries / total_queries
        ) * 100

        self.assertGreaterEqual(compliance_percentage, 95)
if __name__ == "__main__":
    unittest.main()