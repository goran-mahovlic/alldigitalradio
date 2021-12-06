from alldigitalradio.io.ecp5 import ECP5Serdes
from nmigen.build import Resource, Pins, Attrs

def load():
    from nmigen_boards.ulx4m import ULX4MPlatform
    return (ULX4MPlatform, ECP5Serdes)
