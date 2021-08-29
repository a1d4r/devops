pipeline {

    environment {
        POETRY_VERSION = '1.1.8'
        APP_PATH = './app_python'
        CODE = 'app tests'
        TESTS = 'tests'
        IMAGE_NAME = 'devops-python-app'
    }

    agent { 
        docker { 
            image 'python:3.9-slim-buster'
            args '-u root -v $HOME/.local:/usr/local/bin/ -v $HOME/.cache:/root/.cache'
        } 
    }

    stages {
        stage('deps') {
            steps {
                sh '''
                    cd $APP_PATH
                    find . -mindepth 1 -maxdepth 1 -exec mv -t .. -- {} +
                '''
                sh 'pip install poetry'
                sh 'poetry install --no-interaction --no-root'
                sh 'poetry run mypy --install-types --namespace-packages --explicit-package-bases --non-interactive ${CODE}'
            }
        }
        stage('lint-test') {
            steps {
                parallel (
                    'codestyle': {
                        sh 'poetry run isort --diff --check-only --settings-path pyproject.toml ${CODE}'
                        sh 'poetry run black --diff --check --config pyproject.toml ${CODE}'
                        sh 'poetry run darglint --verbosity 2 ${CODE}'
                    },
                    'lint': {
                        sh 'poetry run pylint --rcfile=.pylintrc ${CODE}'
                        sh 'poetry run mypy --config-file pyproject.toml --namespace-packages --explicit-package-bases ${CODE}'
                    }, 
                    'safety': {
                        sh 'poetry check'
                        sh 'poetry run safety check --full-report'
                        sh 'poetry run bandit -s B101 --recursive ${CODE}'
                    },
                    'test': {
                        sh 'poetry run python -m pytest --cov=app ${CODE}'
                    }
                )
            }
        }
        stage('build') {
            steps {
                script {
                    def image = docker.build("${env.IMAGE_NAME}:latest")
                    image.push()
                }
            }
        }
    }
}