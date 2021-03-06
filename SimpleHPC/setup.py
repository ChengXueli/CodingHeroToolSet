from setuptools import setup, find_packages

setup(name="hpc",
      version="1.0",
      license="GPLv2",
      description="This lib is used for HPC jobs distribution",
      keywords=["hpc", "job"],
      author="Xueli Cheng",
      author_email="chengxl842363@gmail.com",
      packages=find_packages(),
      install_requires=["openpyxl"],
      include_package_data=True,
      package_data={"": ["*.xlsm"]},
      exclude_package_data={'': ['README.md']},
      entry_points={'console_scripts': [
          'progress_server = hpc.app.app_master:main',
      ]},
      platforms="Windows"
      )
