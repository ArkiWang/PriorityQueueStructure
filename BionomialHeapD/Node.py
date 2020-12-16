class node(object):

    def __init__(self, key=None, parent=None, child=None, sibling=None, degree=0):
        self.key = key
        self.parent = parent
        self.child = child
        self.sibling = sibling
        self.degree = degree

