import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = 'Text-Summarizer'
AUTHOR_SER_NAME = "Ambigapathi-V"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "ambigapathikavin2@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_SER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A simple text summarizer using Gensim",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/Ambigapathi-V/{REPO_NAME}",
    packages=setuptools.find_packages(where='src'),
    project_urls={
        "Bug Tracker": f"https://github.com/Ambigapathi-V/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
)
