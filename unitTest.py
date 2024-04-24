import unittest
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        self.tracker.add_expense("Food", 20.50)
        self.tracker.add_expense("Food", 15.75)
        self.tracker.add_expense("Transportation", 30.25)

        self.assertEqual(self.tracker.expenses["Food"], [20.50, 15.75])
        self.assertEqual(self.tracker.expenses["Transportation"], [30.25])

    def test_get_total_expenses(self):
        self.tracker.add_expense("Food", 20.50)
        self.tracker.add_expense("Food", 15.75)
        self.tracker.add_expense("Transportation", 30.25)

        total_expenses = self.tracker.get_total_expenses()
        self.assertEqual(total_expenses, 66.50)

    def test_get_expenses_by_category(self):
        self.tracker.add_expense("Food", 20.50)
        self.tracker.add_expense("Food", 15.75)
        self.tracker.add_expense("Transportation", 30.25)

        food_expenses = self.tracker.get_expenses_by_category("Food")
        self.assertEqual(food_expenses, [20.50, 15.75])

        transportation_expenses = self.tracker.get_expenses_by_category("Transportation")
        self.assertEqual(transportation_expenses, [30.25])

if __name__ == "__main__":
    unittest.main()