import unittest

from campusflow.tickets import calculate_priority, create_ticket


class TestTicketPriority(unittest.TestCase):

    def test_critical_priority(self):
        self.assertEqual(calculate_priority("high", 10), "critical")

    def test_high_urgency_with_few_users(self):
        self.assertEqual(calculate_priority("high", 1), "high")

    def test_high_priority_from_affected_users(self):
        self.assertEqual(calculate_priority("low", 10), "high")

    def test_medium_urgency(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_medium_priority_from_affected_users(self):
        self.assertEqual(calculate_priority("low", 3), "medium")

    def test_low_priority(self):
        self.assertEqual(calculate_priority("low", 2), "low")


class TestTicketCreation(unittest.TestCase):

    def test_create_first_ticket(self):
        tickets = []

        ticket = create_ticket(
            tickets,
            "Campus Wi-Fi is down",
            "Network",
            "high",
            15,
        )

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])
        self.assertEqual(len(tickets), 1)

    def test_ticket_ids_are_unique(self):
        tickets = []

        first = create_ticket(
            tickets, "Wi-Fi is down", "Network", "high", 10
        )

        second = create_ticket(
            tickets, "Laptop is broken", "Hardware", "low", 1
        )

        self.assertEqual(first["id"], "T001")
        self.assertEqual(second["id"], "T002")

    def test_category_is_normalized(self):
        tickets = []

        ticket = create_ticket(
            tickets, "Wi-Fi is down", "nETWORK", "HIGH", 10
        )

        self.assertEqual(ticket["category"], "Network")
        self.assertEqual(ticket["urgency"], "high")

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket([], "   ", "Network", "high", 10)

    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket([], "Broken laptop", "Cooking", "low", 1)

    def test_invalid_urgency_is_rejected(self):
        with self.assertRaises(ValueError):
            create_ticket([], "Broken laptop", "Hardware", "extreme", 1)

    def test_invalid_affected_users_is_rejected(self):
        for value in (0, -1, 2.5, "ten"):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    create_ticket(
                        [], "Broken laptop", "Hardware", "low", value
                    )
    def test_invalid_input_does_not_create_ticket(self):
        tickets = []

        with self.assertRaises(ValueError):
            create_ticket(
                tickets,
                "Broken laptop",
                "Cooking",
                "low",
                1,
            )

        self.assertEqual(tickets, [])

    def test_id_uses_highest_existing_number(self):
        tickets = [
            {"id": "T001"},
            {"id": "T003"},
        ]

        ticket = create_ticket(
            tickets,
            "New laptop problem",
            "Hardware",
            "low",
            1,
        )

        self.assertEqual(ticket["id"], "T004")


if __name__ == "__main__":
    unittest.main()