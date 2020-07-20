from setuptools import setup


install_requires = [
    'rocketchat-API==1.6.0'
]

setup(
    name='rocketchat',
    version='1.0.0',
    packages=['rocketchat'],
    install_requires=install_requires,
    author='Danilo Vargas',
)
