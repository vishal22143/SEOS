from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Material:
    code:str
    name:str
    density:float


@dataclass
class Part:

    part_number:str
    name:str
    material:str
    quantity:int=1
    weight:float=0.0
    revision:str="A"


@dataclass
class Assembly:

    assembly_number:str
    name:str
    children:List=field(default_factory=list)

    def add(self,item):
        self.children.append(item)

    def count(self):
        return len(self.children)


@dataclass
class Machine:

    machine_number:str
    manufacturer:str
    model:str
    assemblies:List=field(default_factory=list)

    def add(self,assembly):
        self.assemblies.append(assembly)


@dataclass
class HydraulicCylinder:

    cylinder_number:str
    bore:float
    rod:float
    stroke:float


@dataclass
class HydraulicHose:

    hose_number:str
    length:float
    diameter:float


@dataclass
class Bearing:

    bearing_number:str
    series:str


@dataclass
class Bolt:

    bolt_number:str
    size:str
    length:float


@dataclass
class Pin:

    pin_number:str
    diameter:float
    length:float


@dataclass
class Bushing:

    bushing_number:str
    inside:float
    outside:float
    length:float
