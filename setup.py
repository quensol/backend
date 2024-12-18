from setuptools import setup, find_packages

setup(
    name="keyword-analysis-api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "sqlalchemy>=1.4.23",
        "pymysql>=1.0.2",
        "python-dotenv>=0.19.0",
        "pydantic>=1.8.2",
        "pandas>=1.3.3",
        "tqdm>=4.62.3",
        "mysql-connector-python>=8.0.26",
        "python-multipart>=0.0.5",
        "psutil>=5.8.0",
        "watchfiles>=0.15.0",
        "websockets>=10.0",
        "numpy>=1.21.0",
    ],
) 