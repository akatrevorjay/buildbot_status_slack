from setuptools import setup, find_packages


setup(
    name='buildbot_status_slack',
    version='0.1.0',
    author=['Sylvain Zimmer', 'Marten Klitzke', 'Raphael Randschau'],
    packages=find_packages(),
    scripts=[],
    url='https://github.com/mindmatters/buildbot-status-slack',
    license='LICENSE.txt',
    description='slack status plugin for buildbot',
    long_description=open('README.md').read(),
    install_requires=[
        "buildbot >= 0.8.0",
    ],
)