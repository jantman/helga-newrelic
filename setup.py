from setuptools import setup, find_packages

version = '0.1'

setup(name="helga-newrelic",
      version=version,
      description=('IRC bot using twisted'),
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: IRC',
                   'Intended Audience :: Twisted Developers, IRC Bot Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='irc bot newrelic helga',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/helga',
      license='MIT',
      packages=find_packages(),
      entry_points = dict(
          helga_plugins=[
              'newrelic = helga_newrelic.plugins:newrelic',
          ],
          helga_webhooks=[
              'newrelic = helga_newrelic.webhooks:newrelic',
          ],
      ),
)
