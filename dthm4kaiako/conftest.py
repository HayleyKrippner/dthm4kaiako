"""Module for configuring pytest."""

import pytest
from django.conf import settings
from django.test import RequestFactory

from users.models import User
from tests.users.factories import UserFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    """Pytest setup for media storage."""
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user() -> User:
    """Pytest setup for user model."""
    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    """Pytest setup for factory."""
    return RequestFactory()
