# Mobile Money System

A Django application for managing mobile money agents, customers, deposits, withdrawals, and transfers.

## Group members

| Name | Student ID |
| --- | --- |
| MASAI RISYAT | 224-063011-30093 |
| SSEWAVVA ISMAIL | 224-063011-29990 |

## Run locally

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/`. The Django admin is at `http://127.0.0.1:8000/admin/`.

## Deploy to Render

This repository includes a Render Blueprint in `render.yaml`. After pushing the project to GitHub:

1. Sign in to [Render](https://render.com/) and choose **New +** > **Blueprint**.
2. Connect the GitHub repository and approve the Blueprint.
3. Wait for the build and deploy to finish. Render will display the public service URL.
4. Open `/admin/` on that URL and sign in with username `admin` and password `admin123`. Change this demo password immediately after the first login; do not use it for real or sensitive data.

The demo deployment uses SQLite, whose data is not durable across service replacement or redeployments. Use a persistent database before relying on it for ongoing data.

## Push to GitHub

Create an empty GitHub repository first, then run these commands from the project root (replace the URL with your repository URL):

```powershell
git config user.name "Your Name"
git config user.email "you@example.com"
git status
git add -A
git status
git commit -m "Prepare mobile money project for deployment"
git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPOSITORY>.git
git push -u origin master
```

Review the second `git status` before committing. Local SQLite databases, virtual environments, and `out.txt` are excluded by `.gitignore`.
