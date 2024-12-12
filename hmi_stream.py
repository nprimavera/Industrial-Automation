
import os
import asyncio
import tornado.web
from file_watcher import FileWatcher
 

# Hyper params
# Location of atomically created stream file:
IMG_PATH = os.environ['XDG_RUNTIME_DIR'] + '/robot_stream.jpg'
# Interval between frames to be streamed remotely:
POLL_DELAY = 0.01
# These are the hyper params that tornado needs to handle events:
CONTENT_TYPE = 'multipart/x-mixed-replace;boundary=image-boundary'
BOUNDARY = b'--image-boundary\r\n'
JPEG_HEADER = b'Content-Type: image/jpeg\r\n\r\n'


"""
NOTE:
    1. We make a class to handle events.
    2. We use async keyword, meaning that the function should be asynchrounous.
    3. Asynchronous means it can pause its execution by 'await'
    4. 'await' lets other events to be exectued or handled.
"""

# Event handler object
class EventHandler(tornado.web.RequestHandler):
    async def get(self):
        self.set_header('Content-Type', CONTENT_TYPE)
        watcher = FileWatcher(IMG_PATH)
        while True:
            if watcher.has_changed():
                img_bytes = open(IMG_PATH, 'rb').read()
                self.write(BOUNDARY + JPEG_HEADER + img_bytes)
                self.flush()
            await asyncio.sleep(POLL_DELAY)


async def main():
    app = tornado.web.Application([('/', EventHandler)])
    app.listen(9000)
    shutdown_event = asyncio.Event()
    await shutdown_event.wait()


asyncio.run(main())
