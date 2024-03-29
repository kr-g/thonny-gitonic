import setuptools
import os
import re

with open("README.md", "r") as fh:
    long_description = fh.read()


def find_version(fnam, version="VERSION"):
    with open(fnam) as f:
        cont = f.read()
    regex = f'{version}\s*=\s*["]([^"]+)["]'
    match = re.search(regex, cont)
    if match is None:
        raise Exception(
            f"version with spec={version} not found, use double quotes for version string"
        )
    return match.group(1)


def find_projectname():
    cwd = os.getcwd()
    name = os.path.basename(cwd)
    return name


file = os.path.join("thonnycontrib", "gitonic", "__init__.py")
version = find_version(file)
projectname = find_projectname()


packages = setuptools.find_packages()
print(packages)

setuptools.setup(
    name=projectname,
    version=version,
    author="k. goger",
    author_email=f"k.r.goger+{projectname}@gmail.com",
    description="manage a multi git workspace",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/kr-g/{projectname}",
    packages=packages,
    license="AGPLv3+",
    keywords="python utility shell git git-workspace tkinter thonny",
    install_requires=[
        "gitonic",
        "thonny >= 3.3.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Environment :: Console",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        "Topic :: Desktop Environment",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    ],
    python_requires=">=3.8",
)

# python3 -m setup sdist build bdist_wheel
# twine upload --repository testpypi dist/*
# twine upload dist/*
