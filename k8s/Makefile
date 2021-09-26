CHART_NAME := web
CHART_PATH := ./web-app
SECRETS_PATH := ./secrets.yaml

.PHONY: up
up:
	helm secrets install $(CHART_NAME) $(CHART_PATH) -f $(SECRETS_PATH)

.PHONY: down
down:
	helm uninstall $(CHART_NAME)

.PHONY: debug
debug:
	helm secrets install --dry-run $(CHART_NAME) $(CHART_PATH) -f $(SECRETS_PATH)