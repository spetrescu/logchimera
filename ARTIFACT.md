# `lochimera` Artifact: Log Parsing Evaluation in the Era of Modern Software Systems
This artifact contains information on how to reproduce the experiments of "[Log Parsing Evaluation in the Era of Modern Software Systems](https://arxiv.org/abs/2308.09003)", accepted at ISSRE'23.
We provide instructions on how to reproduce the obtained results for each section of the paper. To simplify reproducibility, all experiments are packaged using Docker. We include all necessary software and data used in the paper, enabling either to evaluate log parsing in various scenarios, showcasing the functionality of the tool presented in the paper (`logchimera`), or reproducing the paper's figures and tables.

## Artifact Description
We organize this document with instructions on reproducing each section of the paper that contains experiments, as following:
```bash
.
├── (1) Artifact Description
├── (2) Environment Setup
├── (3) Getting started
├── (4) Reproducibility Instructions
│   ├── (4.1) Log parsing scrutinized  # Table II, Table III (Section III)
│   ├── (4.2) Heterogeneity analysis   # Figure 4, Table IV  (Section III)
│   ├── (4.3) Proxy metrics weighing   # Table V (Section IV)
│   ├── (4.4) Mixing                   # Table VI (Section IV)
│   ├── (4.5) Mixing and fuzzing       # Table VII (Section IV)
└── └── (4.6) Unlabeled comparison     # Table VIII (Section IV)
```
## Environment Setup
As the artifact is packaged using Docker, the only prerequisites for the evaluation are essentially a properly installed and running Docker daemon. Furthermore, having access to a command line environment is considered to be a prerequisite. In our case, log parsing experiments were run on an AMD server, with Docker version 20.10.5 installed.<br>
Specifically, the experiments were run on the following machines:
- a dual socket AMD Epyc2 machine with 64 cores in total, with a dual Nvidia RTX 2080Ti graphics card setup.
- an Apple M1 Pro machine with 10 cores in total.
In case of experiments that require access to more special resources, such as CUDA enabled GPUs, specific instructions are provided; in such cases, experiments have to be run directly from the sources.

