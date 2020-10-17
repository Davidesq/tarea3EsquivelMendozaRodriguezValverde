from setuptools import setup

setup(
    name='tarea3_micros',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github.com:Davidesq/prueba_pack_1.git',
    author='david',
    author_email='devdavesq@gmail.com',
    license='unlicense',
    packages=['tarea3_micros'],
    install_requires=['opencv-python', 'playsound', 'prettytable'],
    python_requires='>=3.6',
    package_dir={'tarea3_micros':'tarea3_micros'},
    scripts=['bin/bin_text', 'bin/bin_image', 'bin/bin_audio']
)
