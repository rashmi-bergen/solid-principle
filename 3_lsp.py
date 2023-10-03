"""
Liskov Substitution Principle
A derived class can assume the place of its super class, and everything should work.
"""


class KitchenAppliace:
    def on():
        pass

    def off():
        pass

    def set_temperature():
        pass


class Toaster(KitchenAppliace):
    def on():
        print("ON")

    def off():
        print("OFF")

    def set_temperature():
        print("Set temperature")


class Juicer(KitchenAppliace):
    def on():
        print("ON")

    def off():
        print("OFF")


# Juicer breaks lsp since it does not need set_temperature() to be implemented

#################################################################################3

# After lsp


class KitchenAppliace:
    def on():
        pass

    def off():
        pass


class KitheApplianceWithTemp(KitchenAppliace):
    def set_temperature():
        pass


class Toaster(KitheApplianceWithTemp):
    def on():
        print("ON")

    def off():
        print("OFF")

    def set_temperature():
        print("Set temperature")


class Juicer(KitchenAppliace):
    def on():
        print("ON")

    def off():
        print("OFF")
