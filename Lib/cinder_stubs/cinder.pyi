from types import CodeType, ModuleType
from typing import Callable, List, Optional, Tuple, Type, TypeVar

class _PatchEnabledDescr:
    def __get__(self, inst: StrictModule, typ: Type[StrictModule]) -> bool: ...

class StrictModule(ModuleType):
    __patch_enabled__: _PatchEnabledDescr
    def __init__(self, d: Mapping[str, object], enable_patching: bool) -> None: ...
    def patch(self, name: str, value: object) -> None: ...
    def patch_delete(self, name: str) -> None: ...

TType = TypeVar(TType, bound=Type[object])

def freeze_type(_type: TType, /) -> TType: ...
def warn_on_inst_dict(_type: TType, /) -> TType: ...
def _set_qualname(_code: CodeType, _name: str, /) -> None: ...
def warn_on_inst_dict(_type: TType, /) -> TType: ...

TImmutableLoggerType = Callable[List[Tuple[int, str, object]], None]

def set_immutable_warn_handler(_logger: Optional[TImmutableLoggerType], /) -> None: ...
def get_immutable_warn_handler() -> Optional[TImmutableLoggerType]: ...
def raise_immutable_warning(_code: int, _msg: str, _obj: object, /): ...
def flush_immutable_warnings(): ...
def watch_sys_modules(): ...
