import time
import os
from azure.messaging.webpubsubservice import WebPubSubServiceClient
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from dotenv import load_dotenv

load_dotenv()


def message_object(path):
    return {
        "file_name": os.path.basename(path),
        "folder": os.path.dirname(path),
        "path": path,
    }


class EventHandler(FileSystemEventHandler):
    def __init__(self, service) -> None:
        self.service = service

    def on_created(self, event):
        message = message_object(event.src_path)
        if event.is_directory:
            print("Directory created:", event.src_path)
        else:
            print("File created:", message["file_name"])
            res = self.service.send_to_all(message=message)
            print(res)

    def on_deleted(self, event):
        message = message_object(event.src_path)
        if event.is_directory:
            print("Directory deleted:", event.src_path)
        else:
            print("File deleted:", message["file_name"])

    def on_modified(self, event):
        message = message_object(event.src_path)
        if event.is_directory:
            print("Directory modified:", event.src_path)
        else:
            print("File modified:", message["file_name"])


if __name__ == "__main__":

    service = WebPubSubServiceClient.from_connection_string(
        os.getenv("CONNECTION_STRING"), hub="Hub1"
    )

    event_handler = EventHandler(service)
    observer = Observer()
    observer.schedule(event_handler, "./camera", recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
