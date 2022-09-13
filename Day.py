

class Day:
    TESTS = []
    def __init__(self):
        pass



    def parse(self, data):
        return

    def add_test(self, test):
        ret = self.parse(test)

        self.TESTS.append(ret)

    def run1_tests(self):

        for tnum, res in enumerate(self.TESTS, start=1):
            print(f"{tnum}. {res} RESULT: {self.run1(res)}")

    def run2_tests(self):

        for tnum, res in enumerate(self.TESTS, start=1):
            print(f"{tnum}. {res} RESULT: {self.run2(res)}")


    def run1(self, parsed, test=False):
        ans = 0

        return ans

    def run2(self, parsed, test=False):
        ans = 0


        return ans