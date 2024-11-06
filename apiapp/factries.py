import factory
from .models import Item

class ItemFactory(factory.django.DjangoModelFactory):
        class Meta:
            model = Item
        
        name = factory.Faker('sentence', nb_words=3)
        createdOn = factory.Faker('date')