from typing import Any

def pack(structure: Any, data: Any) -> Any: ...
def unpack(structure: Any, data: Any) -> Any: ...
def chunk(data: Any, index: Any) -> Any: ...
def from_pgraster(data: Any) -> Any: ...
def to_pgraster(rast: Any) -> Any: ...