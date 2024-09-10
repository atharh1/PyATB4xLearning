from abc import abstractmethod, ABC


class Browser(ABC):

    @abstractmethod
    def start_browser(self):
        pass
    @abstractmethod
    def close_browser(self):
        pass

class TC(Browser):
     def start_browser(self):
         print("Start browser")

     def close_browser(self):
         print("close browser")

t=TC()
t.start_browser()
t.close_browser()

