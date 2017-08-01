import unittest
from unittest.mock import patch
from task_1 import check_word


class TasksTest(unittest.TestCase):

    @patch("task_1.input", side_effect=["Мужские Брюки", "Бельгия"])
    def test_check_word_to_right_work(self, input):
        self.assertEqual(check_word(), 'База производителей мужских брюк из Бельгии.')


if __name__ == "__main__":
    unittest.main()