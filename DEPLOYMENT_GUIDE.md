# SMS Railway Deployment Guide

This guide will help you deploy the School Management System to Railway.

## Prerequisites

1. **Railway CLI**: Install the Railway CLI
   ```bash
   npm install -g @railway/cli
   ```
   Or visit: https://railway.app/cli

2. **Railway Account**: Create an account at https://railway.app

## Quick Deployment Steps

### Option 1: Automated Deployment (Recommended)

1. **Run the deployment script**:
   ```bash
   python deploy.py
   ```

2. **Follow the prompts** to authenticate and deploy

### Option 2: Manual Deployment

1. **Login to Railway**:
   ```bash
   railway login
   ```

2. **Initialize project**:
   ```bash
   railway init
   ```

3. **Add PostgreSQL database**:
   ```bash
   railway add postgresql
   ```

4. **Deploy the application**:
   ```bash
   railway up
   ```

## Post-Deployment Configuration

1. **Set Environment Variables** in Railway Dashboard:
   - `JWT_SECRET_KEY`: Generate a secure 32+ character key
   - `ENVIRONMENT`: Set to `production`
   - `DEBUG`: Set to `False`
   - `CORS_ORIGINS`: Set to your frontend domain

2. **Initialize Database**:
   Visit: `https://your-app.railway.app/init-db`

3. **Test the API**:
   - Health check: `https://your-app.railway.app/health`
   - Database test: `https://your-app.railway.app/db-test`

## API Endpoints

- `GET /` - Root endpoint with basic info
- `GET /health` - Health check
- `GET /db-test` - Test database connection
- `GET /init-db` - Initialize database tables
- `GET /env` - Show environment variables (sensitive ones redacted)

## Default Admin User

After database initialization, you can login with:
- **Username**: `admin`
- **Password**: `admin123`
- **Email**: `admin@sms.local`

**⚠️ Important**: Change the default admin password immediately after first login!

## Troubleshooting

### Common Issues

1. **Database Connection Failed**:
   - Check if PostgreSQL service is running
   - Verify DATABASE_URL environment variable

2. **Build Failed**:
   - Check requirements.txt for missing dependencies
   - Verify Python version compatibility

3. **App Won't Start**:
   - Check logs in Railway dashboard
   - Verify PORT environment variable is being used

### Getting Help

- Check Railway logs: `railway logs`
- View Railway dashboard: https://railway.app/dashboard
- Railway documentation: https://docs.railway.app

## Security Notes

- Always use HTTPS in production
- Set strong JWT secret keys
- Configure CORS properly
- Change default passwords
- Enable rate limiting
- Monitor application logs

## Next Steps

1. Set up monitoring and alerting
2. Configure custom domain
3. Set up CI/CD pipeline
4. Add SSL certificate
5. Configure backup strategy