pipeline {

    environment {
        APP_PATH = './app_python'
        CODE = 'app tests'
        TESTS = 'tests'
    }

    agent { docker { image 'python:3.9-slim-buster' } }

    stages {
        stage('deps') {
            steps {
                sh 'cd ${APP_PATH}'
                sh 'curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -'
                sh 'poetry install --no-interaction --no-root'
                sh 'poetry run mypy --install-types --namespace-packages --explicit-package-bases --non-interactive ${{ env.CODE }}'
            }
        }
        stage('lint-test') {
            steps {
                parallel (
                    'codestyle': {
                        sh 'poetry run isort --diff --check-only --settings-path pyproject.toml ${CODE}'
                        sh 'poetry run black --diff --check --config pyproject.toml ${CODE}'
                        sh 'poetry run darglint --verbosity 2 ${CODE}'
                    }
                    'lint': {
                        sh 'poetry run pylint --rcfile=.pylintrc ${CODE}'
                        sh 'poetry run mypy --config-file pyproject.toml --namespace-packages --explicit-package-bases ${CODE}'
                    }, 
                    'safety': {
                        sh 'poetry check'
                        sh 'poetry run safety check --full-report'
                        sh 'poetry run bandit -s B101 --recursive ${CODE}'
                    }
                    'test': {
                        sh 'poetry run python -m pytest --cov=app ${CODE}'
                    }
                )
            }
        }
    }
}