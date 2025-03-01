#!/bin/bash

# Create the alembic revision
alembic revision --autogenerate -m "Initial migration"

# Apply the migration
alembic upgrade head

echo "Database initialized successfully!" 