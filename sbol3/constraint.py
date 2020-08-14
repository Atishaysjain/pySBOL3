import math

from . import *


class Constraint(Identified):

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.restriction = URIProperty(self, SBOL_RESTRICTION, 0, math.inf)
        self.subject = ReferencedObject(self, SBOL_SUBJECT, 0, math.inf)
        self.object = ReferencedObject(self, SBOL_OBJECT, 0, math.inf)

    def validate(self) -> None:
        super().validate()
