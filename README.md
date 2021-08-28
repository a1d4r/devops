# DevOps Labs

## Python app

<div align="center">

[![Python web application](https://github.com/a1d4r/devops/actions/workflows/app_python.yaml/badge.svg)](https://github.com/a1d4r/devops/actions/workflows/app_python.yaml)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![License](https://img.shields.io/github/license/a1d4r/devops)](https://github.com/a1d4r/devops/blob/master/LICENSE)

Simple python web application that shows current time in Moscow

</div>

## Installation

Go to the app directory
```bash
cd app_python
```

Install dependencies with `Poetry`:
```bash
poetry add devops
```
or using `pip`:
```bash
pip install -U devops
```

### Run
```shell
make up
```
or using Docker:
```shell
 docker run --rm -p 8000:8000 a1d4r/devops-python-app:latest
```

### Unit tests
```
make test
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
