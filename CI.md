## Github Actions
- Two separate jobs: lint_test, build  
- Use env vars in yaml file instead of hardcoding
- Use SHA to indicate version for 3rd party actions
- Use secrets envs for credentials
- Use ready-to-use docker actions
- Cache poetry installation
- Cache application dependencies
- Cache docker layers
- Build and push only on master branch

## Jenkins
- Use declarative pipeline
- Use env vars instead of hardcoding
- Use docker agent
- Cleanup workspace
- Three stages: install dependencies, lint&test, build&push
- Linting and testing runs in parallel
- Cache python dependencies