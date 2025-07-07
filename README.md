# 🩺 Doctor Appointment Booking App

A simple Flask web application for booking doctor appointments, deployed on an Azure Virtual Machine with MySQL as the backend database and Nginx + Gunicorn for production hosting.

---

## 🚀 Features

- Book appointments with selected doctors
- Stores appointment data in a MySQL database
- Clean, responsive UI with CSS and images
- Deployed using Gunicorn and Nginx on an Azure VM
- Runs as a background service with systemd

---

## 📁 Project Structure

doctor-appointment/
├── app.py
├── requirements.txt
├── static/
│   ├── style.css
│   └── images/
│       ├── doctor1.jpg
│       ├── doctor2.jpg
│       └── clinic-banner.jpg
├── templates/
│   ├── index.html
│   └── success.html



---

## 🛠️ Setup Instructions

### 1. 🖥️ Azure VM Setup

- Create a Linux VM (Ubuntu recommended)
- Open ports 22 (SSH), 80 (HTTP) in the Networking tab

### 2. 🔧 Install Dependencies on VM

```
sudo apt update
sudo apt install python3-pip python3-venv nginx mysql-server
```

### 3. 📦 Set Up the Flask App

```
git clone <your-repo-url> doctor-appointment
cd doctor-appointment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### 4. 🗃️ Configure MySQL

```
sudo mysql -u root -p
```

```
CREATE DATABASE clinic;
CREATE USER 'flaskuser'@'localhost' IDENTIFIED BY 'yourpassword';
GRANT ALL PRIVILEGES ON clinic.* TO 'flaskuser'@'localhost';
FLUSH PRIVILEGES;

USE clinic;
CREATE TABLE appointments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  phone VARCHAR(20),
  doctor VARCHAR(100),
  date DATE,
  time TIME,
  reason TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Update app.py with your DB credentials.

## 🌐 Run with Gunicorn + Nginx

### 5. 🔥 Test Gunicorn

```
gunicorn --bind 127.0.0.1:8000 app:app
```

### 6. ⚙️ Configure Nginx

```
sudo nano /etc/nginx/sites-available/doctor
```
```
server {
    listen 80;
    server_name <your-vm-public-ip>;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```
```
sudo ln -s /etc/nginx/sites-available/doctor /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx
```

## 🔁 Run Gunicorn as a Service

### 7. 🛡️ Create systemd Service
```
sudo nano /etc/systemd/system/gunicorn.service
```
Ini:
```
[Unit]
Description=Gunicorn instance to serve Flask app
After=network.target

[Service]
User=your_username
Group=www-data
WorkingDirectory=/home/your_username/doctor-appointment
Environment="PATH=/home/your_username/doctor-appointment/venv/bin"
ExecStart=/home/your_username/doctor-appointment/venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```
```
sudo systemctl daemon-reload
sudo systemctl start gunicorn
sudo systemctl enable gunicorn
```

## ✅ Access the App
Visit in your browser:
```
http://<your-vm-public-ip>
```

## 📬 Future Enhancements

- Add email notifications
- Admin dashboard to view appointments
- HTTPS with Let’s Encrypt
- Dockerize the app for container deployment

## 🧑‍💻 Author
Built with ❤️ using Flask, MySQL, and Azure.

Let me know if you'd like this saved as a downloadable file or want to push it to a GitHub repo!



