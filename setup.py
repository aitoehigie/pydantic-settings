from setuptools import setup, find_packages

setup(
    name='pydantic-settings',
    version='0.1.0',
    description='A Python package for managing settings with Pydantic',
    author='Your Name',
    author_email='your@email.com',
    url='https://github.com/yourusername/pydantic-settings',
    packages=find_packages(),
    install_requires=[
        'pydantic',  # Add any other dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
