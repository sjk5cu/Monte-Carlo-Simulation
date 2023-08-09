from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url='https://github.com/sjk5cu/montecarlo.git',
    author='Stephen Kullman',
    author_email='sjk5cu@virginia.edu',
    description='Monte Carlo Simulation Final Project',
    packages=find_packages(),    
    install_requires=['numpy', 'pandas','random']
)