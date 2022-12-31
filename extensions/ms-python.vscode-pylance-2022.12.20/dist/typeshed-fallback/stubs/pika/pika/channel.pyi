from _typeshed import Incomplete, Self
from collections.abc import Callable
from typing_extensions import Final

from .callback import CallbackManager
from .connection import Connection
from .data import _ArgumentMapping
from .exchange_type import ExchangeType
from .frame import Method
from .spec import Basic, BasicProperties

LOGGER: Incomplete
MAX_CHANNELS: int

class Channel:
    CLOSED: Final[int]
    OPENING: Final[int]
    OPEN: Final[int]
    CLOSING: Final[int]
    channel_number: int
    callbacks: CallbackManager
    connection: Connection
    flow_active: bool
    def __init__(self: Self, connection: Connection, channel_number: int, on_open_callback: Callable[[Self], object]) -> None: ...
    def __int__(self) -> int: ...
    def add_callback(self, callback, replies, one_shot: bool = ...) -> None: ...
    def add_on_cancel_callback(self, callback) -> None: ...
    def add_on_close_callback(self, callback) -> None: ...
    def add_on_flow_callback(self, callback) -> None: ...
    def add_on_return_callback(self, callback) -> None: ...
    def basic_ack(self, delivery_tag: int = ..., multiple: bool = ...): ...
    def basic_cancel(self, consumer_tag: str = ..., callback: Callable[[Method], object] | None = ...) -> None: ...
    def basic_consume(
        self,
        queue: str,
        on_message_callback: Callable[[Channel, Basic.Deliver, BasicProperties, bytes], object],
        auto_ack: bool = ...,
        exclusive: bool = ...,
        consumer_tag: str | None = ...,
        arguments: _ArgumentMapping | None = ...,
        callback: Callable[[Method], object] | None = ...,
    ) -> str: ...
    def basic_get(self, queue, callback, auto_ack: bool = ...) -> None: ...
    def basic_nack(self, delivery_tag: int = ..., multiple: bool = ..., requeue: bool = ...): ...
    def basic_publish(
        self, exchange: str, routing_key: str, body: str | bytes, properties: BasicProperties | None = ..., mandatory: bool = ...
    ) -> None: ...
    def basic_qos(
        self, prefetch_size: int = ..., prefetch_count: int = ..., global_qos: bool = ..., callback: Incomplete | None = ...
    ): ...
    def basic_reject(self, delivery_tag: int = ..., requeue: bool = ...): ...
    def basic_recover(self, requeue: bool = ..., callback: Incomplete | None = ...): ...
    def close(self, reply_code: int = ..., reply_text: str = ...) -> None: ...
    def confirm_delivery(self, ack_nack_callback, callback: Incomplete | None = ...) -> None: ...
    @property
    def consumer_tags(self): ...
    def exchange_bind(
        self, destination, source, routing_key: str = ..., arguments: Incomplete | None = ..., callback: Incomplete | None = ...
    ): ...
    def exchange_declare(
        self,
        exchange: str,
        exchange_type: ExchangeType | str = ...,
        passive: bool = ...,
        durable: bool = ...,
        auto_delete: bool = ...,
        internal: bool = ...,
        arguments: _ArgumentMapping | None = ...,
        callback: Callable[[Method], object] | None = ...,
    ): ...
    def exchange_delete(
        self, exchange: str | None = ..., if_unused: bool = ..., callback: Callable[[Method], object] | None = ...
    ): ...
    def exchange_unbind(
        self,
        destination: Incomplete | None = ...,
        source: Incomplete | None = ...,
        routing_key: str = ...,
        arguments: Incomplete | None = ...,
        callback: Incomplete | None = ...,
    ): ...
    def flow(self, active, callback: Incomplete | None = ...) -> None: ...
    @property
    def is_closed(self): ...
    @property
    def is_closing(self): ...
    @property
    def is_open(self): ...
    @property
    def is_opening(self): ...
    def open(self) -> None: ...
    def queue_bind(
        self,
        queue,
        exchange,
        routing_key: Incomplete | None = ...,
        arguments: Incomplete | None = ...,
        callback: Incomplete | None = ...,
    ): ...
    def queue_declare(
        self,
        queue,
        passive: bool = ...,
        durable: bool = ...,
        exclusive: bool = ...,
        auto_delete: bool = ...,
        arguments: Incomplete | None = ...,
        callback: Incomplete | None = ...,
    ): ...
    def queue_delete(self, queue, if_unused: bool = ..., if_empty: bool = ..., callback: Incomplete | None = ...): ...
    def queue_purge(self, queue, callback: Incomplete | None = ...): ...
    def queue_unbind(
        self,
        queue,
        exchange: Incomplete | None = ...,
        routing_key: Incomplete | None = ...,
        arguments: Incomplete | None = ...,
        callback: Incomplete | None = ...,
    ): ...
    def tx_commit(self, callback: Incomplete | None = ...): ...
    def tx_rollback(self, callback: Incomplete | None = ...): ...
    def tx_select(self, callback: Incomplete | None = ...): ...

class ContentFrameAssembler:
    def __init__(self) -> None: ...
    def process(self, frame_value): ...
