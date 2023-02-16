import setuptools

with open('readme.md', encoding='utf-8') as file:
    read_me_desc = file.read()


setuptools.setup(
    name='calculator22',
    version='0.2',
    author='Vilena',
    author_email='vilenamuzipova@gmail.com',
    description='calculator is a python method for simple math actions',
    long_description=read_me_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/VilenaMuzipova/calculatorPyPi',
    packages=['calculator22'],
    install_requires=['logging'],
    python_requires='>=3.6'
)