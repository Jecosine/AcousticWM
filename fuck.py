import numpy as np
import os

class WaveEncoder:
  def __init__(self, fname):
    with open(fname, 'rb') as f:
      content = f.read()
      