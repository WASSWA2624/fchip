# FCHIP

**FCHIP** — FairBanks Community Health Intelligence Platform.

## Structure

- `backend/` — Node.js / Express / Prisma API (`fchip-backend`)
- `frontend/` — Flutter client (`fchip`)

## Quick start

**Backend**

```powershell
cd backend
npm install
Copy-Item env.template.txt .env   # then set MySQL to fchip_db
npx prisma migrate dev
npm run dev
```

**Frontend**

```powershell
cd frontend
flutter pub get
.\tool\run_web_5201.ps1
```

Demo accounts use `@fchip.com` emails and password `Fchip@2624.` after seeding.