## Getting Started
As mentioned in the environment setup, the only prerequisites for the evaluation are essentially a properly installed and running Docker daemon. Instructions on how to install and run Docker can be found [here](https://docs.docker.com/get-docker/). <br>
To get you started, we showcase the workflow of reproducing an experiment: regardless of the section to be reproduced, other experiments follow a similar setup and workflow, and we consider this example representative. Subsequently, we showcase how to reproduce one cell from Table II and Table III of the [paper](https://arxiv.org/abs/2308.09003). After the Docker imaged is pulled, this experiment should take less than 5 minutes. <br>
Expectation: after following all the steps below, you should expect to have reproduced the first cell of Table II and III, i.e., the measurement for the AEL log parsing method tested on the Apache dataset, which should output a 0.694 log template accuracy and a 10.426 edit-distance. We consider this example to be representative, as obtaining the results for all the other measurements in the tables follows a similar workflow. <br>

Consequently, to get you started, please follow the steps displayed below (Step 1 through 5):<br>
__Step 1__: _Pull the docker image_
```bash
$ docker pull spetrescu/log-parsing-evaluator:py2
# (about 5min)
```
__Step 2__: _Start the image and bash shell_
```
$ docker run -it spetrescu/log-parsing-evaluator:py2 bash
```

**Step 3**: *Go to path for current experiment*
```
$ cd ~/log_parsing_evaluation/experiments/log_parsing_experiments/python2
```

**Step 4**: *Setup environment*
```
$ sh setup_python2.sh
```

**Step 5**: *Run experiment (runs method 10 times)*
```
$ sh run_experiment_python2.sh -m AEL -d Apache
# (about 3m)
# (Expect a result of 0.694 log template accuracy and 10.426 edit-distance)
```
> `-m` specifies the log parsing method to be used and `-d` the dataset.
> 
To reproduce other results, for example, `Drain` on the `BGL` dataset (second cell on the second line of Table II and III), simply replace the method and dataset to be used, namely:

```
sh run_experiment_python2.sh -m Drain -d BGL
# (about 5m)
# (Expect a result of 0.341 log template accuracy and 4.930 edit-distance)
```

All other experiments in the artifact follow a similar workflow.

# (4) Reproducibility Instructions

In this section we describe how to reproduce the paper’s results in detail.
We display below the structure of this section: each section refers to particular Tables or Figures to be reproduced. Should you encounter any issues, additional support and examples on reproducing the experiments can be found [here](https://github.com/spetrescu/logchimera).

```
├── (4) Reproducibility Instructions
│   ├── (4.1) Log parsing scrutinized  # Table II, Table III (Section III)
│   ├── (4.2) Heterogeneity analysis   # Figure 4, Table IV  (Section III)
│   ├── (4.3) Proxy metrics weighing   # Table V             (Section IV)
│   ├── (4.4) Mixing                   # Table VI            (Section IV)
│   ├── (4.5) Mixing and fuzzing       # Table VII           (Section IV)
└── └── (4.6) Unlabeled comparison     # Table VIII          (Section IV)
```

## (4.1) Log parsing scrutinized (Table II, Table III)

The following methods can be tested, in their respective environment.
We recommend following the methods in sequential order, from 1 to 14.

```
No. |   Method      | Python 2 | Python 3 |
-------------------------------------------
1   |   AEL         |     X    |     -    |
2   |   Drain       |     X    |     -    |
3   |   IPLoM       |     X    |     -    |
4   |   LenMa       |     X    |     -    |
5   |   LFA         |     X    |     -    |
6   |   LKE         |     X    |     -    |
7   |   LogCluster  |     X    |     -    |
8   |   LogMine     |     X    |     -    |
9   |   LogSig      |     X    |     -    |
10  |   SHISO       |     X    |     -    |
11  |   SLCT        |     X    |     -    |
12  |   Spell       |     X    |     -    |
13  |   MoLFI       |     -    |     X    |
14  |   NuLog       |     -    |     X    |

```

```
No. |   Dataset         |
-------------------------
1   |   Apache          |
2   |   BGL             |
3   |   HDFS            |
4   |   HealthApp       |
5   |   HPC             |
6   |   Mac             |
7   |   OpenStack       |
8   |   Spark           |
9   |   Windows         |
10  |  Combined_Dataset |

```

### Method 1-12 (Python 2 log parsing methods)

Expectation: after going through all the steps below (1 through 5), you should expect to have reproduced the highlighted sections in the figure below (Table II and III). We start by showcasing how to reproduce the measurement for **AEL** on the **Apache** dataset, which should output a  **0.694** log template accuracy and a **10.426** edit-distance. We consider this example to be representative, as obtaining the results for all the other measurements follows a similar workflow.

Consequently, to get you started, please follow the steps displayed below (1 through 5):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:py2
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:py2 bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/log_parsing_evaluation/experiments/log_parsing_experiments/python2
```

**Step 4**: *Setup environment*

```
$ sh setup_python2.sh
```

**Step 5**: *Run experiment (runs method 10 times)*

```
$ sh run_experiment_python2.sh -m AEL -d Apache
# (about 3m)
# (Expect a result of 0.694 log template accuracy and 10.426 edit-distance)
```

> `-m` specifies the log parsing method to be used and `-d` the dataset.
> 

To reproduce other results, for example, `Drain` on the `BGL` dataset (second cell on the second line of Table II and III), simply replace the method and dataset to be used, namely:

```
$ sh run_experiment_python2.sh -m Drain -d BGL
# (about 5m)
# (Expect a result of 0.341 log template accuracy and 4.930 edit-distance)
```

Similarly, all other cells for Methods 1-12 follow a similar workflow.

### Method 13 (Python 3 log parsing method)

To get you started, please follow the steps displayed below (Step 1 through 5):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:py3
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:py3 bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/log_parsing_evaluation/experiments/log_parsing_experiments/python3
```

**Step 4**: *Setup environment*

```
$ sh setup_python3.sh
```

**Step 5**: *Run experiment (runs method 10 times)*

```
$ sh run_experiment_python3.sh -m MoLFI -d Apache
# (about 6m)
# (Expect a result of 0.27 log template accuracy and 10.179 edit-distance)
```

> `-m` specifies the log parsing method to be used and `-d` the dataset.
> 

### Method 14 (Python 3 log parsing method, CUDA GPU access required)

This experiment requires access to GPU, as the respective method (NuLog [ref]) involves neural network training. However, not having access to that does not pose a threat to validity, and it is only a small part of the experiments (one column in Table II and III). Our experiments were run on a dual socket AMD Epyc2 machine with 64 cores in total, with a dual Nvidia RTX 2080Ti graphics card setup. Experiments in this section have to be run directly from the source.

To get you started, please follow the steps displayed below (Step 1 through 5):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:py3
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:py3 bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/log_parsing_evaluation/experiments/log_parsing_experiments/python3
```

**Step 4**: *Setup environment*

```
$ sh setup_python3.sh
```

**Step 5**: *Run experiment (runs method 10 times)*

```
$ sh run_experiment_python3.sh -m NuLog -d Apache
# (about 10m)
# (Expect a result of 0.560 log template accuracy and 4.679 edit-distance)
```

## (4.2) Heterogeneity analysis (Figure 4, Table IV)

We analyze a variety of datasets, and asses their heterogeneity by considering three metrics, namely *unique number of words*, *unique number of characters*, and *unique number of log lengths*.

To reproduce Figure 4 (based on the measurements from Table IV), follow the steps below (1-5):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:py3
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:py3 bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/analysis-data-heterogeneity
```

**Step 4**: *Generate figures*

```
$ sh measure_statistics.sh
# (about 1m)
# (generates three figures, which correspond to the three subfigures below)
```

**Step 5 (optional)**: *Visualize figure(s)*

To visualize a subfigure (for example, subfigure (a) above), run the command below.

```
$ docker cp <container_id>:/root/analysis-data-heterogeneity/entity_1.pdf <path_on_host>
# (run the above command from host, outside of the Docker container)
```

To discover the `container_id` , run `docker ps -a` on the host machine, outside of the Docker container. Lastly, replace `<path_on_host>` with the path where you would like to save the visualisations. 

```bash
# Example (from host)
$ docker cp e461dc9cc42c:~/analysis-data-heterogeneity/entity_1.pdf ./
```

## (4.3) Proxy metrics weighing (Table V)

To reproduce this table we (1) computed the normalized values for the proxy metrics (by dividing all measurements by the highest element on each respective row) and (2) subsequently computed the variance. We display below the entire process of obtaining the values showcased in the paper (Table V).

Below, we display:

- Initial table (Table IV)
- Normalized table
- Final values table (Table V)

**Initial table (Table V)**

```
Dataset                   | Apache | BGL | HDFS | HealthApp | HPC | Mac |
-------------------------------------------------------------------------
No. unique words          |   874  | 2068| 3599 |    1512   | 510 | 2981|
No. unique characters     |   46   |  75 |  56  |     71    | 65  |  90 |
No. unique log lengths    |    9   | 114 |  59  |     55    | 50  | 186 |

Dataset                   |OpenStack | Spark | Windows | Combined | Industry |
------------------------------------------------------------------------------
No. unique words          |  1445    | 1970  |  1206   |   3123   |   4421   |
No. unique characters     |   72     |  70   |   82    |    91    |    92    |
No. unique log lengths    |   50     |  63   |   66    |   157    |   181    |
```

**Normalized table (Table V)**

```

Dataset                   | Apache | BGL | HDFS | HealthApp | HPC | Mac |
-------------------------------------------------------------------------
No. unique words          | 0.197  |0.467|0.814 |    0.342  |0.115|0.674|
No. unique characters     | 0.5    |0.815|0.608 |    0.771  |0.706|0.978|
No. unique log lengths    | 0.049  |0.629|0.325 |    0.303  |0.276|0.027|

Dataset                   | OpenStack | Spark | Windows | Combined | Industry |
-------------------------------------------------------------------------------
No. unique words          |  0.326    | 0.445 |  0.272  |   0.706  |     1    |
No. unique characters     |  0.782    | 0.760 |  0.891  |   0.989  |     1    |
No. unique log lengths    |  0.276    | 0.348 |  0.364  |   0.867  |     1    |
```

**Final values table (Table V)**

```
No. |   Metric                 | Sigma ^ 2 |
--------------------------------------------
1   |   No. unique words       |   0.278   |
2   |   No. unique characters  |   0.159   |
3   |   No. unique log lengths |   0.331   |

```

## (4.4) Mixing (Table VI)

In this section, we showcase how to reproduce Table VI, by showcasing how to reproduce the results for a particular dataset and method, namely for `Apache` and `AEL`. Specifically, we reproduce the following section of Table VI.

To get you started, please follow the steps displayed below (Step 1 through 4):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:mixing
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:mixing bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/mixing
```

**Step 4**: *Run experiment*

```
$ sh experiment_mixing_vi.sh -d "Apache" -m "AEL" -x
# (about 5m)
```

> `-d` specifies the dataset, `-m` the method, and `-x` if mixing is to be applied.
> 

```bash
# Usage: ./experiment_mixing_vi.sh [-d dataset] [-m method] [-x]
# Options:
#   -d: Dataset (dataset to be used)
#   -m: Method (log parsing method to test)
#   -x: Mixing (true if flagged)
```

For this experiment, fuzzing is not to be applied. At the end of running the commands above you should be able to reproduce the section corresponding to `Apache` and `AEL`. Similarly, for the other sections of the table, the arguments of the script need to be changed accordingly. For example, for reproducing the results for `Drain` on the `Apache` dataset, the following command needs to be run:

`$ sh experiment_mixing_table_vi.sh -d "Apache" -m "Drain" -x`

## (4.5) Mixing and fuzzing (Table VII)

Similarly to the workflow for reproducing Table VI, reproducing Table VII requires following the steps below. Specifically, we showcase how to reproduce the following section of Table VII (all other sections of the table follow a similar workflow).

To get you started, please follow the steps displayed below (Step 1 through 4):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:mixing
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:mixing bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/mixing_and_fuzzing
```

**Step 4**: *Run experiment*

```
$ sh experiment_fuzzing_vii.sh -d "Apache" -m "AEL" -x -f
```

> `-d` specifies the dataset, `-m` the method, `-x` if mixing is to be applied, and `-f` if fuzzing is to be applied.
> 

```bash
# Usage: ./experiment_fuzzing_vii.sh [-d dataset] [-m method] [-x] [-f]
# Options:
#   -d: Dataset (dataset to be used)
#   -m: Method (log parsing method to test)
#   -x: Mixing (true if flagged)
#   -f: Fuzzing (true if flagged)
```

At the end of running the commands above you should be able to reproduce the section corresponding to `Apache` and `AEL`. Similarly, for reproducing the other sections of the table, the arguments of the script need to be changed accordingly. For example, for reproducing the results for `Drain` on the `Apache` dataset, the following command needs to be run:

`$ sh experiment_fuzzing_vii.sh -d "Apache" -m "Drain" -x -f`

## (4.6) Unlabeled comparison (Table VIII)

In this section we provide instructions on how to reproduce Table VIII. Specifically, we showcase how to reproduce the following row of Table VIII (all other rows follow a similar workflow):

To get you started, please follow the steps displayed below (Step 1 through 4):
**Step 1**: *Pull the docker image*

```
$ docker pull spetrescu/log-parsing-evaluator:mixing
# (about 5min)
```

**Step 2**: *Start the image and bash shell*

```
$ docker run -it spetrescu/log-parsing-evaluator:mixing bash
```

**Step 3**: *Go to path for current experiment*

```
$ cd ~/automated_mixing_and_fuzzing
```

**Step 4**: *Run experiment*

```
$ sh experiment_automated_mixing_and_fuzzing_viii.sh -d "Apache"
```

> `-d` specifies the dataset to be used
> 

```bash
# Usage: ./experiment_automated_mixing_and_fuzzing_viii.sh [-d dataset]
# Options:
#   -d: Dataset (either Apache or HPC or BGL or Mac)
```

At the end of running the commands above you should be able to reproduce the section corresponding to `Apache`. Similarly, for reproducing the other rows of the table, the arguments of the script need to be changed accordingly. For example, for reproducing the results for `HPC`, the following command needs to be run:

`$ sh experiment_automated_mixing_and_fuzzing_viii.sh -d "HPC"`

# Citation

```python
@INPROCEEDINGS{petrescu2023issre,
author={Petrescu, Stefan and den Hengst, Floris and Uta, Alexandru and Rellermeyer, Jan S.},
booktitle={34th IEEE International Symposium on Software Reliability Engineering (ISSRE)}, 
title={Log Parsing Evaluation in the Era of Modern Software Systems}, 
year={2023}}
```


