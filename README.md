# logchimera

 `logchimera` was born out of a research innitiative ([Log Parsing Evaluation in the Era of Modern Software Systems](https://arxiv.org/abs/2308.09003)), as a consequence of a general lack of access to heterogeneous log data typically found in industry. With `logchimera` you can generate and evaluate log parsing on heterogeneous industry-like data from publicly available logs. The name of the tool is inspired by the mythological creature _chimera_, which symbolizes a fusion or combination of different elements; and in this case, it reflects heterogeneity by enabling bringing together diverse formats from various logs to resemble industry-like contexts.

<div align="left">
  <p>
<!--   <img width="230" alt="Group_movie" src="https://user-images.githubusercontent.com/60047427/122675863-a7e86380-d1db-11eb-84f4-d4a3bc488209.jpg"> -->
  <img width="230" alt="Group_movie" src="https://github.com/spetrescu/logchimera/assets/60047427/10cc52d6-dc33-4159-a99c-cfc279cf3f11.jpg">
  <img width="230" alt="Group_movie" src="https://github.com/spetrescu/logchimera/assets/60047427/d2012c9d-753c-4b9d-b867-1c65896c26df.jpg">
  <img width="230" alt="Group_movie" src="https://github.com/spetrescu/logchimera/assets/60047427/cdc0d927-fbf5-48be-8a6c-e033fb4af958.jpg">

  </p>
  <p>
    <a href="">
      <img alt="First release" src="https://img.shields.io/badge/release-v0.1.0-brightgreen.svg" />
    </a>
  </p>
</div>

## Usage
We display below how you can use `logchimera`. Currently, `logchimera` can do the following:
1. Estimate heterogeneity for a log dataset
2. Increase the heterogeneity for a log dataset
3. Transform industry data into publicly available data with equivalent properties

To use `logchimera`, make sure you first follow the set-up section corresponding to your system (currently available for Linux or Mac).
### 1. Estimate heterogeneity
To estimate log heterogeneity, simply provide the path to your file. Currently, `logchimera` is able to estimate heterogeneity for a file of arbitrary size. The only requirement that needs to be met is for your file to contain the log lines separated by a new line character. Below you can see a sample of what `logchimera` would expect in terms of an input file.

#### Sample input file:
```
workerEnv.init() ok /etc/httpd/conf/workers2.properties
mod_jk child init 1 -2
jk2_init() Found child 5785 in scoreboard slot 6
...
```
#### Example 1 (estimate heterogeneity)
```python
# example estimating heterogeneity in python shell
$ python
Python 3.9.17 (main, Jul  5 2023, 20:41:20) 
[GCC 11.2.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import estimate_heterogeneity
>>> from logchimera.datasets import get_example_data_for_estimating_heterogeneity
>>> example_file_path = get_example_data_for_estimating_heterogeneity()
>>> estimate_heterogeneity(example_file_path)
# Returns a 3-decimal floating-point value in the range [0, 1], e.g., 0.222; higher means more heterogeneous.
...
```
#### Example 2 (estimate heterogeneity)
```python
# example estimating heterogeneity in python script
from logchimera.logchimera import estimate_heterogeneity
from logchimera.datasets import get_example_data_for_estimating_heterogeneity
example_file_path = get_example_data_for_estimating_heterogeneity()
h_level = estimate_heterogeneity(example_file_path) # Returns a 3-decimal floating-point value in the range [0, 1], e.g., 0.222; higher means more heterogeneous.
print(h_level)
...
```

## Set-up MacOS
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

## Set-up Linux
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
>>> from logchimera.logchimera import estimate_heterogeneity
>>>
```

## Installation

```bash
$ pip install logchimera
```

## Artifact: Reproduce Experiments from Original Paper
To reproduce the experiments conducted during the research initiative that led to the creation of `logchimera`, please refer to the [ARTIFACT.md file](https://github.com/spetrescu/logchimera/blob/main/ARTIFACT.md).

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`logchimera` was created by Stefan Petrescu. It is licensed under the terms of the MIT license.

## Credits for Initial Package Structure

The initial package structure of `logchimera` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).

## Citation
To cite this package, you can use the following BibTeX entry:
```python
@INPROCEEDINGS{petrescu2023issre,
author={Petrescu, Stefan and den Hengst, Floris and Uta, Alexandru and Rellermeyer, Jan S.},
booktitle={34th IEEE International Symposium on Software Reliability Engineering (ISSRE)},
title={Log Parsing Evaluation in the Era of Modern Software Systems},
year={2023}}
```



