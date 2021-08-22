# Docker best practices

- Use linter [hadolint](https://hadolint.github.io/hadolint/)
- Order layers from the less frequently changed (to ensure the build cache is reusable) to the more frequently changed
- Use lightweight `python:3.9-slim-buster` as base image
- Build argument `INSTALL_DEV` indicating whether to install development packages (Poetry separates them)
- Use `.dockerignore` not to include unwanted files
- Use `EXPOSE` to indicate which ports docker image uses.
