"""
Dependency Inversion Principle
The Dependency Inversion Principle (DIP) is one of the SOLID principles of object-oriented design. 
It states that high-level modules should not depend on low-level modules, but both should depend on abstractions. 
In Python, we can implement the Dependency Inversion Principle using interfaces or abstract classes to define the abstractions 
that high-level and low-level modules depend on.
"""
from abc import ABC, abstractmethod

# Abstraction (abstract class or interface)
class MessageSender(ABC):
    @abstractmethod
    def send_message(self, message: str):
        pass

# Low-level module
class EmailSender(MessageSender):
    def send_message(self, message: str):
        print(f"Sending email: {message}")

# Another low-level module
class SMSSender(MessageSender):
    def send_message(self, message: str):
        print(f"Sending SMS: {message}")

# High-level module depending on abstraction
class NotificationService:
    def __init__(self, message_sender: MessageSender):
        self.message_sender = message_sender

    def send_notification(self, message: str):
        self.message_sender.send_message(message)

# Example usage
if __name__ == "__main__":
    email_sender = EmailSender()
    sms_sender = SMSSender()

    email_notification = NotificationService(email_sender)
    sms_notification = NotificationService(sms_sender)

    email_notification.send_notification("Hello via email")
    sms_notification.send_notification("Hello via SMS")
