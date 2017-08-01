import unittest
from unittest.mock import patch
from task_1 import check_word
from task_2 import dice


class TasksTest(unittest.TestCase):

    @patch("task_1.input", side_effect=["Мужские Брюки", "Бельгия"])
    def test_check_word_to_right_work(self, input):
        self.assertEqual(check_word(), 'База производителей мужских брюк из Бельгии.')

    @patch("task_2.input", return_value="dices.txt")
    def test_dice_func_to_right_work(self, input):
        self.assertEqual(dice(), "Результат: 4")


if __name__ == "__main__":
    unittest.main()