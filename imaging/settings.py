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


class ImagingMixin(ConfigMixin):
    WSGI_APPLICATION = 'imaging.wsgi.application'
    ROOT_URLCONF = 'imaging.urls'

    BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

    @staticmethod
    def mutate_configuration(configuration: ComposedConfiguration) -> None:
        # Install local apps first, to ensure any overridden resources are found first
        configuration.INSTALLED_APPS = [
            'imaging.core.apps.CoreConfig',
        ] + configuration.INSTALLED_APPS

        # Install additional apps
        configuration.INSTALLED_APPS += [
            's3_file_field',
            'django_large_image',
        ]


class DevelopmentConfiguration(ImagingMixin, DevelopmentBaseConfiguration):
    pass


class TestingConfiguration(ImagingMixin, TestingBaseConfiguration):
    pass


class ProductionConfiguration(ImagingMixin, ProductionBaseConfiguration):
    pass


class HerokuProductionConfiguration(ImagingMixin, HerokuProductionBaseConfiguration):
    pass
