from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='mpu9150-raspberrypi',
      version='1.0.3.4',
      description='A Python module for accessing the MPU-9150 digital accelerometer and gyroscope on a Raspberry Pi.',
      classifiers=[
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries',
          'Programming Language :: Python :: 2.7',
          'Operating System :: POSIX :: Linux',
      ],
      keywords='mpu9150 raspberry',
      url='https://github.com/stsdc/mpu9150',
      author='stsdc',
      license='MIT',
      packages=['mpu9150'],
      scripts=['bin/mpu9150-example'],
      zip_safe=False,
      long_description=readme())
