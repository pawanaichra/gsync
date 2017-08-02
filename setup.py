from setuptools import setup

setup(
    name="gsync",
    version='0.0.1',
    description="Open Source google drive",
    long_description="",
	author = 'Pawan Aichra',
	author_email = 'aichrapawan@gmail.com',
	plateforms = ['OS Independent'],
    classifiers=[
        "Topic :: drive :: google drive",
        "Topic :: storage :: online-store"
    ],
    url="https://github.com/pawanaichra/gsync",
    license="MIT License",
    packages=['gsync'],
	keywords = ['google-drive', 'folder-sync'],
    entry_points={
        'console_scripts': [
            'gsync = gsync.cli:main']},
    install_requires=[
        "google-api-python-client"
    ],

)