from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="car_price_preprocessing",
    version="0.1",
    packages=find_packages(include=["preprocessing"]),  # Explicitly include preprocessing
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False
)
