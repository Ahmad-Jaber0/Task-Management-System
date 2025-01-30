# 📌 Task Management System  

## 📝 Description  
This project is a **Task Management System** designed for companies to efficiently manage tasks among employees according to their roles. The system follows a clear hierarchy:

- **Manager**
- **Team Leaders**
- **Developers**

Each role has specific permissions and responsibilities:  

- **Manager**:  
  - Access all **team leaders** and **developers**  
  - View company hierarchy  
  - See all tasks  
  - Add new employees  

- **Team Leader**:  
  - View and assign tasks to their **developers**  
  - Manage their own tasks  

- **Developer**:  
  - View their assigned tasks  
  - Update the status of their tasks  

---

## ⚙️ Task Parts  
The project consists of the following key parts:  

1. **Database Design** – Creating tables for employees, tasks, and roles.  
2. **Authentication System** – Implementing login and logout functionality.  
3. **Web Interface** – Developing user-friendly pages for different roles.  

---

## 🛠️ Tech Stack  
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, JavaScript  
- **Database**: SQLite 
- **Authentication**: Django's built-in authentication system  

---

## 🚀 Features  

✅ **User Roles & Authentication**  
✅ **Task Assignment & Management**  
✅ **Sorting & Filtering for Tasks/Users**  
✅ **Role-Based Access Control (RBAC)**  

---

## 🔑 Installation & Setup  

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/Ahmad-Jaber0/Task-Management-System.git
cd task-management-system
```

2️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

3️⃣ **Run database migrations**  
```bash
python manage.py migrate
```

4️⃣ **Create a superuser (for Manager role)**  
```bash
python manage.py createsuperuser
```

5️⃣ **Run the development server**  
```bash
python manage.py runserver
```

---

## 🌍 Usage  

### **1️⃣ Login Page**  
Employees can log in to view and manage their tasks.  

### **2️⃣ Manager Dashboard**  
- View & manage **Team Leaders** and **Developers**  
- Add new employees  
- Approve new tasks  

### **3️⃣ Team Leader Panel**  
- View **assigned developers**  
- Assign & manage tasks  

### **4️⃣ Developer Panel**  
- View & update **task statuses**  
  - **In Progress**  
  - **Ready for Test**  
  - **Completed**  

---

## 🤝 Contributing  
Feel free to contribute by submitting **pull requests**. For major changes, please open an **issue** first to discuss what you would like to change.  

---

### 📧 Contact  
For any inquiries or suggestions, reach out via **jaber5834@gmail.com**  
