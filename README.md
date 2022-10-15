# Python-Prometheus-Grafana-Chaos

The main objective of this project is to create a simple Python service example that exports metrics to Prometheus which is a standalone open source project that monitors and alerts systems and Grafana.

### Mains Tools
- Docker [Install](https://docs.docker.com/get-docker/)
- Prometheus
- Grafana
- Windows Subsystem for Linux (WSL) if you are using windows [Install](https://learn.microsoft.com/en-us/windows/wsl/install)
**Note:** If on Windows also need to configure your docker to talk with your WSL distro [Instructions](https://docs.docker.com/desktop/windows/wsl/)

### Technical Overview

You will need Docker installed: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)

To follow the next steps and build and run the image locally you just need to use the following command:
```bash
docker-compose build --no-cache
```
```bash
docker-compose up
```

### How it Works

At first, make some reqeust several times using the following link `http://localhost:5000`, then you be able to see changes in the metrics `http://localhost:5000/metrics`.

After that, you can navigate to grafana's Dashboard via the link `http//localhost:3000` and upload the datasource and dashboard configuration using the JSO files. Or you can use Grafana's Dashboard API to create a new dashboard and datasource using the following requests:

- Enable datasource:
  1. Change directory to `grafana-configuration`
      ```
      cd grafana-configuration
      ```
  2. Hit the grafana `/api/datasources` endpoint with our `datasources.json` payload to configure grafana to pick up our prometheus metrics
      ```
      curl --request POST http://localhost:3000/api/datasources --header "Content-Type: application/json" -d @datasources.json
      ```

- Create Dashboard:
  1. Change directory to `grafana-configuration`
      ```
      cd grafana-configuration
      ```
  2. Hit the grafana `/api/dashboards/db` endpoint with our `dashboard.json` payload to configure grafana to pick up our prometheus metrics
      ```
      curl --request POST http://localhost:3000/api/dashboards/db --header "Content-Type: application/json" -d @dashboard.json
      ```

For more information you can access the [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/http_api/dashboard/).

After all these actions, you should be able to access the Grafana Dashboard that display some graphs and metrics related to the Flask Web Application that was created.

### Help and Resources

You can read more on:

- [Docker Documentation](https://docs.docker.com/get-started/overview/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [Grafana Dashboard API](https://grafana.com/docs/grafana/latest/http_api/dashboard/)
- [Grafana Documentation](https://grafana.com)
- [Prometheus Documentation](http://prometheus.io)
- [Prometheus Python Client](https://github.com/prometheus/client_python)

### Authors
* Source: [https://github.com/samhaque/python-prometheus-grafana-chaos](https://github.com/samhaque/python-prometheus-grafana-chaos)
* [@SamiulHaque](https://github.com/samhaque)