from faker import Faker
fake = Faker()


class GeneratePayload:
    @staticmethod
    def generate_user_payload():
        email = fake.email()
        password = fake.password()
        name = fake.name()
        payload = {
            "email": email,
            "password": password,
            "name": name
        }
        return payload

class GenerateData:
    FAKE_EMAIL = fake.email()
    FAKE_NAME = fake.name()