from typing import List, Optional
from diffsync import DiffSyncModel

class caDev(DiffSyncModel):
    _modelname = "ca_dev"
    _identifiers = ("@id",)
    _shortname = ()
    _attributes = ("$")
    _children = {"device": "devices"}

    id: str
    name: str

    def load(self):
        # Store an individual object
        site = self.site(name="nyc")
        self.add(site)

        # Store an object and define it as a child of another object
        device = self.device(name="rtr-nyc", role="router", site_name="nyc")
        self.add(device)
        site.add_child(device)
        site.update()
