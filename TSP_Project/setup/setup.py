from setuptools import setup, find_packages

setup(
    name="tsp_solver",
    version="1.0.0",
    author="Phan Dang Khoa",
    author_email="khoadangphan307@gmail.com",
    description="Mô phỏng bài toán người du lịch",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Silnix/csn-da22ttb-phandangkhoa-tsp-python",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy",
    ],
    entry_points={
        "console_scripts": [
            "tsp_solver=main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
