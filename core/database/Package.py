"""
This is the class which denotes a package and has all details about it
"""


class Package:

    """
    Parameters:
        tracking_number: tracking number for this package (String)
        service: Service which is delivering this package eg. USPS, Fedex etc. (String)
        status: Status of the package (String)
    """
    def __init__(self, tracking_number, service, status):
        self.tracking_number = tracking_number
        self.service = service
        self.status = status

    def get_tracking_number(self):
        return self.tracking_number

    def get_service(self):
        return self.service

    def get_status(self):
        return self.status