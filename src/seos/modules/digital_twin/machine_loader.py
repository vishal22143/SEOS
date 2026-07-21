from .kubota_b2441n import KubotaB2441N


class MachineLoader:

    def __init__(self,root):

        self.root=root

    def kubota(self):

        return KubotaB2441N(self.root)
