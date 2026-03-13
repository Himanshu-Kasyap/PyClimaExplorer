# 🚀 Quick Deployment Reference

## TL;DR - Fastest Way to Deploy

### Streamlit Cloud (RECOMMENDED)
```bash
# 1. Push to GitHub
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/YOUR_USERNAME/pyclima-explorer.git
git push -u origin main

# 2. Go to https://share.streamlit.io
# 3. Click "New app" → Select repo → Deploy
# Done! ✅
```

---

## Why NOT Vercel?

❌ **Vercel doesn't support Streamlit** because:
- Streamlit needs persistent WebSocket connections
- Vercel is for static sites & serverless functions
- Streamlit requires a long-running Python server

✅ **Use these instead:**
- Streamlit Cloud (best for Streamlit)
- Heroku (general Python apps)
- Railway (modern deployment)
- Google Cloud Run (scalable)

---

## Platform Comparison

| Platform | Free Tier | Setup Time | Best For |
|----------|-----------|------------|----------|
| **Streamlit Cloud** | ✅ Yes | 2 min | Streamlit apps |
| **Heroku** | ✅ Yes | 5 min | Python apps |
| **Railway** | ✅ $5 credit | 3 min | Modern apps |
| **Google Cloud** | ❌ Pay-as-go | 10 min | Production |
| **Vercel** | ❌ Not supported | N/A | Static sites only |

---

## Quick Commands

### Streamlit Cloud
```bash
# Just push to GitHub, then deploy via web UI
git push origin main
```

### Heroku
```bash
heroku login
heroku create pyclima-explorer
git push heroku main
heroku open
```

### Railway
```bash
# Deploy via web UI at railway.app
# Connect GitHub repo → Auto-deploy
```

### Docker (Any Platform)
```bash
docker build -t pyclima .
docker run -p 8501:8501 pyclima
```

---

## Files Needed for Each Platform

### Streamlit Cloud
- ✅ `requirements.txt` (already have)
- ✅ `app.py` (already have)
- ✅ GitHub repository

### Heroku
- ✅ `requirements.txt` (already have)
- ✅ `Procfile` (already created)
- ✅ `setup.sh` (already created)

### Railway
- ✅ `requirements.txt` (already have)
- ✅ `app.py` (already have)

### Docker
- ✅ `Dockerfile` (already created)
- ✅ `.dockerignore` (already created)

---

## Troubleshooting

### "Can I use Vercel?"
**No.** Vercel doesn't support Streamlit. Use Streamlit Cloud instead.

### "Which is easiest?"
**Streamlit Cloud.** Purpose-built for Streamlit, 1-click deploy.

### "Which is free?"
**Streamlit Cloud** (free forever) and **Heroku** (free tier with limits).

### "Which is best for production?"
**Google Cloud Run** or **AWS** for scalability and reliability.

### "I want custom domain"
**Streamlit Cloud** (paid), **Heroku**, or **Railway** support custom domains.

---

## My Recommendation

**For PyClimaExplorer:**

1. **First choice**: Streamlit Community Cloud
   - Free, easy, purpose-built
   - See: [DEPLOY_STREAMLIT_CLOUD.md](DEPLOY_STREAMLIT_CLOUD.md)

2. **Second choice**: Railway
   - Modern, fast, auto-scaling
   - See: [DEPLOY_ALTERNATIVES.md](DEPLOY_ALTERNATIVES.md)

3. **Third choice**: Heroku
   - Well-documented, reliable
   - See: [DEPLOY_ALTERNATIVES.md](DEPLOY_ALTERNATIVES.md)

---

## Next Steps

1. Read [DEPLOY_STREAMLIT_CLOUD.md](DEPLOY_STREAMLIT_CLOUD.md)
2. Push code to GitHub
3. Deploy to Streamlit Cloud
4. Share your live app! 🎉

---

**Questions? Check the full deployment guides!**
