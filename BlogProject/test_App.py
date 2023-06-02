class Test_App():
    def test_addition(self):
        num1 = 5
        num2 = 10
        assert num1 + num2 == 15


    def test_uppercase(self):
        assert "loud noises".upper() == "LOUD NOISES"

    def test_reversed(self):
        assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

    def test_some_primes(self):
        assert 37 in {
            num
            for num in range(2, 50)
            if not any(num % div == 0 for div in range(2, num))
        }