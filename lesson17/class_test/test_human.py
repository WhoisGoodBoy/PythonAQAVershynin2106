from lesson17.code_for_testing import Human
class TestHuman:
    def setup_class(self):
        print('it`s teardown class')
    def setup(self):
        self.human = Human('Alfred',78,'grey')
        print('setup for each test')
    def test_check_age(self):
        self.human.grow()
        assert self.human.age == 79

    def test_hair_color_change(self):
        self.human.change_color('black')
        assert self.human.color == 'black'

    def test_hair_color_change2(self):
        self.human.change_color('pink')
        assert self.human.color == 'black'
    def teardown(self):
        print('teardown for each test')

    def teardown_class(self):
        print('it`s teardown class')