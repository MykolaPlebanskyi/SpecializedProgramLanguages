import os
import unittest

from labwork_6.interface import Interface

if __name__ == '__main__':

    interface = Interface()
    suite = interface.user_interface()
    unittest.TextTestRunner().run(suite)
