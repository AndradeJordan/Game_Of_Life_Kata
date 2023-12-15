import abc

class game(abc.ABC):
    @abc.abstractproperty
    def description(self):
        pass

    @abc.abstractproperty
    def strategie(self):
        pass