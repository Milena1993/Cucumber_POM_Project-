SeleniumPythonPytestBDD Banking Project 

## Setup

Install all the required Python modules using `pip`:

You can get a copy of all files used in this tutorial by cloning this repository!

```shell
git clone git@github.com:Milena1993/Cucumber_POM_Project-.git
```
The first required modules are

```shell
pip install selenium
```
```shell
pip install python
```
```shell
pip install Faker
```
The project is created under Python 3.9.6

### To use Cucumber and Gerkin with pytest install 

```shell
pip install pytest 
```
```shell
pip install pytest bdd
```
```shell
pip install gherkin-official
```
**NOTE**: This step can be skipped if you've cloned the repository and install all Python dependencies.

Run tests using: 
```shell
python -m pytest -v 
```
Run tests including all the print statments using:
```shell
python -m pytest -s 
```
Run tests in parallel first install pytest xdist:
```shell
pip install pytest-xdist
```
Run tests in parallel using:
```shell
python -m pytest -n 4
```
