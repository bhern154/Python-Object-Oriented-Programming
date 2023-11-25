"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Initialize a new generator"""
        self.start = start
        self.next = start

    def generate(self):
        """Generates a new serial number by incementing 1 every time"""
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Resets the serial number to the original start number"""
        self.next = self.start
    
    def __repr__(self):
        """returns representation of SerialGenerator class"""
        return f"<SerialGenerator start={self.start} next={self.next}>"