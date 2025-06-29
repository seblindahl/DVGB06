from bank_central import BankCentral

class TestBank:
    def __init__(self):
        self.bank = BankCentral()
        self.test_counter = 1

    def run_tests(self):#fler test kommer, bla utskrift
        self.test_get_all_customers(expected = [])

        self.test_create_customer("Bengt", "Karlsson", "8110102424", expected = True)

        self.test_create_customer("Bengt", "Karlsson", "8110102424", expected = False)

    def test_get_all_customers (self, expected):
        result = self.bank.get_all_customers()
        self._print_result("get_all_customers()", result, expected)

    def test_create_customer(self, name, surname, p_no, expected):
        result = self.bank.create_customer(name, surname, p_no)
        self._print_result(f"create_customer({name}, {surname}, {p_no})", result, expected)

    def _print_result(self, description, result, expected):
        if result == expected:
            print(f"Test {self.test_counter}: PASS - {description}")
        else:
            print(f"Test {self.test_counter}: FAIL - {description}")
            print(f"  Expected: {expected}")
            print(f"  Got     : {result}")
        self.test_counter += 1

if __name__ == "__main__":
    tester = TestBank()
    tester.run_tests()