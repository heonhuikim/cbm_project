import os
from glob import glob

from setuptools import setup

package_name = 'adc_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Heon-Hui Kim',
    maintainer_email='heonhuikim@mmu.ac.kr',
    description='8CH 24Bit ADC reading and publishing the sensor readings',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'adc_talker = adc_package.adc_read_pub:main',
            'adc_listener = adc_package.adc_read_sub:main',
        ],
    },
)
