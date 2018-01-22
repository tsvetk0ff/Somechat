from setuptools import setup, find_packages

setup(
    name="Somechat",
    version='0.1.1',
    description='Simple messenger.',
    long_description='Somechat is a simple GUI & console messenger for Windows.',
    url='https://github.com/tsvetk0ff/MessengerProject',
    license='MIT',
    keywords=['python', 'messenger', 'Somechat'],
    author='Igor Tsvetkov',
    author_email='tsvetkov.igor.n@gmail.com',
    packages=find_packages('somechat'),
    install_requires=[
        "PyQt5==5.9.2",
        "SQLAlchemy==1.1.15",
    ],
)
