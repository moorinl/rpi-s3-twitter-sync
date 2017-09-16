from setuptools import find_packages, setup


setup(
    name='s3-twitter-sync',
    version='0.1.0',
    description='S3 Twitter Sync.',
    author='Rob Moorman',
    author_email='rob@moori.nl',
    scripts=[
        'sync.py'
    ],
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
)
