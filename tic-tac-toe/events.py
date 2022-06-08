from pyclbr import Function
from typing import Dict, List

class EventEmitter:

  def __init__(self):
    self.events: Dict[str, List[Function]] = {}

  def on(self, event_name, callback: Function):
    if self.events.get(event_name) is not None:
      self.events[event_name].append(callback)
    else:
      self.events[event_name] = [callback]

  def emit(self, event_name: str, *args):
    if self.events.get(event_name) is not None:
      for callback in self.events[event_name]:
        callback(*args)


eventBus = EventEmitter()