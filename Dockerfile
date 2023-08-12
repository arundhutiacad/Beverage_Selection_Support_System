# Stage 1: Backend (Python) build
FROM python:3.9 AS backend

# Set the working directory for the backend
WORKDIR /starbucks

# Copy the required files for the backend
COPY starbucks_drinkMenu_expanded.csv .
COPY random_forest_model.pkl .
COPY app.py .
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the backend will run
EXPOSE 8000

# Start the backend application
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000"]


# Stage 2: Frontend (npm) build
FROM node:14 AS frontend

# Set the working directory for the frontend
WORKDIR /starbucks/client

# Copy the required files for the frontend
COPY client/package.json .
COPY client/package-lock.json .
COPY client/public public
COPY client/src src

# Install dependencies and build the frontend
RUN npm ci
RUN npm run build


# Stage 3: Combine backend and frontend
FROM backend AS final

# Copy the built frontend files to the backend container
COPY --from=frontend /app/client/build /app/client/build

# Change the working directory to the frontend build directory
WORKDIR /starbucks/client/build

# Serve the frontend with a static file server
CMD ["npm", "start"]
