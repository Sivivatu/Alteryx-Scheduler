import json

# from app.routers import alt_schedules
import logging.config

logger = logging.getLogger(__name__)
log_config_file = (
    "/workspaces/Alteryx-Scheduler/app/app_logger/logging_configs/log_config.json"
)
with open(log_config_file) as f_in:
    config = json.load(f_in)
    logging.config.dictConfig(config)

logger.info("Starting FastAPI app")
