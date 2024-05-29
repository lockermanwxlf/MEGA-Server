from threading import Event
from typing import Any
from mega import MegaListener

class Listener(MegaListener):
    def __init__(self, event: Event, logging: bool):
        self.event = event
        self.logging = logging
        super(Listener, self).__init__()

    def onRequestStart(self, api, request):
        if self.logging:
            print("Request Started:", request, flush=True)
            
    def onRequestFinish(self, api, request, e):
        if self.logging:
            print("Request Finished:", request, "- Error:", e, flush=True)
        self.event.set()
    
    def onTransferStart(self, api, transfer):
        if self.logging:
            print("Transfer Started:", transfer, flush=True)
            
    def onTransferFinish(self, api, transfer, error):
        if self.logging:
            print("Transfer Finished", transfer, "- Error:", error, flush=True)

class Executor:
    def __init__(self, logging: bool = False) -> None:
        self.__event = Event()
        self.listener = Listener(self.__event, logging)
        
    def execute(self, func, *args):
        print("Executing", flush=True)
        self.__event.clear()
        func(*args)
        self.__event.wait()
        print("Done", flush=True)
        
    def __call__(self, func, *args: Any) -> Any:
        self.__event.clear()
        func(*args)
        self.__event.wait()