# -phase4-flask-blog-
# Phase 4 Flask Blog

This repository contains the source code for a full-stack web application built with Flask. It demonstrates the best practices discussed in my blog post: **"From Code to Production: Best Practices for Full-Stack Web Apps"**.

## Features

- **RESTful API Design**: Structured endpoints with proper HTTP status codes.
- **Database Separation**: Uses PostgreSQL with environment variable configuration.
- **Production Ready**: Includes configuration for deployment on platforms like Render.

## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Genepro75/phase4-flask-code-challenge.git
   cd phase4-flask-code-challenge
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   Create a `.env` file in the root directory:
   ```env
   DATABASE_URL=postgresql://user:password@localhost:5432/flask_blog
   SECRET_KEY=your_secret_key
   ```

4. Run the application:
   ```bash
   flask run
   ```
