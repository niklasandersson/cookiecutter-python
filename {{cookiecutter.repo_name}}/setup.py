from setuptools import setup, find_packages

setup(
    name='{{cookiecutter.repo_name}}',
    version='{{cookiecutter.version}}',
    url='{{cookiecutter.github_url}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    description='{{cookiecutter.description}}',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        {{cookiecutter.repo_name}}={{cookiecutter.repo_name}}.main:main
    '''
)
