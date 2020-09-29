#!/usr/bin/env python3

__author__ = "Humberto Hidalgo"
__version__ = "0.1.0"

import os
import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class watcher():
    """Watcher \n
    Watcher watches a path and returns an object when a file is done being created. \n
    To use: \n
    Initiate watcher() \n
    Then run watcher.run(path) \n
    Escape with control+c."""

    def __init__(self):
        self.observer = Observer()


    def run(self, path):

        if os.path.exists(path):
            print(f'Running watcher on {path}')

            handler = event_handler()
            self.observer.schedule(handler, path, recursive=True)
            self.observer.start()
            try:
                while True:
                    time.sleep(1)
            except:
                self.observer.stop()
            self.observer.join()

        else:
            print('Check path provided, exiting.')
            raise SystemExit()

class event_handler(FileSystemEventHandler):

    @staticmethod
    def on_created(event):
        # Wait for growing file
        file_size = -1
        while file_size != os.path.getsize(event.src_path):
            file_size = os.path.getsize(event.src_path)
            time.sleep(5)

# Remove print and add a return of a json object that has Name, Event Type, and location.
        if event.event_type == 'created':
            object = {}
            object['event_type'] = event.event_type
            object['filename'] = os.path.basename(event.src_path)
            object['location'] = event.src_path

            #return object
            print(object)
