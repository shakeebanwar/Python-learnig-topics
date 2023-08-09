"""
Dependency Injection:
Ab aap MessageSender class ko create karte waqt MessageService object ko constructor ke through inject karte hain. Yani aap dependencies ko class ke bahar se provide kar rahe hain
"""

print("Injection Example............")

class MessageService:
    def send_message(self, message):
        print(f"Sending message: {message}")

class MessageSender:
    def __init__(self, message_service):
        self.message_service = message_service
    
    def send(self, message):
        self.message_service.send_message(message)

# Create a MessageService instance
service = MessageService()

# Inject the MessageService into MessageSender using Dependency Injection
sender = MessageSender(message_service=service)

# Send a message
sender.send("Hello, how are you?")


print("Inversion Example............")

"""
Dependency Inversion Principle:
Ab aap Dependency Inversion Principle ka istemal karte hain. Aap ek abstract interface MessageServiceProvider create karte hain jisse dono high-level aur low-level components use kar sakte hain. Phir aap MessageService class ko implement karke MessageServiceProvider interface ke sath bind karte hain.
"""


class MessageServiceProvider:
    def send_message(self, message):
        pass

class MessageService(MessageServiceProvider):
    def send_message(self, message):
        print(f"Sending message: {message}")

class MessageSender:
    def __init__(self, message_service_provider):
        self.message_service_provider = message_service_provider
    
    def send(self, message):
        self.message_service_provider.send_message(message)

# Using Dependency Inversion to inject the message service provider
service = MessageService()
sender = MessageSender(message_service_provider=service)

sender.send("Hello, how are you?")
