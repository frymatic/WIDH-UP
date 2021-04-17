import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="", # Replace with your own username
    version="0.0.1",
    author="kelu124",
    author_email="author@example.com",
    description="Covid-19 diagnosis using Ultrasound imaging and AI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kelu124/WIDH-UP",
    project_urls={
        "Bug Tracker": "https://github.com/kelu124/WIDH-UP/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",        
        "Operating System :: OS Independent",
    ],
    
)