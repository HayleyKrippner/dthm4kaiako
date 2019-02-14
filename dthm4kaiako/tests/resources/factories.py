"""Module for factories for tesing resources application."""

import random
from factory import DjangoModelFactory, Faker, post_generation
from factory.faker import faker
from resources.models import (
    Resource,
    ResourceComponent,
)


class ResourceFactory(DjangoModelFactory):
    """Factory for generating resources."""

    name = Faker('sentence')
    description = Faker('paragraph', nb_sentences=5)

    class Meta:
        """Metadata for class."""

        model = Resource

    @post_generation
    def create_components(self, create, extracted, **kwargs):
        """Create components for resource."""
        FAKER = faker.Faker()
        number_of_components = random.randint(1, 9)
        for i in range(number_of_components):

            component_name = FAKER.sentence()
            component_type = random.choice(list(ResourceComponent.COMPONENT_TYPE_DATA))
            resource_count = Resource.objects.count()

            if component_type == ResourceComponent.TYPE_RESOURCE and resource_count >= 2:
                resources = list(Resource.objects.exclude(pk=self.pk))
                resource_component = resources[random.randint(0, len(resources) - 1)]
                ResourceComponent.objects.create(
                    name=resource_component.name,
                    resource=self,
                    component_resource=resource_component,
                )
            # TODO: Implement all types of components
            else:  # Website
                ResourceComponent.objects.create(
                    name=component_name,
                    resource=self,
                    component_url=FAKER.url(),
                )
