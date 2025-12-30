import pandas as pd

def attach_segments(rfm, labels, name):
    rfm[name] = labels
    return rfm
