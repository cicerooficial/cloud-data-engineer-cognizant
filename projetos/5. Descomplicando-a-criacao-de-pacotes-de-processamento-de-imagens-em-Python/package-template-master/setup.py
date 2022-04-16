from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_name",
    version="0.0.1",
    author="Cicero Henrique",
    author_email="cicerooficial@gmail.com",
    description="Pacote de exercícios simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cicerooficial/cloud-data-engineer-cognizant/tree/main/projetos/5.%20Descomplicando-a-criacao-de-pacotes-de-processamento-de-imagens-em-Python/package-template-master"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10',
)
