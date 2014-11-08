from setuptools import setup, find_packages

setup(
    name="flmakesetup",
    version="0.0.1",
    author="takahrio iwatani",
    author_email="taka.05022002@gmail.com",
    description="easy create setup.py",
    url="http",
    py_modules=["autosetup"],
    entry_points={
        "console_scripts":[
            "create-setuppy = autosetup:create_setuppy"
        ]
    }
)
