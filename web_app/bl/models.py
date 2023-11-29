from dataclasses import dataclass, asdict


@dataclass(slots=True)
class StudentRequest:
    first_name: str
    last_name: str
    group_id: int | None

    def to_dict(self) -> dict[str]:
        data = asdict(self)
        if not (isinstance(self.first_name, str)
                and isinstance(self.last_name, str)
                and isinstance(self.group_id, int)):
            raise TypeError('to_dict')
        return data
