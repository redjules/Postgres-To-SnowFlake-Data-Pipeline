#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


from setuptools import find_packages, setup

TEST_REQUIREMENTS = [
    "requests-mock~=1.9.3",
    "pytest-mock~=3.6.1",
    "pytest~=6.1",
]

setup(
    entry_points={
        "console_scripts": [
            "source-slack=source_slack.run:run",
        ],
    },
    name="source_slack",
    description="Source implementation for Slack.",
    author="Airbyte",
    author_email="contact@airbyte.io",
    packages=find_packages(),
    install_requires=["airbyte-cdk", "pendulum>=2,<3"],
    package_data={"": ["*.json"]},
    extras_require={
        "tests": TEST_REQUIREMENTS,
    },
)
