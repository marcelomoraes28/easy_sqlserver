from setuptools import setup

setup(name='easy_sqlserver',
      description='A simple active record to assist in manipulating SQL Server data',
      long_description="This is a simple library to assist in manipulating SQL Server data",
      version='0.0.7',
      url='https://github.com/marcelomoraes28/easy_sqlserver',
      author='Marcelo Moraes',
      author_email='marcelomoraesjr28@gmail.com',
      license='MIT',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
      ],
      packages=['easy_sqlserver',
                'easy_sqlserver/filters'],
      install_requires='pymssql>=2.1.3',
      )
