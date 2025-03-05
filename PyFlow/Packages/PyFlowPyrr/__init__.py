import os
from PyFlow.Core.PackageBase import PackageBase

class PyFlowPyrr(PackageBase):
    """Pyrr pyflow package
    """	    
    def __init__(self):
        super(PyFlowPyrr, self).__init__()
        self.analyzePackage(os.path.dirname(__file__))
