## Logging
### Steps
- Create docker-compose with `monitoring` network
- Put web app, Promtail, Loki, Graphana containers into the network
- Create configuration for promtail to look for logs of the system and docker containers
- Specify tags for docker container in the logging section and promtail config
- Run docker-compose, setup data source for Loki in Graphana: [Screenshot](screenshots/loki_data_source.png)
- Check available labels for Loki: [Screenshot](screenshots/loki_containers_logs.png)
- Check if there is logs for web app: [Screenshot](screenshots/loki_web_logs.png)

### Best practices
Used: 
- Create labels for docker container and image names
- Define network in docker-compose instead of using a default one
- Limit number of logs for containers in docker-compose 

Aware of:
- Static labels are good
- Use dynamic labels sparingly
- Label values must always be bounded
- Be aware of dynamic labels applied by clients
- Logs must be in increasing time order per stream