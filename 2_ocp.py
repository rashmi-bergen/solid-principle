"""
Open Closed Principle

A class/function should be open for extension, and closed for modification
"""

# Before ocp


class Company:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Company name {self.name}"


class CompanyStorage:
    def save_to_database(self, company):
        print(f"Save the {company} to database")

    def save_to_json(self, company):
        print(f"Save the {company} to a JSON file")


company = Company("ABC")
storage = CompanyStorage()
storage.save_to_database(company)


"""
In the above example, the CompanyStorage class has two methods:

The save_to_database() method saves a company to the database.
The save_to_json() method saves a company to a JSON file.
Later, if you want to save the Company's object into an XML file, you must modify the CompanyStorage class.
It means that the CompanyStorage class is not open for extension but modification. Hence, it violates the open-closed principle.
"""

################################################################################
# After ocp

from abc import ABC, abstractmethod


class Company:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f"Company name {self.name}"


class CompanyStorage(ABC):
    @abstractmethod
    def save(self, company):
        pass


class CompanyDB(CompanyStorage):
    def save(self, company):
        print(f"Save the {company} to DB")


class CompanyJSON(CompanyStorage):
    def save(self, company):
        print(f"Save the {company} to json")


class CompanyXML(CompanyStorage):
    def save(self, company):
        print(f"Save the {company} to xml")


company = Company("ABC")
storage = CompanyXML()
storage.save(company)
