from datetime import datetime

LOG_FILE = "sortify.log"


def log_message(message: str) -> None:
    timestamp = datetime.now().strftime(
        "%d/%m/%Y, %H:%M:%S"
    )

    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(
            f"[{timestamp}] {message}\n"
        )



def end_session():
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write("\n\n\n")