from setuptools import setup

setup(
    name='CuriosiPy',
    version='0.1',
    description='Track Mars Curiosity Rover Tweets',
    url='https://github.com/howard-roark/CuriosiPy',
    author='Matt McGuire',
    author_email='matt@mwmcguire.com',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    packages=['src'],
    install_requires=[
        'certifi==2017.7.27.1',
        'chardet==3.0.4',
        'docutils==0.14',
        'gpiocrust==1.0.0',
        'idna==2.6',
        'lockfile==0.12.2',
        'luigi==2.8.0',
        'numpy==1.13.1',
        'pandas==0.20.3',
        'py==1.4.34',
        'pytest==3.2.1',
        'python-daemon==2.1.2',
        'python-dateutil==2.6.1',
        'pytz==2017.2',
        'requests==2.18.4',
        'tornado==4.5.2',
        'urllib3==1.22'
    ],
)
