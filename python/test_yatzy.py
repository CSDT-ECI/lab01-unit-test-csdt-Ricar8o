from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_demo():
        expected = 15
        actual = 15
        assert expected == actual        

def test_chance_category_assertion():
        dices = [5,6,1,1,2]
        result = Yatzy.chance(*dices)
        assert result == 15

def test_yatzy_category_should_return_50():
        dices = [1,1,1,1,1]
        result = Yatzy.yatzy(dices)
        assert result == 50
def test_yatzy_category_should_return_zero():
        dices = [2,2,2,2,6]
        result = Yatzy.yatzy(dices)
        assert result == 0
def test_ones_category_should_sum():
        dices = [1,6,5,3,1]
        result = Yatzy.ones(*dices)
        assert result == 2

def test_ones_category_should_return_zero():
        dices = [3,6,5,3,2]
        result = Yatzy.ones(*dices)
        assert result == 0
     
def test_twos_category_should_sum():
        dices = [2,2,3,2,5]
        result = Yatzy.twos(*dices)
        assert result == 6

def test_twos_category_should_return_zero():
        dices = [1,3,3,6,5]
        result = Yatzy.twos(*dices)
        assert result == 0

def test_threes_category_should_sum():
        dices = [3,3,3,3,3]
        result = Yatzy.threes(*dices)
        assert result == 15

def test_threes_category_should_return_zero():
        dices = [1,1,5,6,2]
        result = Yatzy.threes(*dices)
        assert result == 0

def test_fours_category_should_return_zero():
        dices = [1,1,5,6,2]
        yatzy = Yatzy(*dices)
        result = yatzy.fours()
        assert result == 0

def test_fours_category_should_sum():
        dices = [4,4,4,4,4]
        yatzy = Yatzy(*dices)
        result = yatzy.fours()
        assert result == 20

def test_crazy_change_should_sum_evens():
        dices = [2,4,6,2,2]
        result = Yatzy.crazyChange(*dices)
        assert result == 48

def test_crazy_change_should_sum_odds():
        dices = [1,1,3,5,5]
        result = Yatzy.crazyChange(*dices)
        assert result == 30

def test_crazy_change_should_sum_evens_and_odds():
        dices = [2,4,3,5,6]
        result = Yatzy.crazyChange(*dices)
        assert result == 52
