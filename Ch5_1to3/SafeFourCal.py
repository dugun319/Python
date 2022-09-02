from MoreFourCal import MoreFourCal

class SafeFourCal(MoreFourCal):

    
    def div(self):
        if self.int2 == 0:
            return 0
        else:
            return self.int1 / self.int2

