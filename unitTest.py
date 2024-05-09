import unittest
from expense_tracker import ExpenseTracker

class TestExpenseTracker(unittest.TestCase):

    def setUp(self):
        self.tracker = ExpenseTracker()

    def test_add_expense(self):
        # Test adding expense to a category
        self.tracker.add_expense("Food", 50)
        self.assertEqual(self.tracker.expenses["Food"], [50])

        # Test adding multiple expenses to the same category
        self.tracker.add_expense("Food", 30)
        self.assertEqual(self.tracker.expenses["Food"], [50, 30])

        # Test adding expense to a new category
        self.tracker.add_expense("Transport", 20)
        self.assertEqual(self.tracker.expenses["Transport"], [20])

    def test_get_total_expenses(self):
        # Test total expenses calculation with multiple categories
        self.tracker.add_expense("Food", 50)
        self.tracker.add_expense("Food", 30)
        self.tracker.add_expense("Transport", 20)

        self.assertEqual(self.tracker.get_total_expenses(), 100)

        # Test total expenses calculation with no expenses
        self.assertEqual(self.tracker.get_total_expenses(), 0)

    def test_get_expenses_by_category(self):
        # Test getting expenses for an existing category
        self.tracker.add_expense("Food", 50)
        self.tracker.add_expense("Food", 30)
        self.tracker.add_expense("Transport", 20)

        self.assertEqual(self.tracker.get_expenses_by_category("Food"), [50, 30])
        self.assertEqual(self.tracker.get_expenses_by_category("Transport"), [20])

        # Test getting expenses for a non-existent category
        self.assertEqual(self.tracker.get_expenses_by_category("Entertainment"), [])

    def test_get_categories(self):
        # Test getting categories with expenses
        self.tracker.add_expense("Food", 50)
        self.tracker.add_expense("Transport", 20)

        self.assertEqual(self.tracker.get_categories(), ["Food", "Transport"])

        # Test getting categories with no expenses
        self.assertEqual(self.tracker.get_categories(), [])

    def test_get_category_total(self):
        # Test getting total expenses for an existing category
        self.tracker.add_expense("Food", 50)
        self.tracker.add_expense("Food", 30)
        self.tracker.add_expense("Transport", 20)

        self.assertEqual(self.tracker.get_category_total("Food"), 80)
        self.assertEqual(self.tracker.get_category_total("Transport"), 20)

        # Test getting total expenses for a non-existent category
        self.assertEqual(self.tracker.get_category_total("Entertainment"), 0)

if __name__ == '__main__':
    unittest.main()
