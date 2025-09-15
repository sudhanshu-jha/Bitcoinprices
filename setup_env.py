#!/usr/bin/env python3
"""
Environment Setup Script for Bitcoin Prices Django Project
This script helps you set up and manage environment variables.
"""

import os
import sys
from pathlib import Path

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = Path('.env')
    
    if env_file.exists():
        print("✅ .env file already exists!")
        return
    
    print("📝 Creating .env file...")
    
    env_content = """# Django Settings
SECRET_KEY=k&8vl)hycn$hxh*dp%aj$91y4a!jwlvw1n@61upa1pqbjby)u3
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# CoinMarketCap API Configuration
COINMARKETCAP_API_KEY=mysecretkey
COINMARKETCAP_API_URL=https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest

# Database Configuration (for production)
# DATABASE_URL=sqlite:///db.sqlite3

# Email Configuration (optional)
# EMAIL_HOST=smtp.gmail.com
# EMAIL_PORT=587
# EMAIL_USE_TLS=True
# EMAIL_HOST_USER=your_email@gmail.com
# EMAIL_HOST_PASSWORD=your_app_password
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(".env file created successfully!")

def check_environment():
    """Check if environment variables are properly set"""
    print("🔍 Checking environment configuration...")
    
    try:
        from decouple import config
        
        # Check required variables
        secret_key = config('SECRET_KEY', default=None)
        api_key = config('COINMARKETCAP_API_KEY', default=None)
        api_url = config('COINMARKETCAP_API_URL', default=None)
        debug = config('DEBUG', default=True, cast=bool)
        
        print(f"SECRET_KEY: {'Set' if secret_key else 'Not set'}")
        print(f"COINMARKETCAP_API_KEY: {'Set' if api_key else 'Not set'}")
        print(f"COINMARKETCAP_API_URL: {'Set' if api_url else 'Not set'}")
        print(f"DEBUG: {debug}")
        
        if not secret_key or not api_key:
            print("Warning: Some required environment variables are not set!")
            return False
        
        print(" All environment variables are properly configured!")
        return True
        
    except ImportError:
        print(" python-decouple is not installed. Run: pip install python-decouple")
        return False
    except Exception as e:
        print(f" Error checking environment: {e}")
        return False

def show_help():
    """Show help information"""
    print("""
 Bitcoin Prices - Environment Setup

Available commands:
  python setup_env.py create    - Create .env file
  python setup_env.py check     - Check environment configuration
  python setup_env.py help      - Show this help message

Environment Variables:
  SECRET_KEY                    - Django secret key
  DEBUG                         - Debug mode (True/False)
  ALLOWED_HOSTS                 - Comma-separated list of allowed hosts
  COINMARKETCAP_API_KEY         - Your CoinMarketCap API key
  COINMARKETCAP_API_URL         - CoinMarketCap API endpoint

For production deployment:
  1. Copy .env.example to .env
  2. Update the values in .env with your production settings
  3. Set DEBUG=False
  4. Update ALLOWED_HOSTS with your domain
  5. Use a secure SECRET_KEY
""")

def main():
    """Main function"""
    if len(sys.argv) < 2:
        show_help()
        return
    
    command = sys.argv[1].lower()
    
    if command == 'create':
        create_env_file()
    elif command == 'check':
        check_environment()
    elif command == 'help':
        show_help()
    else:
        print(f" Unknown command: {command}")
        show_help()

if __name__ == '__main__':
    main()
