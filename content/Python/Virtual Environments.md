---
title: Virtual environments in Python
draft: false
---

# Virtual environments in Python 

- Allow to disentangle the system-level *python* and the one that is used in a given project
- Allows to use different versions of the same library, across multiple projects

## Handling environments through *anaconda*

- Create a *conda* (virtual) environment with a given name ("env_name") and a given python version (that doesn't need to be installed in the computer):

```bash
conda create -n env_name python=3.9
```

- Activate the environment:
```bash
conda activate env_name
```
- Install libraries:
```bash
conda install -n env_name numpy
```

## Handling environments through *venv*

- Comes by default with python, avoiding installation of other programs
- Create an environment:
```bash
python -m venv env_name
```
- Activation of environment:
```bash
source env_name/bin/activate
```

## Installation of libraries:

- After the environment is active, we also have a version of pip available to us:
```bash
pip install numpy
```
or, if we have a list of requirements:
```bash
pip install -r requirements.txt
```

## Other options:

- **poetry**: https://python-poetry.org/


> [!info] References
> https://docs.python.org/3/library/venv.html
> 
> https://pip.pypa.io/en/stable/user_guide/
