class CPFValidator:

    def __init__(self, cpf):
        self.cpf = cpf
        self.count_first_digit = 10
        self.count_second_digit = 11
        self.first_validation = []
        self.second_validation = []

    def convert_cpf_to_strings(self):
        self.cpf = list(self.cpf)
        try:
            for i in range(0, len(self.cpf)):
                self.cpf[i] = int(self.cpf[i])
        except ValueError:
            print("Cpf with caracher invalid")
        print(self.cpf)

    def validate_first_digit_cpf(self):
        self.first_digit_verificator = self.cpf[-2]
        self.cpf_first_nine_digits = self.cpf[:9]
        for i in self.cpf_first_nine_digits:
            self.first_validation.append(self.count_first_digit * i)
            self.count_first_digit -= 1
        result = sum(self.first_validation) % 11
        if result < 2:
            self.first_digit_verificator = 0
        else:
            self.first_digit_verificator = 11 - result
        print(self.first_digit_verificator)

    def validate_second_digit_cpf(self):
        self.second_digit_verificator = self.cpf[len(self.cpf) - 1]
        self.cpf_ten_digits = self.cpf[:10]
        for i in self.cpf_ten_digits:
            self.second_validation.append(self.count_second_digit * i)
            self.count_second_digit -= 1
        result = sum(self.second_validation) % 11

        if result <= 2:
            self.second_digit_verificator = 0
        else:
            self.second_digit_verificator = 11 - result
        print(self.second_digit_verificator)


cpf = CPFValidator()
print(cpf. convert_cpf_to_strings())
print(cpf.validate_first_digit_cpf())
print(cpf.validate_second_digit_cpf())
