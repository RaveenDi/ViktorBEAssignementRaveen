import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field

@dataclass
class Product(ABC):
    """Abstract base class for all products."""

    id: uuid.UUID = field(default_factory=uuid.uuid4, init=False)
    price_eur: float

    @abstractmethod
    def get_weight_kg(self) -> float:
        """Return the weight in kg. Software licenses return 0."""
        pass

@dataclass
class Book(Product):
    title: str
    author: str
    num_pages: int
    weight_kg: float

    def get_weight_kg(self) -> float:
        return self.weight_kg

@dataclass
class MusicAlbum(Product):
    artist: str
    title: str
    num_tracks: int
    weight_kg: float

    def get_weight_kg(self) -> float:
        return self.weight_kg

@dataclass
class SoftwareLicense(Product):
    name: str

    def get_weight_kg(self) -> float:
        return 0.0