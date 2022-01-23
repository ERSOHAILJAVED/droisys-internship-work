
class RailwayForm:

        def printData(self):
            print(f"Name is {self.name}")
            print(f"Train is {self.train}")

javedApplication = RailwayForm()
javedApplication.name = "Javed"
javedApplication.train = "Rajdhani Express"
javedApplication.printData()