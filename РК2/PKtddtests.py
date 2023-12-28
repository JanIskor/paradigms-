import unittest
from РКmain import *


class TestRK2(unittest.TestCase):
    # Компьютеры
    deps = [
        Dep(1, 'MacBook Air'),
        Dep(2, 'MacBook Pro'),
        Dep(3, 'Xiaomi RedmiBook'),

        Dep(11, 'Asus ViviBook Pro'),
        Dep(22, 'Lenovo ThinkPad'),
        Dep(33, 'Honor 2020'),
    ]

    # Браузеры
    brausers = [
        Brauser(1, 'Google', 112.52, 11),
        Brauser(2, 'Opera', 21.1, 11),
        Brauser(3, 'Safari', 78.3, 33),
        Brauser(4, 'Yandex', 53.8, 33),
        Brauser(5, 'Firefox', 11.23, 2),
    ]

    def test_A1(self):
        one_to_many = [(e.name, e.market_share, d.model)
                       for d in deps
                       for e in brausers
                       if e.brause_id == d.id]
        self.assertEqual(a1_solution(one_to_many),
                         [('Google', 112.52, 'Asus ViviBook Pro'), ('Opera', 21.1, 'Asus ViviBook Pro'),
                          ('Safari', 78.3, 'Honor 2020'), ('Yandex', 53.8, 'Honor 2020'), ('Firefox', 11.23, 'MacBook Pro')]
)

    def test_A2(self):
        one_to_many = [(e.name, e.market_share, d.model)
                       for d in deps
                       for e in brausers
                       if e.brause_id == d.id]
        self.assertEqual(a2_solution(one_to_many),
                         [('Asus ViviBook Pro', 133.62), ('Honor 2020', 132.1), ('MacBook Pro', 11.23)])

    def test_A3(self):
        many_to_many_temp = [(d.model, ed.brause_id, ed.emp_id)
                         for d in deps
                         for ed in brausers_deps
                         if d.id == ed.brause_id]

        many_to_many = [(e.name, e.market_share, dep_name)
                        for dep_name, brause_id, emp_id in many_to_many_temp
                        for e in brausers if e.id == emp_id]
        self.assertEqual(a3_solution(many_to_many),
                         {'MacBook Air': ['Google', 'Opera', 'Safari'], 'MacBook Pro': ['Firefox']})


if __name__ == '__main__':
    unittest.main()
