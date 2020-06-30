from setuptools import setup, find_packages

setup(
  name = 'compressive_transformer_pytorch',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Implementation of Compressive Transformer in Pytorch',
  author = 'Phil Wang',
  author_email = 'lucidrains@gmail.com',
  url = 'https://github.com/lucidrains/compressive-transformer-pytorch',
  keywords = ['attention', 'artificial intelligence', 'transformer', 'deep learning'],
  install_requires=[
      'torch'
  ],
  classifiers=[
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'License :: OSI Approved :: MIT License',
      'Programming Language :: Python :: 3.6',
  ],
)