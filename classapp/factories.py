import factory
from .models import TodoClass
from django.contrib.auth.models import User


class TodoFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = TodoClass
        
        todo = factory.Faker('sentence', nb_words=3)

class UserFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = User
        
        username = factory.sequence(lambda n:f"user{n}")
        password = factory.PostGenerationMethodCall('set_password','password')
        email = factory.LazyAttribute(lambda obj:f"{obj.username}@example.com")