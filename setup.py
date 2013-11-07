from setuptools import setup, find_packages

setup(
    name='djlime-filebrowser',
    version='0.1',
    description='Media-Management with the Django Admin-Interface.',
    author='Patrick Kranzlmueller, Andrey Butenko, Andrey Voronov',
    author_email='voronov84+github@gmail.com',
    url='https://github.com/freshlimestudio/djlime-filebrowser',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
