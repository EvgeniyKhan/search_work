class Vacancy:
    def __init__(self, title, link, salary):
        self.title = title
        self.link = link
        self.salary = salary
        self.checks_salary()

    def checks_salary(self):
        if self.salary and isinstance(self.salary, dict):
            salary_from = self.salary.get("from")
            salary_to = self.salary.get("to")
            self.salary["from"] = salary_from if salary_from else 0
            self.salary["to"] = salary_to if salary_to else 0
        else:
            self.salary = {
                "from": 0,
                "to": 0
            }

    def __str__(self):
        return f"\ntitle - {self.title}\nsalary - {self.salary}\n"
