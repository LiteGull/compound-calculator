class SimpleInterest(object):
    def __init__(self, principle, rate):
        self.principle = principle
        self.rate = float(rate / 100)

    def calculate_interest(self):
        return self.principle * self.rate

    def calculate_total_repayment(self):
        return self.calculate_interest() + self.principle


class CompoundInterest(object):
    def __init__(self, time, principle, rate):
        self.time = time
        self.principle = principle
        self.rate = rate
        self.interest = principle

    def calculate_term_total_repayment(self):
        for n in range(self.time):
            si = SimpleInterest(self.interest, self.rate)
            self.interest = si.calculate_total_repayment()
            print(f"Year {n+1}: £{round(self.interest, 2):.2f}")
        print("\n")
        return round(self.interest, 2)


def simple_interest():
    si = SimpleInterest(principle=1000, rate=10)
    return round(si.calculate_total_repayment(), 2)


def compound_interest():
    principle, rate, time = user_input()
    m = f"\nCalculations for compound interest on £{principle} with interest at a rate of {rate}% over {time} year(s)\n"
    print(m)
    ci = CompoundInterest(time=time, principle=principle, rate=rate)
    return ci.calculate_term_total_repayment()


def user_input():
    time = int(input("Please enter calculation period: ") or 1)
    principle = int(input("Please enter principle £: ") or 1000)
    rate = int(input("Please enter interest rate %: ") or 10)
    return principle, rate, time


def interest_calculator():
    principle, rate, time = user_input()
    return round(float(principle * float(1 + rate / 100) ** time), 2)


if __name__ == "__main__":
    simple_interest()
    compound_interest()
