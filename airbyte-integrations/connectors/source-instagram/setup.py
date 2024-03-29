#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk",
    "cached_property~=1.5",
    "facebook_business~=18.0.5",
]

TEST_REQUIREMENTS = [
    "requests-mock~=1.9.3",
    "pytest~=6.1",
    "pytest-mock~=3.6",
    "requests_mock~=1.8",
]

setup(
    entry_points={
        "console_scripts": [
            "source-instagram=source_instagram.run:run",
        ],
    },
    name="source_instagram",
    description="Source implementation for Instagram.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
