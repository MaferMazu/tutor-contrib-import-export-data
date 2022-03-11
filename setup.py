import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutor_import_export_data", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-contrib-import-export-data",
    version=ABOUT["__version__"],
    url="https://github.com/MaferMazu/tutor-contrib-import-export-data",
    project_urls={
        "Code": "https://github.com/MaferMazu/tutor-contrib-import-export-data",
        "Issue tracker": "https://github.com/MaferMazu/tutor-contrib-import-export-data/issues",
    },
    license="AGPLv3",
    author="Maria Fernanda Magallanes Zubillaga",
    description="import-export-data plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v0": [
            "import-export-data = tutor_import_export_data.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
