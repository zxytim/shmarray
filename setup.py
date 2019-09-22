import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open("requirements.txt") as f:
    requirements = [line.strip() for line in f]


setuptools.setup(
    name="shmarray",
    version="0.0.3",
    author="Xinyu Zhou",
    author_email="zxytim@gmail.com",
    description="A polished shmarray, originated by David Baddeley",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zxytim/shmarray",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
