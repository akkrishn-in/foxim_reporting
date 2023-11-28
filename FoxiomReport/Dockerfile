# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the necessary files for dependency installation
COPY pyproject.toml poetry.lock /app/

# Install poetry and project dependencies
RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Set the environment variables
ENV CONNECTION_STRING="${DATABASE_DRIVER};${DATABASE_SERVER};${DATABASE_NAME};${DATABASE_USER};${DATABASE_PASSWORD};${DATABASE_INSTANCE}"

# Command to run the application
CMD ["poetry", "run", "python", "app.py"]
