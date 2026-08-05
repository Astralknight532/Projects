import logging

logging.basicConfig(
    level = logging.INFO, # controls logging visibility
    format = "%(asctime)s - %(levelname)s - %(message)s" # format of log messages
)

# Demonstrating the 5 different log levels
# the debug level doesn't actually show in the console/command prompt
# because when you configure logging.info (or anything higher in visibility),
# anything lower in visibility will not be shown
logging.debug("Pipeline Started")
logging.info("Pipeline Started")
logging.warning("Pipeline Started")
logging.error("Pipeline Started")
logging.critical("Pipeline Started")

try:
    amount = "100"
    total = int(amount) + 50
    logging.info(f"Total amount calculated: {total}")
except Exception as e:
    logging.error(f"Pipeline failed: {e}")

logging.info("Pipeline finished.")