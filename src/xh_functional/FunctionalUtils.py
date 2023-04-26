from typing import TypeVar, Generic, Callable

T = TypeVar('T')
R = TypeVar('R')


class Scope(Generic[T]):
    def __init__(self, obj: T):
        self._obj = obj

    def apply(self, f: Callable[[T], T]) -> 'Scope[T]':
        return Scope(f(self._obj))

    def map(self, f: Callable[[T], R]) -> 'Scope[R]':
        return Scope(f(self._obj))

    def get(self) -> 'T':
        return self._obj
