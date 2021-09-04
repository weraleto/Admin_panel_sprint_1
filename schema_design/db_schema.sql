-- Создание отдельной схемы для контента:
CREATE SCHEMA IF NOT EXISTS content;

-- Жанры кинопроизведений:
CREATE TABLE IF NOT EXISTS content.genre (
    id uuid PRIMARY KEY,
    name CHAR(255) NOT NULL,
    description TEXT,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Персоны
CREATE TABLE IF NOT EXISTS content.person (
    id uuid PRIMARY KEY,
    full_name CHAR(255) NOT NULL,
    birth_date DATE,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

-- Фильмы
CREATE TABLE IF NOT EXISTS content.film_work (
    id uuid PRIMARY KEY,
    title CHAR(255) NOT NULL,
    description TEXT,
    creation_date DATE,
    certificate TEXT,
    file_path TEXT,
    rating FLOAT,
    type CHAR(255) not null,
    created_at timestamp with time zone,
    updated_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.genre_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    genre_id uuid NOT NULL,
    created_at timestamp with time zone
);

CREATE TABLE IF NOT EXISTS content.person_film_work (
    id uuid PRIMARY KEY,
    film_work_id uuid NOT NULL,
    person_id uuid NOT NULL,
    role TEXT NOT NULL,
    created_at timestamp with time zone
);

-- Уникальный композитный индекс (нельзя добавить жанр фильму более одного раза)
CREATE UNIQUE INDEX film_work_genre ON content.genre_film_work (film_work_id, genre_id);

-- Уникальный композитный индекс (нельзя добавить одного актера фильму более одного раза)
CREATE UNIQUE INDEX film_work_person ON content.person_film_work (film_work_id, person_id, role);