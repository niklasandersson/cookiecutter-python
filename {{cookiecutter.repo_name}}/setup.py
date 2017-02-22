from setuptools import setup, find_packages

setup(
    name='hej',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        main={{cookiecutter.repo_name}}.main:main
    '''
)
