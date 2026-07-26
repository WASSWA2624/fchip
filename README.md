# FCHIP

**FCHIP** — Community Health Intelligence Platform.

**Slogan:** Your health, our mission.

## How the product works

Start here: [`app-flows/README.md`](app-flows/README.md) — flow charts of shells, screens, and how modules connect.

Product narrative SoT: [`.cursor/app-write-up.mdc`](.cursor/app-write-up.mdc)

## Structure

- `backend/` — Node.js / Express / Prisma API (`fchip-backend`)
- `frontend/` — Flutter client (`fchip`)
- `app-flows/` — App flow diagrams (overview → workspaces → platform)

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
