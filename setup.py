from setuptools import setup, find_packages

setup(
    name='my_package',
    version='0.1',
    packages=find_packages(),
    install_requires=["openai", "langchain", "langchain_google_genai", "pillow", "python-dotenv", "streamlit", "PyPDF2"],
    author="Roshan kumar",
    author_email="roshankumarredmi@gmail.com",
    description="A package for generating AI based content",
)