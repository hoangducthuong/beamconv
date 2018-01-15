from setuptools import setup

setup(name='cmb_beams',
      version='0.1',
      description='Code for beam convolution.',
      url='https://github.com/oskarkleincentre/cmb_beams',
      author='Adri J. Duivenvoorden',
      author_email='adri.j.duivenvoorden@gmail.com',
      license='MIT',
      packages=['cmb_beams', 'tests'],
      install_requires=['healpy', 'numpy', 'qpoint'],
      test_suite='tests',
      zip_safe=False)
