from dataclasses import dataclass


@dataclass
class Requirement:
    id: str
    title: str
    description: str
    priority: str
    status: str
