[![gtvf](https://circleci.com/gh/gtvf/poll-manager.svg?style=svg)](https://app.circleci.com/pipelines/github/gtvf/poll-manager)

### Run backend

1. Make sure following env vars set in your host system:
   `$POSTGRES_PASSWORD`, `$POSTGRES_USER`, `$POSTGRES_DB`, `$POSTGRES_URL`, `$POSTGRES_PORT`
2. Run local server
    ```shell
    $ cd poll-manager
    $ docker-compose up -d --build
    ```
3. Navigate to Swagger UI: http://0.0.0.0:8000/docs
