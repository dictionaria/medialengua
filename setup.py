from setuptools import setup


setup(
    name='cldfbench_medialengua',
    py_modules=['cldfbench_medialengua'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'medialengua=cldfbench_medialengua:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
        'pyglottolog',
        'pydictionaria>=2.1',
        'openpyxl',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
