from modules.knowledge.requirement import Requirement
from modules.knowledge.requirement_manager import RequirementManager


def test_requirement_database():

    manager = RequirementManager()

    manager.initialize()

    req = Requirement(
        "REQ-000001",
        "Front Loader Lift Capacity",
        "Loader shall lift 750 kg",
        "HIGH",
        "OPEN"
    )

    manager.add_requirement(req)

    result = manager.get_requirement("REQ-000001")

    assert result is not None
    assert result.title == "Front Loader Lift Capacity"
