"""
This module is the main module of the ACC program.

Running this module will start up the ACC and run the webserver for the user
interface.
"""
from multiprocessing import Process, Queue

import acc
import api

def main():
    """
    The main function of the ACC program. It starts up the ACC and runs the
    webserver for the user interface.
    """
    command_queue = Queue()

    listener_process = Process(target=api.run, args=(command_queue, True))

    listener_process.start()

    while True:
        print(command_queue.get())

    listener_process.join()

if __name__ == "__main__":
    main()
