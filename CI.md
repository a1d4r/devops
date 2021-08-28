## Github Actions best practices
- Two separate jobs: lint_test, build  
- Use env vars in yaml file instead of hardcoding
- Use SHA to indicate version for 3rd party actions
- Use secrets envs for credentials
- Use ready-to-use docker actions
- Cache poetry installation
- Cache application dependencies
- Cache docker layers
