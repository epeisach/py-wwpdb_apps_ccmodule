class InvalidLigandId(Exception):
    def __init__(self, lig_id=None):
        if not lig_id or lig_id == '':
            self.message = 'Missing ligand ID'
        else:
            self.message = 'Invalid ligand ID provided ({})'.format(lig_id)

        super().__init__(self.message)