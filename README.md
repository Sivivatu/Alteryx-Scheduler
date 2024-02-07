# Alteryx-Scheduler

Alteryx-Scheduler is a project that enables scheduling of an Alteryx Server using the APIs. The scheduling functionality is designed to be flexible, allowing for conditional running and starting of a pipeline anywhere in the stream.

## Features

- Integration with FastAPI for the backend
- Utilizes HTMX for dynamic webpages

## Getting Started

To get started with Alteryx-Scheduler, follow these steps:

1. Clone the repository.
2. Install the required dependencies.
3. Configure the Alteryx Server API credentials.
4. Start the FastAPI server.
5. Access the webpages and schedule your Alteryx pipelines.

For detailed instructions, please refer to the [documentation](/docs).

An example folder structure for the server:

```bash
.
├── app
│   ├── __init__.py
│   ├── main.py
│   └── database
│   │   ├── __init__.py
│   │   ├── database.py
│   │   └── models.py
│   └── routers
│   │   ├── __init__.py
│   │   └── alt_schedules.py
│   └── modules
│   │   ├── __init__.py
│   │   └── schedules.py
│   └── internal
│       ├── __init__.py
│       └── auth.py
```

## Using Alembic

The current process requires that the dev container is run as root to allow alembic to work correctly.

## Contributing

Contributions are welcome! If you would like to contribute to Alteryx-Scheduler, please follow the guidelines outlined in the [CONTRIBUTING.md](/CONTRIBUTING.md) file.

## License

Alteryx-Scheduler is licensed under the [MIT License](/LICENSE).


