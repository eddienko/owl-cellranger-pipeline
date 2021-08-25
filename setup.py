from setuptools import find_packages, setup

readme = ""

requirements = [
    "dask",
    "distributed",
    "voluptuous",
]

setup_requirements = ["pytest-runner", "flake8"]

test_requirements = ["coverage", "pytest", "pytest-cov", "pytest-mock"]


setup(
    author="Eduardo Gonzalez Solares",
    author_email="eglez@ast.cam.ac.uk",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3.7",
    ],
    description="Owl CITE Seq Count Pipeline",
    entry_points={"owl.pipelines": "cellranger = owl_cellranger"},
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    include_package_data=True,
    keywords="owl",
    name="owl-cellranger-pipeline",
    packages=find_packages(include=["owl_cellranger*"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/eddienko/owl-cellranger-pipeline",
    version="0.1.0",
    zip_safe=False,
    python_requires=">=3.7",
)
