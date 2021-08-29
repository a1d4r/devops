pipeline {

    environment {
        POETRY_VERSION = '1.1.8'
        APP_PATH = './app_python'
        CODE = 'app tests'
        TESTS = 'tests'
        IMAGE_NAME = 'devops-python-app'
        DOCKER_HUB = credentials('docker-hub')
    }

    agent { 
        docker { 
            image 'python:3.9-slim-buster'
            args '-u root -v $HOME/.cache:/root/.cache'
        } 
    }

    stages {
        stage('deps') {
            steps {
                dir('$APP_PATH') {
                    sh 'python -m pip install poetry'
                    sh 'poetry install --no-interaction --no-root'
                    sh 'poetry run mypy --install-types --namespace-packages --explicit-package-bases --non-interactive ${CODE}'
                }
            }
        }
        stage('lint-test') {
            steps {
                parallel (
                    'codestyle': {
                        dir('$APP_PATH') {
                            sh 'poetry run isort --diff --check-only --settings-path pyproject.toml ${CODE}'
                            sh 'poetry run black --diff --check --config pyproject.toml ${CODE}'
                            sh 'poetry run darglint --verbosity 2 ${CODE}'
                        }
                    },
                    'lint': {
                        dir('$APP_PATH') {
                            sh 'poetry run pylint --rcfile=.pylintrc ${CODE}'
                            sh 'poetry run mypy --config-file pyproject.toml --namespace-packages --explicit-package-bases ${CODE}'
                        }
                    }, 
                    'safety': {
                        dir('$APP_PATH') {
                            sh 'poetry check'
                            sh 'poetry run safety check --full-report'
                            sh 'poetry run bandit -s B101 --recursive ${CODE}'
                        }
                    },
                    'test': {
                        dir('$APP_PATH') {
                            sh 'poetry run python -m pytest --cov=app ${CODE}'
                        }
                    }
                )
                
            }
        }
        stage('build') {
            agent none
            steps {
                dir('$APP_PATH') {
                    script {
                        def image = docker.build('${env.DOCKER_HUB_USR}/${env.IMAGE_NAME}:latest', '-f ./docker/Dockerfile .')
                        docker.withRegistry('', '${env.DOCKER_HUB_PSW}') {
                            image.push()
                        }
                    }
                }
            }
        }
    }
}