CHART_NAME := web
CHART_PATH := ./web-app

.PHONY: up
up:
	helm install $(CHART_NAME) $(CHART_PATH)

.PHONY: down
down:
	helm uninstall $(CHART_NAME)

.PHONY: debug
debug:
	helm install --dry-run $(CHART_NAME) $(CHART_PATH)