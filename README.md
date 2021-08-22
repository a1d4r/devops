# DevOps Labs

## Python app

<div align="center">

[comment]: <> ([![Build status]&#40;https://github.com/a1d4r/devops/workflows/build/badge.svg?branch=master&event=push&#41;]&#40;https://github.com/a1d4r/devops/actions?query=workflow%3Abuild&#41;)

[comment]: <> ([![Python Version]&#40;https://img.shields.io/pypi/pyversions/devops.svg&#41;]&#40;https://pypi.org/project/devops/&#41;)

[comment]: <> ([![Dependencies Status]&#40;https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg&#41;]&#40;https://github.com/a1d4r/devops/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot&#41;)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/a1d4r/devops/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/a1d4r/devops/releases)
[![License](https://img.shields.io/github/license/a1d4r/devops)](https://github.com/a1d4r/devops/blob/master/LICENSE)

Simple python web application that shows current time in Moscow

</div>

## Installation

```bash
cd app_python
```

```bash
pip install -U devops
```

or install with `Poetry`

```bash
poetry add devops
```

### Run
```shell
make up
```
or using Docker:
```shell
 docker run --rm -p 8000:8000 a1d4r/devops-python-app:latest
```

### Docker
Build
```shell
make docker-build
```
Remove
```shell
make docker-remove
```


### Makefile usage

[`Makefile`](https://github.com/a1d4r/devops/blob/master/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

<details>
<summary>4. Code security</summary>
<p>

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

</p>
</details>

<details>
<summary>5. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>6. Tests</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>7. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy && make check-safety
```

</p>
</details>

<details>
<summary>8. Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/a1d4r/devops/tree/master/docker).

</p>
</details>

<details>
<summary>9. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Or to remove pycache, build and docker image run:

```bash
make clean-all
```

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/a1d4r/devops)](https://github.com/a1d4r/devops/blob/master/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/a1d4r/devops/blob/master/LICENSE) for more details.

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/python--package--template-%F0%9F%9A%80-brightgreen)](https://github.com/TezRomacH/python-package-template)

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)
