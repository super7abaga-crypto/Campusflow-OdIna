import unittest

from campusflow.reports import format_report, format_ticket, summarize_tickets


class ReportTests(unittest.TestCase):
    def setUp(self):
        self.tickets = [
            {"id": "T001", "title": "Wi-Fi", "category": "Network", "urgency": "high", "affected_users": 12, "priority": "critical", "status": "open", "assigned_to": None},
            {"id": "T002", "title": "Mouse", "category": "Hardware", "urgency": "low", "affected_users": 1, "priority": "low", "status": "resolved", "assigned_to": "Ada"},
        ]

    def test_summary_counts_groups_and_unassigned(self):
        report = summarize_tickets(self.tickets)
        self.assertEqual(report["total"], 2)
        self.assertEqual(report["by_status"], {"open": 1, "resolved": 1})
        self.assertEqual(report["by_priority"], {"critical": 1, "low": 1})
        self.assertEqual(report["by_category"], {"Network": 1, "Hardware": 1})
        self.assertEqual(report["unassigned"], 1)

    def test_format_ticket_includes_core_details(self):
        line = format_ticket(self.tickets[0])
        self.assertIn("T001", line)
        self.assertIn("Wi-Fi", line)
        self.assertIn("critical", line)
        self.assertIn("Unassigned", line)

    def test_format_report_includes_total_and_unassigned(self):
        report = format_report(self.tickets)
        self.assertIn("2 total ticket(s)", report)
        self.assertIn("Unassigned tickets: 1", report)

    def test_empty_report_is_readable(self):
        report = format_report([])
        self.assertIn("0 total ticket(s)", report)
        self.assertIn("None", report)


if __name__ == "__main__":
    unittest.main()
