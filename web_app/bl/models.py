from dataclasses import dataclass, asdict


@dataclass(slots=True)
class StudentRequest:
    first_name: str
    last_name: str
    group_id: int | None

    def __post_init__(self) -> None:
        try:
            if self.group_id is not None:
                self.group_id = int(self.group_id)
        except ValueError:
            raise ValueError('Not valid group_id')

    def to_dict(self) -> dict[str, str | int | None]:
        return asdict(self)


@dataclass(slots=True)
class GroupRequest:
    name: str
    course_id: int

    def to_dict(self) -> dict[str, str | int]:
        return asdict(self)


@dataclass(slots=True)
class CourseRequest:
    name: str
    description: str

    def to_dict(self) -> dict[str, str]:
        return asdict(self)
