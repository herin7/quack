# Quack - Secure URL Data Storage

Quack is a Django-based web application that allows users to securely store personal data and URLs. The app provides an added layer of security by requiring a password when users attempt to access their stored data after the first access.

## Usage

1. **Create Your Personal Space**: Sign up or log in to get started. Once you're in, create your own custom URL—your unique gateway to a personal space where you can store anything!

2. **Store Data Securely**: Add your text, links, or media files to your space. Everything you store is protected by a password, ensuring that only you can access it after the first visit.

3. **Access Anytime, Anywhere**: Visit your custom URL at any time to retrieve or update your stored data. Whether you're on the go or at home, your personal space is just a click away.

4. **Personalize Your Experience**: Edit your profile and make your space truly yours. Update your information and manage your content effortlessly, keeping everything organized and secure.

With Quack, your data is always within reach, safely stored and accessible whenever you need it—anytime, anywhere!

## Features

- **User Authentication**: Register, login, and manage accounts.
- **Store Text and URLs**: Save your text data or web URLs securely.
- **Password Protection**: Access stored data only after entering a password, adding extra security.
- **Cloud Media Management**: Media files are stored using **Cloudinary** for efficient storage and retrieval.
- **PostgreSQL Database**: **Neon PostgreSQL** is used for storing user data securely.
- **Responsive Design**: User-friendly and modern UI for a smooth experience across devices.

## Technologies Used

- **Django**: Backend framework for building the app.
- **Cloudinary**: Used for handling media files (images, etc.).
- **Neon PostgreSQL**: For secure and reliable database storage.
- **HTML/CSS/JavaScript**: For frontend UI and interactivity.

## Project Structure

The project is organized to separate different functionalities, making it easier to maintain and scale.

## Installation Instructions

### Configuration

#### Environment Variables

Before running the application, you need to create a `.env` file in the root directory of your project. This file will store sensitive configuration settings. 

Create a file named `.env` and add the following credentials:
```python
DATABASE_URL='{neonpostgresql_url}'
DJANGO_SECRET_KEY='your_secret_key_here'
ALLOWED_HOSTS='localhost, 127.0.0.1'

# Cloudinary settings
CLOUDINARY_CLOUD_NAME='your_cloud_name_here'
CLOUDINARY_API_KEY='your_api_key_here'
CLOUDINARY_API_SECRET='your_api_secret_here'
```

#### Steps to Set Up the Project Locally

1. **Clone the repository**:
    ```sh
    git clone https://github.com/herin7/quack.git
    cd quack
    ```

2. **Set up the virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser** (for accessing the Django admin/This won't be needed of you use Neon PostgreSQL):
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to start using the app.






