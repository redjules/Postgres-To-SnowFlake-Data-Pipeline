#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = [
    "airbyte-cdk",
]

TEST_REQUIREMENTS = [
    "pytest~=6.1",
    "pytest-faker==2.0.0",
    "pytest-mock~=3.6.1",
    "requests-mock",
]

setup(
    entry_points={
        "console_scripts": [
            "source-marketo=source_marketo.run:run",
        ],
    },
    name="source_marketo",
    description="Source implementation for Marketo.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
