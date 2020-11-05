from setuptools import setup

setup(
    name = "google-data-load",
    version = "1.0.0RC",
    author = "Juan Domingos",
    author_email = "juan.eduardo@outlook.com.br",
    license = "MIT",
    package = ['br.com.domingos.juan', 'br.com.domingos.juan.jobs', 'br.com.domingos.juan.utils'],
    namespace_packages = ['br', 'br.com', 'br.com.domingos'],
    install_requires=open('requirements.txt').readlines(),
    tests_require=['pytest'],
    zip_safe=False
)