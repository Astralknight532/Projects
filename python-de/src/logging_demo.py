import logging

logging.basicConfig(
    level = logging.ERROR, # controls logging severity
    format = "%(asctime)s - %(levelname)s - %(message)s" # format of log messages
)

# Demonstrating the 5 different log levels (levels of severity)
# the debug level doesn't actually show in the console/command prompt
# because when you configure logging.INFO (or anything worse in severity),
# any logs lower in severity than the configured severity level will not be shown
# and only logs at the same severity or higher will be shown
logging.debug("Pipeline Started") # lowest severity
logging.info("Pipeline Started")
logging.warning("Pipeline Started")
logging.error("Pipeline Started")
logging.critical("Pipeline Started") # highest severity

try:
    amount = "100"
    total = int(amount) + 50
    logging.info(f"Total amount calculated: {total}")
except Exception as e:
    logging.error(f"Pipeline failed: {e}")

logging.info("Pipeline finished.")