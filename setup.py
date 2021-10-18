import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent
readme = (here / "README.rst").read_text(encoding="utf-8")

setup(
    name="saudi-id-validator",
    version="1.0.7",
    description="Validate ID numbers of Saudi Arabian identity cards",
    long_description=readme,
    long_description_content_type="text/x-rst",
    url="",
    author="Mohd Alshehri",
    author_email="",
    license="MIT",
    classifiers=["Development Status :: 7 - Inactive"],
    keywords="saudi government validator identity number",
    py_modules=[module.stem for module in here.glob("src/*.py")],
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.5",
)
