from dataclasses import dataclass, field
from datetime import datetime
import uuid


@dataclass(frozen=True)
class Genre:
    name: str
    description: str = field(default='')
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class Person:
    full_name: str
    birth_date: datetime = None
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class Film:
    title: str
    description: str = field(default='')
    creation_date: datetime = None
    certificate: str = field(default='')
    file_path: str = field(default='')
    rating: float = field(default=0.0)
    type: str = field(default='')
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class FilmGenre:
    film_work_id: uuid.UUID
    genre_id: uuid.UUID
    created_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


@dataclass(frozen=True)
class PersonFilmWork:
    film_work_id: uuid.UUID
    person_id: uuid.UUID
    role: str
    created_at: datetime = field(default_factory=datetime.now)
    id: uuid.UUID = field(default_factory=uuid.uuid4)


tables_dict = {
    'genre': Genre,
    'person': Person,
    'film_work': Film,
    'genre_film_work': FilmGenre,
    'person_film_work': PersonFilmWork
}
