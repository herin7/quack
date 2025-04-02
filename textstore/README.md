# 🌟 Quack - Secure URL Data Storage

Quack is a feature-rich Django-based web application designed for secure and personalized data storage. This app allows users to create custom spaces, store personal data and URLs, and access them securely using a password protection system.

Whether you're a creator managing content, an entrepreneur safeguarding critical data, or just someone looking for a safe personal space on the web, Quack has you covered. Built with security and usability in mind, it ensures your digital space is always just a click away—secure, accessible, and organized.

## 🎥 Demo
* **Live Demo**: [Home - Quack](https://quack-2.onrender.com/)
* **Video Demo**: [Watch on YouTube](https://youtu.be/iS8OXg74EUI)

## 🚀 Key Features

### 🔒 Customizable User Spaces
* Create Personal Spaces: Users can sign up and create their own custom URL to access a personal space. Whether you want a portfolio or a secure place for your personal content, Quack gives you full control.
* Password Protection: For extra security, each user space requires a password after the first visit. This ensures that only authorized users can access their stored content.

### 📂 Content Storage and Management
* Store Text and URLs: Save your text-based data, URLs, and web links securely in your personal space. Perfect for those who want a central location to store quick notes or reference links.
* Media Management with Cloudinary: Easily upload and manage media files (images, videos) using Cloudinary, ensuring efficient storage and fast retrieval.

### 🌍 Accessible Anytime, Anywhere
* Secure Access: After setting up your personal space, you can visit your custom URL anytime to retrieve, update, or delete your stored data.
* User Profile Management: Edit your profile and keep your space organized. You can also manage your content directly from the dashboard.

### 🛠️ Powerful Backend Features
* Cloud Storage: Integration with Cloudinary ensures smooth handling of media files and their seamless retrieval from anywhere.
* Neon PostgreSQL: Utilizing Neon PostgreSQL ensures that your data is stored securely and efficiently, with scalability built into the system from the start.

### 🎨 Responsive and User-Friendly Interface
* Authentication System: Secure user registration, login, and authentication are built-in with Django, offering a reliable framework for managing user access.

## 🧑‍💻 Tech Stack
* Django for backend development
* Neon PostgreSQL for cloud database storage
* Cloudinary for media file handling (images, videos)
* HTML, CSS, and JavaScript for the user interface

## 🌱 Installation Instructions

### Configuration
Before running the application, you'll need to set up your environment variables. Create a `.env` file in the root directory with the following configuration:

```python
DATABASE_URL='{neonpostgresql_url}'
DJANGO_SECRET_KEY='your_secret_key_here'
ALLOWED_HOSTS='localhost, 127.0.0.1'

# Cloudinary settings
CLOUDINARY_CLOUD_NAME='your_cloud_name_here'
CLOUDINARY_API_KEY='your_api_key_here'
CLOUDINARY_API_SECRET='your_api_secret_here'
```

### Steps to Set Up the Project Locally

1. Clone the repository:
```bash
git clone https://github.com/herin7/quack.git
cd quack
```

2. Set up the virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up the database:
```bash
python manage.py migrate
```

5. Create a superuser (optional, for accessing the Django admin):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ to start using Quack.

## 🚀 Deployment
The application is successfully deployed and running on render. You can access the live version at [APP URL](https://quack-2.onrender.com/)

## ✨ What's Next?
* Social Media Integration: The ability to share your custom URL with others and integrate with social platforms.
* Advanced Content Management: More tools to organize, categorize, and search through stored data.
* Enhanced Admin Features: Greater admin control to manage users and spaces across the platform.

## 📝 Contributing
We welcome contributions! Feel free to open an issue or create a pull request if you have any suggestions, bug fixes, or improvements. Your feedback and ideas help make Quack better!

## 💬 Feedback
We value your feedback! Let us know what works, what doesn't, and how we can improve your experience with Quack. Reach out if you need any help.

This app was built with passion and precision, combining powerful backend features with a clean, user-friendly interface. Quack isn't just a tool—it's your personal space to securely store and manage your most valuable content.
