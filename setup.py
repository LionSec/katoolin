from setuptools import find_packages, setup


setup(
    name = 'katoolin',
    version = '3.0',
    description = 'install kali packages on debian and its derivatives',
    url = 'https://github.com/b166erobot/katoolin',
    author = 'https://github.com/LionSec',
    licence = 'GNU GENERAL PUBLIC LICENSE',
    packages = find_packages(),
    include_package_data = True,
    package_data = {
        '': ['banner.txt', '*.md']
    },
    entry_points = {
        'console_scripts': [
            'katoolin3=katoolin.katoolin3install:main',
        ]
    },
    zip_safe = False
)
