from abc import abstractmethod, ABC


class Engine(ABC):
    @staticmethod
    def start_engine():
        print("Start engine")

    @staticmethod
    @abstractmethod
    def stop_engine():
        pass

    @abstractmethod
    def drive(self):
        pass


Engine.start_engine()


class Car(Engine):
    def cardrive(self):
        Engine.start_engine()

    def stop_engine(self):
        print("Stop engine")
        #Engine.stop_engine()

    def drive(self):
        print("Driving")


c = Car()
c.cardrive()
c.stop_engine()
#Engine.stop_engine()

