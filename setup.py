from setuptools import find_packages, setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author='vishy',
    author_email='vishyp@yahoo.com',
    install_required=["openai", "langchain", "python-dotenv", "PyPDF2"],
    packages=find_packages()
)