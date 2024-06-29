from setuptools import setup, find_packages

setup(
    name='django-users-vehicle-forms-api',  # Corrected app name
    version='3.12.4',  # Matches your preferred version
    packages=find_packages(where='.', exclude=[]),  # Comprehensive package discovery
    include_package_data=True,  # Includes static and media files
    description='An API for managing users and their vehicles in Django',
    author='Hazem-Adel',
    author_email='zoma0097@gmail.com',
    license='MIT',
    # Install dependencies (consider dynamic requirements with `pipreqs`)
    install_requires=[
        'django>=3.12.4,<3.13.0'  # Example dependency (update as needed)
    ],
    # Optional classifiers for better discoverability (uncomment as needed)
     classifiers=[
         'Development Status :: 3 - Alpha',
         'Environment :: Web Environment',
         'Framework :: Django',
         'Intended Audience :: Developers',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Programming Language :: Python :: 3',
         'Topic :: Software Development :: Libraries :: Python Modules',
     ]
)
