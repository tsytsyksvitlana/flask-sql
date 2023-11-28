from dataclasses import dataclass, asdict


@dataclass(slots=True)
class StudentRequest:
    first_name: str
    last_name: str

    def to_dict(self) -> dict[str]:
        data = asdict(self)
        if not all(isinstance(item, str) for item in data.values()):
            raise TypeError('to_dict')
        return data
