from setuptools import setup, find_packages

setup(
    name="dsss_homework_2",  # Replace with your project's name
    version="0.1.0",  # Replace with the appropriate version
    author="Hari",  # Replace with the author's name
    author_email="haripvtt@gmail.com",  # Replace with the author's email
    description="A brief description of your project",  # Short description of your package
    long_description=open("README.md").read(),  # Long description from a README file (optional)
    long_description_content_type="text/markdown",  # If using Markdown for README
    url="https://github.com/username/dsss_homework_2",  # Replace with the URL of your project (e.g., GitHub)
    packages=find_packages(),  # Automatically find all the packages in your project
    classifiers=[  # Optional, list of classifiers to categorize your project on PyPI
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[  # List of external dependencies required for your package
        "requests",  # Example of a dependency
        "numpy",     # Another example, replace with your actual dependencies
    ],
    python_requires='>=3.6',  # Minimum Python version required
    include_package_data=True,  # Include non-Python files listed in MANIFEST.in
    entry_points={  # Optional: Define command-line scripts or entry points if needed
        "console_scripts": [
            "my-script=my_module.main:main_function",  # Example command for running the script
        ],
    },
)
