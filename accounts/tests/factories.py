from django.contrib.auth import get_user_model

from factory import Faker, PostGenerationMethodCall
from factory.django import DjangoModelFactory


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")
    # This allows us to use the latest factory-boy package; but, for now, need
    # to hard-code the password.
    # See: https://github.com/FactoryBoy/factory_boy/issues/359
    password = PostGenerationMethodCall("set_password", "P@s5word")

    """
    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).generate(extra_kwargs={})
        )
        self.set_password(password)
        """

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
