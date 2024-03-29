#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

MAIN_REQUIREMENTS = ["airbyte-cdk"]

TEST_REQUIREMENTS = [
    "pytest-mock~=3.6.1",
    "pytest~=6.1",
    "requests-mock",
]

setup(
    entry_points={
        "console_scripts": [
            "source-linkedin-ads=source_linkedin_ads.run:run",
        ],
    },
    name="source_linkedin_ads",
    description="Source implementation for Linkedin Ads.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=MAIN_REQUIREMENTS,
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
