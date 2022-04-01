from __future__ import annotations

from pathlib import Path

from composed_configuration import (
    ComposedConfiguration,
    ConfigMixin,
    DevelopmentBaseConfiguration,
    HerokuProductionBaseConfiguration,
    ProductionBaseConfiguration,
    TestingBaseConfiguration,
)


class DjangoLargeImageTestMixin(ConfigMixin):
    WSGI_APPLICATION = 'django_large_image_test.wsgi.application'
    ROOT_URLCONF = 'django_large_image_test.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    @staticmethod
    def mutate_configuration(configuration: ComposedConfiguration) -> None:
        # Install local apps first, to ensure any overridden resources are found first
        configuration.INSTALLED_APPS = [
            'django_large_image_test.core.apps.CoreConfig',
        ] + configuration.INSTALLED_APPS

        # Install additional apps
        configuration.INSTALLED_APPS += [
            's3_file_field',
        ]


class DevelopmentConfiguration(DjangoLargeImageTestMixin, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(DjangoLargeImageTestMixin, TestingBaseConfiguration):
    pass


class ProductionConfiguration(DjangoLargeImageTestMixin, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration(DjangoLargeImageTestMixin, HerokuProductionBaseConfiguration):
    pass
