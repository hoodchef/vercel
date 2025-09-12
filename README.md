# Trading Terminal Monorepo

This repository contains two applications:

- `apps/web` – Next.js frontend deployed on Vercel
- `apps/api` – FastAPI backend deployed on Fly.io

### Deployment

GitHub Actions are configured to deploy each app:

- `.github/workflows/web.yml` deploys the web app to Vercel.
- `.github/workflows/api.yml` deploys the API to Fly.io.

Environment variable examples are provided in each app's `.env.example` file.
