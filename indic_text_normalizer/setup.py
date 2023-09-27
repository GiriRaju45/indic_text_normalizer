from setuptools import setup

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="indic_text_norm",
    version='1.0.0',
    description="A module to normalize indian text by converting the short-forms and representation into their full-forms and actual word representation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AI4Bhārat",
    author_email="opensource@ai4bharat.org",
    packages=['indic_text_norm'],
    package_dir= {'indic_text_norm': 'indic_text_norm'},
    package_data= {'indic_text_norm':['data/*.json']},
    install_requires= ["pytest", "indic-numtowords"],
    include_package_data=True,
    python_requires='>=3.6',
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries"
    ],
)