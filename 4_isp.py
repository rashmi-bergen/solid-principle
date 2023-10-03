"""
Interface Segregation Principle
Interfaces should be granularly split and be as small as possible
Basically the principle states that a class should not be forced to implement functions that it does not use.
"""
from abc import ABC, abstractmethod


class MobileDevice(ABC):
    @abstractmethod
    def voice(self):
        pass

    @abstractmethod
    def text(self):
        pass

    @abstractmethod
    def camera(self):
        pass


class BestMobileDeviceEver(MobileDevice):
    def voice(self):
        # voide implementation
        pass

    def text(self):
        # text implemenation
        pass

    def camera(self):
        # camera implementation
        pass


class OldSchollMobileDevice(MobileDevice):
    def voice(self):
        # voide implementation
        pass

    def text(self):
        # text implemenation
        pass

    def camera(self):
        raise NotImplementedError


#####################################################
# After isp


class Phone(ABC):
    @abstractmethod
    def voice(self):
        pass


class Text(ABC):
    @abstractmethod
    def text_message(self):
        pass


class Camera(ABC):
    @abstractmethod
    def photo(self):
        pass


class BestMobileDeviceEver(Phone, Text, Camera):
    def voice(self):
        # voide implementation
        pass

    def text_message(self):
        # text implemenation
        pass

    def photo(self):
        # camera implementation
        pass


class OldSchollMobileDevice(Phone, Text):
    def voice(self):
        # voide implementation
        pass

    def text_message(self):
        # text implemenation
        pass
