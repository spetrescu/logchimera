# logchimera

Test log parsing on heterogeneous industry data.

## Development MacOS
1. Install `miniconda`
```bash
$ mkdir -p ~/miniconda3
$ curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
$ rm -rf ~miniconda3/miniconda.sh
```
2. Initialize `miniconda` for bash / zsh shells
```bash
$ ~/miniconda3/bin/conda init bash
$ ~/miniconda3/bin/conda init zsh
```
3. Create `logchimera` virtual environment and activate it
```bash
$ conda create --name logchimera python=3.9 -y
$ conda activate logchimera
$ pip install poetry
```
4. Install package
```bash
$ git clone https://github.com/spetrescu/logchimera.git
$ cd logchimera
$ poetry install
```
5. Check if installation was successfull
```bash
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44) 
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import function_test
>>>
```

## Development Linux
1. Install `miniconda`
```bash
$ mkdir -p ~/miniconda3
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
$ bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
$ rm -rf ~/miniconda3/miniconda.sh
```
2. Initialize `miniconda` for bash / zsh shells
```bash
$ ~/miniconda3/bin/conda init bash
$ ~/miniconda3/bin/conda init zsh
```
3. Create `logchimera` virtual environment and activate it
```bash
$ conda create --name logchimera python=3.9 -y
$ conda activate logchimera
$ pip install poetry
```
4. Install package
```bash
$ git clone https://github.com/spetrescu/logchimera.git
$ cd logchimera
$ poetry install
```
5. Check if installation was successfull
```bash
$ python
Python 3.9.17 (main, Jul  5 2023, 20:41:20) 
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import function_test
>>>
```

## Installation

```bash
$ pip install logchimera
```

## Usage

```python
import logchimera
...
```

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`logchimera` was created by Stefan Petrescu. It is licensed under the terms of the MIT license.

## Credits

`logchimera` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
