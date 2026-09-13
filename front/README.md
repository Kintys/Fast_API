# Booking System

Simple room booking frontend (Vue 3 + Vite).

## Setup

```bash
npm install
cp .env.example .env
npm run dev
```

## Backend

## Backend

Production API: `https://fast-api-9luc.onrender.com/api`

Local `npm run dev` uses Vite proxy (`VITE_API_BASE_URL=/api` in `.env.development`).

Production build uses full API URL from `.env.production`.

On Render (frontend service), set env:
```
VITE_API_BASE_URL=https://fast-api-9luc.onrender.com/api
```
Then redeploy (Vite bakes this value at build time).

Rooms list endpoint: `GET /api/rooms`

