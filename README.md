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
$ git checkout issre_23_code
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
$ git checkout issre_23_code
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

## Example usage ISSRE 23
### Use `logchimera` for mixing
<img width="400" alt="table_vi" src="https://github.com/spetrescu/logchimera/assets/60047427/08079592-6cca-481f-be26-958a7969cc4f">

```bash
# Apache example. To obtain different levels of heterogeneity, vary the heterogeneity level (the second parameter) from 0 to 1. Example values: 0.22 (for Apache 5)
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/Apache/Apache_2k.log_structured.csv", 0.22, "Apache")
Heterogeneity is: 0.5304069912609239 for dataset datasets_mixing/5_Apache.csv # corresponds to the second row in table vi (0.530, Apache 5)
>>> increase_heterogeneity_for_file("experiments/Apache/Apache_2k.log_structured.csv", 0.40, "Apache")
Heterogeneity is: 0.6399750312109863 for dataset datasets_mixing/10_Apache.csv # corresponds to the third row in table vi (0.640, Apache 10)
>>> increase_heterogeneity_for_file("experiments/Apache/Apache_2k.log_structured.csv", 0.57, "Apache")
Heterogeneity is: 0.7366891385767791 for dataset datasets_mixing/15_Apache.csv # corresponds to the fourth row in table vi (0.737, Apache 15)
>>> increase_heterogeneity_for_file("experiments/Apache/Apache_2k.log_structured.csv", 0.95, "Apache")
Heterogeneity is: 0.8861722846441948 for dataset datasets_mixing/25_Apache.csv # corresponds to 0.886, Apache 25
```

```bash
# BGL example. To obtain different levels of heterogeneity, vary the heterogeneity level (the second parameter) from 0 to 1. Example values: 0.69 (for BGL 15)
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/BGL/BGL_2k.log_structured.csv", 0.25, "BGL")
Heterogeneity is: 0.7564544319600499 for dataset datasets_mixing/5_BGL.csv # corresponds to 0.756, BGL 5
>>> increase_heterogeneity_for_file("experiments/BGL/BGL_2k.log_structured.csv", 0.47, "BGL")
Heterogeneity is: 0.8325243445692885 for dataset datasets_mixing/10_BGL.csv # corresponds to 0.833, BGL 10
>>> increase_heterogeneity_for_file("experiments/BGL/BGL_2k.log_structured.csv", 0.69, "BGL")
Heterogeneity is: 0.9082347066167291 for dataset datasets_mixing/15_BGL.csv # corresponds to 0.908, BGL 15
>>> increase_heterogeneity_for_file("experiments/BGL/BGL_2k.log_structured.csv", 0.93, "BGL")
Heterogeneity is: 0.9489438202247192 for dataset datasets_mixing/20_BGL.csv # corresponds to 0.949, BGL 20
```

```bash
# HPC example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/HPC/HPC_2k.log_structured.csv", 0.60, "HPC")
Heterogeneity is: 0.7347465667915107 for dataset datasets_mixing/15_HPC.csv # corresponds to 0.730, HPC 15
```

```bash
# Mac example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/Mac/Mac_2k.log_structured.csv", 0.40, "Mac")
Heterogeneity is: 0.9011235955056179 for dataset datasets_mixing/5_Mac.csv # corresponds to 0.901, Mac 5
```
### Use `logchimera` for fuzzing
<img width="1286" alt="table_vii" src="https://github.com/spetrescu/logchimera/assets/60047427/f682a95f-faa1-45ad-a7cd-48d45ed1fdf8">

```bash
# Apache example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import fuzz_data, increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/Apache/Apache_2k.log_structured.csv", 0.95, "Apache")
Heterogeneity is: 0.8861722846441948 for dataset datasets_mixing/25_Apache.csv # corresponds to 0.886, Apache 25
>>> fuzz_data("datasets_mixing/25_Apache.csv", "Apache", 25)
Heterogeneity is: 1.0 for dataset fuzzing/Apache_25_fuzzed.csv
```

```bash
# HPC example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import fuzz_data, increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/HPC/HPC_2k.log_structured.csv", 0.99, "HPC")
Heterogeneity is: 0.8810786516853932 for dataset datasets_mixing/25_HPC.csv # corresponds to 0.881, BGL HPC 25
>>> fuzz_data("datasets_mixing/25_HPC.csv", "HPC", 25)
Heterogeneity is: 0.9094831460674158 for dataset fuzzing/HPC_25_fuzzed.csv
```

```bash
# BGL example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import fuzz_data, increase_heterogeneity_for_file
>>> increase_heterogeneity_for_file("experiments/BGL/BGL_2k.log_structured.csv", 0.93, "BGL")
Heterogeneity is: 0.9489438202247192 for dataset datasets_mixing/20_BGL.csv # corresponds to 0.949, BGL 20
>>> fuzz_data("datasets_mixing/20_BGL.csv", "BGL", 20)
Heterogeneity is: 1.0 for dataset fuzzing/BGL_20_fuzzed.csv
```

```bash
# Mac example
$ python
Python 3.9.16 (main, Mar  8 2023, 04:29:44)
[Clang 14.0.6 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from logchimera.logchimera import fuzz_data
>>> fuzz_data("datasets_mixing/8_Mac.csv", "Mac", 8)
Heterogeneity is: 1.0 for dataset fuzzing/Mac_8_fuzzed.csv
```


## Installation

```bash
$ pip install logchimera
```

## Usage

```python
from logchimera.logchimera import estimate_heterogeneity
h_level = estimate_heterogeneity("Apache.csv") 
# Returns a 3-decimal floating-point value in the range [0, 1], e.g., 0.959
...
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



