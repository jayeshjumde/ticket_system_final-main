# Ticket Booking Management System 🎟️

A Django-based web application to manage event/show ticket bookings with user authentication and admin controls.

## Features

- User Registration and Login
- View available shows/events
- Book tickets (select seats)
- View booking history
- Admin panel to add/edit/delete shows
- Dockerized setup
- CI/CD Pipeline (Jenkins-ready)

## Technologies Used

- Django 4.2
- PostgreSQL
- Docker & Docker Compose
- Jenkins (for DevOps automation)

# Screenshots

## Home Page
![Home Page](screenshots/home_page.png)

## Show Page
![Show Page](screenshots/show_page.png)

## Booking History
![Booking History](screenshots/booking_history.png)

## Login
![Login](screenshots/login.png)

## Register
![Register](screenshots/Register.png)

## Setup Instructions

```bash
# Clone the repository
git clone https://github.com/your-username/ticket_system_final.git

# Go into the project directory
cd ticket_system_final

# Build and run Docker containers
docker-compose up --build
