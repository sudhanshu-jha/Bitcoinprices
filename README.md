# 🚀 Bitcoin Prices - 3D Crypto Dashboard [![Codacy Badge](https://api.codacy.com/project/badge/Grade/8ae052f10dba47ad91bf895b52eea74f)](https://www.codacy.com/app/sudhanshu-jha/Bitcoinprices?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=sudhanshu-jha/Bitcoinprices&amp;utm_campaign=Badge_Grade)

A modern Django web application that displays real-time cryptocurrency prices with stunning 3D visualizations using the CoinMarketCap API.

## ✨ Features

- 🎨 **3D Interactive UI** - Beautiful 3D cards with hover effects and animations
- 📊 **Real-time Data** - Live cryptocurrency prices from CoinMarketCap API
- 📱 **Responsive Design** - Works perfectly on desktop and mobile
- 🔒 **Secure Configuration** - Environment variables for sensitive data
- ⚡ **Fast Performance** - Optimized for speed and smooth animations

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd Bitcoinprices
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirement.txt
```

### 4. Environment Configuration
```bash
# Create environment file
python setup_env.py create

# Check environment setup
python setup_env.py check
```

### 5. Database Setup
```bash
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your 3D crypto dashboard!

## 🔧 Environment Variables

The application uses environment variables for secure configuration. Copy `.env.example` to `.env` and update the values:

```bash
# Django Settings
SECRET_KEY=your_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# CoinMarketCap API Configuration
COINMARKETCAP_API_KEY=your_coinmarketcap_api_key_here
COINMARKETCAP_API_URL=https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest
```

## 🎨 3D Features

- **Perspective Effects** - True 3D transforms with CSS perspective
- **Interactive Cards** - Hover effects that lift and rotate cards
- **Mouse Parallax** - Cards respond to mouse movement
- **Smooth Animations** - Professional easing and transitions
- **Gradient Backgrounds** - Beautiful color schemes
- **Responsive Grid** - Adaptive layout for all screen sizes

## 📊 API Integration

The app integrates with the CoinMarketCap Pro API to fetch:
- Real-time cryptocurrency prices
- Market capitalization data
- 24-hour trading volume
- Price change percentages
- Market rankings

## 🚀 Deployment

For production deployment:

1. Set `DEBUG=False` in your environment
2. Update `ALLOWED_HOSTS` with your domain
3. Use a secure `SECRET_KEY`
4. Configure your production database
5. Set up proper logging and monitoring

## 🛠️ Development

### Environment Management
```bash
# Check environment status
python setup_env.py check

# Create new environment file
python setup_env.py create

# Show help
python setup_env.py help
```

### Project Structure
```
Bitcoinprices/
├── bitcoin/           # Main Django app
├── crypto/           # Project settings
├── templates/        # HTML templates
├── .env              # Environment variables (not in git)
├── .env.example      # Environment template
├── setup_env.py      # Environment management script
└── requirement.txt   # Python dependencies
```


## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 👨‍💻 Author

Created by [sudhanshujha](https://github.com/sudhanshu-jha)
