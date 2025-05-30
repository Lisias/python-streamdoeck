import setuptools

with open("VERSION", 'r') as f:
    version = f.read().strip()

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
   name='python-streamdoeck',
   version=version,
   description='Library to control Elgato StreamDeck and Mirabox StreamDock devices.',
   author='Lisias',
   author_email='projects@lisias.net',
   url='https://github.com/StreamDoeck/python-streamdoeck',
   package_dir={'': 'src'},
   packages=setuptools.find_packages(where='src'),
   install_requires=[],
   license="MIT",
   long_description=long_description,
   long_description_content_type="text/markdown",
   include_package_data=True,
   python_requires='>=3.8',
)
