# DEPLOYMENT GUIDE

## Deploying Stock Market Analytics Dashboard

### Deployment Options

1. **Render (Recommended)** - Free, easy, serverless
2. **Heroku** - Traditional PaaS platform
3. **AWS/GCP/Azure** - Enterprise solutions
4. **Local Server** - For development/testing

---

## 🚀 RENDER DEPLOYMENT (Recommended)

Render is free for hobby projects and offers easy integration with GitHub.

### Prerequisites
- GitHub account with repository access
- Render account (free at https://render.com)
- Push code to GitHub

### Step-by-Step Instructions

#### 1. Push Code to GitHub
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

#### 2. Create Render Web Service
1. Log in to https://render.com
2. Click "New +" → "Web Service"
3. Connect GitHub account (if not already connected)
4. Select your repository
5. Fill in configuration:

| Field | Value |
|-------|-------|
| Name | stock-market-dashboard |
| Environment | Python 3.11 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:server` |
| Plan | Free (or Starter) |

#### 3. Set Environment Variables
In Render dashboard:
```
DASH_HOST=0.0.0.0
DASH_PORT=8050
DEBUG_MODE=False
```

#### 4. Deploy
Click "Create Web Service" and wait for deployment (2-5 minutes)

#### 5. Verify
- Check deployment logs for errors
- Visit your app URL (provided by Render)
- Test all features

### Cost
- **Free Tier**: Up to 750 hours/month (free service spins down after 15 min inactivity)
- **Starter**: $7+ /month (always on)

---

## 🐳 DOCKER DEPLOYMENT

### Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "app:server", "--bind", "0.0.0.0:8050"]
```

### Create .dockerignore
```
__pycache__
*.pyc
.git
.gitignore
venv/
env/
.env
.DS_Store
notebooks/
data/*.csv
models/*.pkl
```

### Build and Run
```bash
docker build -t stock-dashboard .
docker run -p 8050:8050 stock-dashboard
```

---

## 📦 REQUIREMENTS OPTIMIZATION FOR DEPLOYMENT

### Reduce Model Size
```python
# In code, load FinBERT only when needed
if ENABLE_FINBERT:
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
```

### Use Lightweight Alternatives
- Replace torch with ONNX for model inference
- Use `sentiment` library instead of full FinBERT
- Cache downloaded models to reduce bandwidth

### Optimize Dependencies
```bash
pip install pipdeptree
pipdeptree
```

---

## 🔐 SECURITY CHECKLIST

- [ ] Set `DEBUG_MODE=False` in production
- [ ] Use environment variables for sensitive data
- [ ] Implement input validation
- [ ] Use HTTPS (Render provides SSL by default)
- [ ] Keep dependencies updated
- [ ] Review .gitignore matches sensitive files
- [ ] Implement rate limiting if exposed publicly
- [ ] Use authentication if needed

---

## 📊 MONITORING & MAINTENANCE

### Check Application Status
```bash
# View logs in Render dashboard
# Monitor performance metrics
```

### Update Dependencies
```bash
pip list --outdated
pip install -U <package-name>
pip freeze > requirements.txt
git commit -am "Update dependencies"
git push
```

### Restart Service
In Render dashboard → Manual Deploy → Restart Web Service

---

## 🆘 TROUBLESHOOTING DEPLOYMENT

### Issue: "Dependencies failed to install"
```bash
# Ensure requirements.txt format
pip install -r requirements.txt

# Use specific versions
pip freeze > requirements.txt
```

### Issue: "App starts but shows blank page"
- Check browser console for JavaScript errors
- Verify data files are in correct locations
- Check application logs in Render dashboard

### Issue: "Out of memory" errors
- Reduce model sizes
- Use VADER instead of FinBERT
- Implement data pagination

### Issue: "Slow response times"
- Enable caching for expensive operations
- Optimize data loading
- Use CDN for static assets
- Upgrade to paid Render tier

---

## 📈 SCALING CONSIDERATIONS

### For Small Datasets (<1GB)
- Render Free/Starter tier sufficient
- Load all data in memory
- Use SQLite for temporary caching

### For Medium Datasets (1-10GB)
- Render Standard tier recommended
- Consider using PostgreSQL for caching
- Implement lazy loading for data

### For Large Datasets (>10GB)
- Consider AWS/GCP/Azure
- Use cloud databases (RDS, Cloud SQL)
- Implement chunked data loading
- Use caching layer (Redis)

---

## 🔄 CONTINUOUS DEPLOYMENT

Render automatically deploys when you push to GitHub's main branch.

### Set up Smart Deploys
1. In Render → Settings → Deploy on Push
2. Select branch (main)
3. Automatic deployments enabled

### Branch Strategy
```bash
# main - Production (auto-deploys)
# develop - Staging
# feature/* - Development
```

---

## 📝 FINAL CHECKLIST

- [ ] Code pushed to GitHub
- [ ] requirements.txt contains all dependencies
- [ ] config.py configured for production
- [ ] Data files in data/ directory
- [ ] .gitignore properly configured
- [ ] README.md updated
- [ ] QUICKSTART.md reviewed
- [ ] Environment variables set
- [ ] Application tested locally
- [ ] Procfile created
- [ ] Render Web Service created
- [ ] Application deployed and running
- [ ] Application tested in production
- [ ] Monitoring enabled

---

## 📞 SUPPORT

For deployment issues:
1. Check Render logs (Dashboard → Logs)
2. Review this guide's troubleshooting section
3. Check application error messages locally
4. Contact Render support

---

**Good luck with your deployment! 🚀**
