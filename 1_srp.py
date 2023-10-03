"""
Single Resposibility Principle.

A class should have ONE responsibility

The single responsibility principle is a software design guideline which states that every module, 
class or function in your code should have only one responsibility and only one reason to change.

It helps to transform a large block of code into well-defined, well-labelled, high cohesive, clean and robust components.
Small and well-defined code blocks can be mixed and re-used better.
"""

from dataclasses import dataclass, field

# Before the single responsibility principle


@dataclass
class Company:
    company: dict = field(default_factory=dict)
    number = 0

    def add_company(self, company):
        self.number += 1
        self.company[self.number] = company

    def __str__(self):
        return str(self.company)

    def save(self, filename):
        with open(filename, "w") as f:
            f.write(str(self.company))


# The above example breaks the spr since storing info to a file has nothing to do with Company class

#######################################################################################
# After the single responsibility principle

company = Company()
company.add_company("Company A")
company.add_company("Company B")
print(f"Companies: {company}")
company.save("test1.txt")


@dataclass
class Company:
    company: dict = field(default_factory=dict)
    number = 0

    def add_company(self, company):
        self.number += 1
        self.company[self.number] = company

    def __str__(self):
        return str(self.company)


class DataService:
    @staticmethod
    def save(filename, my_object):
        with open(filename, "w") as f:
            f.write(str(my_object))


company = Company()
company.add_company("Company A")
company.add_company("Company B")
print(f"Companies: {company}")
DataService.save("test2.txt", company)


# More examples

# Before the single responsibility principle
class Model:
    def pre_process(self):
        pass

    def train(self):
        pass

    def evaluate(self):
        pass

    def predict(self):
        pass


# After the single responsibility principle applied
class PreProcess:
    pass


class Train:
    pass


class Evaluate:
    pass


class Predict:
    pass


# Before the single responsibility principle applied
def pre_processing_data():
    # importing data
    # converting data types
    # handling missing values
    # handling outliers
    # transforming data
    pass


# After the single responsibility principle applied
def import_data():
    pass


def convert_data_type():
    pass


def handle_missing_values():
    pass


def handle_outliers():
    pass


def transform_data():
    pass
