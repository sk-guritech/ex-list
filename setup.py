from __future__ import annotations

from setuptools import setup

with open('README.md', encoding='utf-8') as readme_md:
    long_description = readme_md.read()

setup(
    name='ex-list',
    version='0.1.6',
    author='Sakaguchi Ryo',
    author_email='sakaguchi@sk-techfirm.com',
    description='This is a utility library that extends Python\'s list operations.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sk-guritech/ex-list',
    project_urls={
        'Bug Tracker': 'https://github.com/sk-guritech/ex-list/issues',
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['list', 'comprehension', 'iterable', 'code quality'],
    packages=['.'],
    python_requires='>=3.10',
    install_requires=['typing_extensions'],
)
