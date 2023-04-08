from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, *args):
        pass


class Subject(ABC):
    @abstractmethod
    def register(self, observer: Observer):
        pass

    @abstractmethod
    def unregister(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self, *args):
        pass

