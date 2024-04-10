import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summerizer-AI"
AUTHOR_USER_NAME = "SabitCanTurunc"
SRC_REPO = "textSummerizer"
AUTHOR_EMAIL = "turuncsc@gmail.com"

setuptools.setup(

    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    email=AUTHOR_EMAIL
    description="A small python package for NLP app",
    Long_description=long_description,
    Long_description_content="text/markdown",

    url="https://github.com/SabitCanTurunc/Text-Summerizer-AI",
    project_urls={
        "Bug Tracker": "https://github.com/SabitCanTurunc/Text-Summerizer-AI/issues",
    },
    package_dir={'': 'src'},

    packages=setuptools.find_packages(where='src'),
)
