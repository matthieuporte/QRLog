## Alembic

### init migrations

```sh
alembic init backend/db/migrations
```

where `backend/db/migrations` is the directory to save migrations files

### generate migrations file

```sh
alembic revision --autogenerate -m "comment to update"
```

### apply migrations

```sh
alembic upgrade head
```

## Linters

### black : reindent code

`black --check backend`
`black backend`

### isort : reorder imports

`isort --check backend`
`isort backend`

### flake8 : 

`flake8 backend --count --show-source --statistics`
`flake8 backend`
