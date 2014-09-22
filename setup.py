"""
Flask-Swagger
-------------

This is the description for that library
"""
from setuptools import setup


setup(
    name='Flask-Swagger',
    version='1.2',
    url='https://github.com/spil-rkoopmans/flask-sillywalk',
    license='BSD',
    author='Robin Walsh & Harvey Rogers',
    author_email='rob.walsh@gmail.com',
    description='So you want to implement an auto-documenting API?',
    long_description=__doc__,
    py_modules=['flask_sillywalk'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Spilgames :: Internal'
    ]
)
