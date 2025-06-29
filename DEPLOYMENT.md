# Hospital Management System - Vercel Deployment Guide

This guide will help you deploy your Django Hospital Management System on Vercel.

## Prerequisites

1. A GitHub account
2. A Vercel account (free at vercel.com)
3. Your Django project ready for deployment

## Deployment Steps

### 1. Prepare Your Repository

Make sure your project is pushed to a GitHub repository. The following files have been added to your project:

- `vercel.json` - Vercel configuration
- `build_files.sh` - Build script
- `api/index.py` - API handler for Vercel
- Updated `hms_project/settings.py` - Production-ready settings
- Updated `hms_project/wsgi.py` - Vercel-compatible WSGI
- Updated `requirements.txt` - Added whitenoise for static files
- `.gitignore` - Excludes unnecessary files

### 2. Deploy to Vercel

1. **Go to Vercel Dashboard**
   - Visit [vercel.com](https://vercel.com)
   - Sign in with your GitHub account

2. **Import Your Repository**
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will automatically detect it's a Python project

3. **Configure Environment Variables**
   In your Vercel project settings, add these environment variables:
   ```
   SECRET_KEY=your-secure-secret-key-here
   DEBUG=False
   EMAIL_HOST_USER=smart.care.2025.01@gmail.com
   EMAIL_HOST_PASSWORD=soip vlre szcg lmwu
   ```

4. **Deploy**
   - Click "Deploy"
   - Vercel will build and deploy your application

### 3. Post-Deployment Setup

After deployment, you'll need to:

1. **Run Migrations**
   - Vercel doesn't support running Django management commands directly
   - You may need to use a database service like PostgreSQL
   - Consider using Django's `--run-syncdb` flag in your build script

2. **Create Superuser**
   - You'll need to create a superuser account
   - Consider using Django's `createsuperuser` command in your build script

3. **Static Files**
   - Static files are handled by whitenoise middleware
   - The build script runs `collectstatic`

## Important Notes

### Database Limitations
- Vercel uses serverless functions with read-only filesystem
- SQLite database won't persist between requests
- Consider using external database services:
  - **PostgreSQL**: Supabase, Railway, or Neon
  - **MongoDB**: MongoDB Atlas
  - **MySQL**: PlanetScale

### File Uploads
- Media files won't persist on Vercel
- Consider using cloud storage:
  - AWS S3
  - Cloudinary
  - Firebase Storage

### Email Configuration
- Email settings are configured for Gmail SMTP
- Make sure your Gmail app password is correct
- Consider using services like SendGrid for production

## Alternative Deployment Options

If Vercel doesn't meet your needs, consider:

1. **Railway** - Better Django support
2. **Heroku** - Traditional Django hosting
3. **DigitalOcean App Platform** - Good for Django apps
4. **AWS Elastic Beanstalk** - Enterprise-grade hosting

## Troubleshooting

### Common Issues

1. **Build Failures**
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version compatibility

2. **Static Files Not Loading**
   - Verify whitenoise is in `requirements.txt`
   - Check `STATIC_ROOT` and `STATICFILES_DIRS` settings

3. **Database Errors**
   - SQLite won't work on Vercel
   - Switch to external database service

4. **Environment Variables**
   - Ensure all required environment variables are set in Vercel dashboard
   - Check variable names match those in `settings.py`

### Getting Help

- Check Vercel logs in the dashboard
- Review Django error logs
- Test locally with production settings

## Security Considerations

1. **Secret Key**: Use a strong, unique secret key
2. **Debug Mode**: Set `DEBUG=False` in production
3. **Allowed Hosts**: Configure properly for your domain
4. **HTTPS**: Vercel provides SSL certificates automatically

## Performance Optimization

1. **Static Files**: Use CDN for better performance
2. **Database**: Use connection pooling
3. **Caching**: Implement Redis or similar
4. **Images**: Optimize and compress images

---

For more information, visit:
- [Vercel Documentation](https://vercel.com/docs)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/)
- [Django on Vercel](https://vercel.com/guides/deploying-django-with-vercel) 