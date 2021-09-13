## Metrics
### Steps
- Mofify python app so it exposes `metrics` endpoint with HTTP requests metrics
- Add Prometheus to docker container
- Create config for Prometheus to scrape metrics from web app, Loki and Prometheus itself
- Run and check Prometheus targets: [Screenshot](screenshots/prometheus_targets.png)
- Set up Graphana dashboard for Loki and Prometheus: [Screenshot Prometheus](screenshots/prometheus_dashboard.png), [Screenshot Loki](screenshots/loki_dashboard.png) 
- Set up dashboard for Python app: [Screenshot](screenshots/web_dashboard.png)
- Add log rotation and memory limits for containers

### Best practices
- Follow naming convention for application metrics
- Install ready-to-use dashboards in Graphana