# encoding: UTF-8
"""

"""
from __future__ import print_function


from heron import Component, Event


class hello(Event):
    """hello Event"""


class terminate(Event):
    """terminate Event"""


class eventObj(object):
    def __init__(self):
        self.a = "a"
        self.b = "b"


class App(Component):

    def hello(self, obj):
        """Hello Event Handler"""

        print(obj.a)
        print("Hello World! and")

    def started(self):
        """Started Event Handler

        This is fired internally when your application starts up
        and can be used to trigger events that only occur once
        during startup.
        """

        print("i am here")

        obj = eventObj()
        obj.a = "b"
        obj.b = "a"

        self.fire(hello(obj))  # Fire hello Event
        self.fire(terminate())

    def terminate(self):
        raise SystemExit(0)  # Terminate the Application

app = App()

while len(app):
    app.flush()

app.run()

