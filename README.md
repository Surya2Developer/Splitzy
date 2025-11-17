# Splitzy - Smart Expense Splitting App 

Splitzy is a modern expense tracking and splitting application built with Expo/React Native. It simplifies group expense management, making it easy to track shared costs, split bills fairly, and settle debts among friends, roommates, or travel groups.

##  Key Features

- **Multi-Platform**: Built with Expo for iOS, Android, and Web
- **Smart Expense Splitting**: Flexible splitting options (equal, percentage, custom amounts)
- **Group Management**: Create and manage multiple expense groups
- **Real-Time Sync**: Live updates across all devices
- **Secure Authentication**: Email/password and Google OAuth integration
- **Receipt Management**: Upload and attach receipts to expenses
- **Debt Simplification**: Advanced algorithms to minimize payment transactions
- **Multi-Currency Support**: Handle expenses in different currencies
- **Settlement Tracking**: Record and track payments between group members

##  Architecture

### Frontend (Expo/React Native)
- **Framework**: Expo with TypeScript
- **Navigation**: File-based routing
- **State Management**: React Context/Redux (TBD)
- **Authentication**: Secure token storage with refresh token rotation
- **UI**: Modern, responsive design

### Backend (FastAPI)
- **Framework**: FastAPI with Python
- **Database**: MongoDB for document storage
- **Authentication**: JWT with refresh token rotation
- **File Storage**: S3-compatible storage for receipts
- **Real-time**: WebSocket support for live updates

### Key Services
1. **Authentication Service**: Secure login with email/password and Google OAuth
2. **User Service**: Profile management and preferences
3. **Group Service**: Group creation, member management, and invitations
4. **Expense Service**: Expense tracking, splitting algorithms, and attachments
5. **Settlement Service**: Payment recording and debt resolution
6. **Notification Service**: Real-time updates and notifications

# Demo video
https://github.com/user-attachments/assets/84544cf7-dfdc-4c72-b7bb-4650739b98fc

##  Getting Started

### Prerequisites
- Node.js (v18 or higher)
- Expo CLI
- MongoDB (for backend)
- Python 3.9+ (for backend)

### Development Setup

#### Frontend (Expo App)

1. **Install dependencies**:
   ```bash
   npm install
   ```

2. **Start development server**:
   ```bash
   npm start
   ```

#### Backend (FastAPI)

1. **Set up Python environment**:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your MongoDB connection string and other config
   ```

4. **Start the server**:
   ```bash
   uvicorn main:app --reload
   ```

##  Features in Detail

### Authentication & Security
- **Secure Token Storage**: Access tokens in memory, refresh tokens in secure storage
- **Token Rotation**: Automatic refresh token rotation for enhanced security
- **Multi-Provider Auth**: Support for email/password and Google OAuth
- **Session Management**: Track and revoke active sessions across devices

### Expense Management
- **Flexible Splitting**: Equal splits, percentage-based, or custom amounts
- **Receipt Attachments**: Upload and store receipt images
- **Categories & Tags**: Organize expenses with custom categories
- **Multi-Currency**: Handle expenses in different currencies with real-time conversion
- **Edit History**: Track all changes to expenses with full audit trail

### Group Features
- **Invite System**: Email-based invitations with secure tokens
- **Role Management**: Admin and member roles with different permissions
- **Group Settings**: Customizable group preferences and currencies
- **Member Management**: Add, remove, and manage group members

### Smart Debt Resolution
- **Debt Simplification**: Advanced graph algorithms to minimize transactions
- **Settlement Tracking**: Record real payments and update balances
- **Balance Overview**: Clear visualization of who owes what to whom
- **Payment Reminders**: Optional notifications for pending settlements

##  Development

### Project Structure
```
Splitzy/
├── app/                    # Expo app source code
├── backend/               # FastAPI backend (when implemented)
├── docs/                  # Technical documentation
│   ├── auth-service.md   # Authentication service design
│   └── micro-plan.md     # Detailed API specifications
└── README.md
```

### API Documentation
- **Authentication**: See `docs/auth-service.md` for detailed auth flow
- **API Endpoints**: See `docs/micro-plan.md` for complete API specification
- **Interactive Docs**: FastAPI auto-generates docs at `/docs` when backend is running

### Technology Stack
- **Frontend**: Expo, React Native, TypeScript
- **Backend**: FastAPI, Python, MongoDB
- **Authentication**: JWT with refresh tokens, Firebase Auth (Google)
- **Storage**: MongoDB for data, S3-compatible for file storage
- **Real-time**: WebSockets for live updates

