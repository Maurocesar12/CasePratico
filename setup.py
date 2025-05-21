from setuptools import setup

setup(
    name="email_classifier",
    version="0.1",
    install_requires=[
        'flask>=2.0.0',
        'transformers>=4.0.0',
        'torch>=1.8.0',
        'nltk>=3.6.0'
    ],
)