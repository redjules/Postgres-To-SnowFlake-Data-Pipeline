#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

TEST_REQUIREMENTS = ["pytest-mock~=3.6.1", "pytest~=6.1", "responses~=0.19.0", "requests-mock~=1.9.3"]


setup(
    entry_points={
        "console_scripts": [
            "source-mailchimp=source_mailchimp.run:run",
        ],
    },
    name="source_mailchimp",
    description="Source implementation for Mailchimp.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=[
        "airbyte-cdk",
        "pytest~=6.1",
    ],
    package_data={"": ["*.json", "schemas/*.json", "schemas/shared/*.json"]},
    extras_require={"tests": TEST_REQUIREMENTS},
)
