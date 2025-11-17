# React Native + Expo Folder Structure

## Overview
This document outlines the recommended folder structure for the Splitwiser mobile app, following best practices for modularity, testability, and scalability using a **feature-based domain architecture**.

## 📁 Complete Folder Structure

```
/app
├── navigation/                    # Central navigation config (React Navigation)
│   ├── AppNavigator.tsx          # Main app navigation container
│   ├── AuthNavigator.tsx         # Authentication flow navigation
│   ├── MainTabNavigator.tsx      # Bottom tab navigation
│   ├── GroupsNavigator.tsx       # Groups stack navigation
│   ├── ExpenseNavigator.tsx      # Expense creation flow navigation
│   └── types.ts                  # Navigation type definitions
│
├── screens/                      # Screen components grouped by feature
│   ├── Auth/
│   │   ├── LoginScreen.tsx
│   │   ├── SignupScreen.tsx
│   │   ├── ForgotPasswordScreen.tsx
│   │   └── OnboardingScreen.tsx
│   │
│   ├── Home/
│   │   ├── HomeScreen.tsx
│   │   ├── NotificationsScreen.tsx
│   │   └── ActivityDetailScreen.tsx
│   │
│   ├── Groups/
│   │   ├── GroupsListScreen.tsx
│   │   ├── GroupDetailsScreen.tsx
│   │   ├── CreateGroupScreen.tsx
│   │   ├── JoinGroupScreen.tsx
│   │   ├── GroupSettingsScreen.tsx
│   │   └── GroupMembersScreen.tsx
│   │
│   ├── Expenses/
│   │   ├── AddExpenseStep1Screen.tsx     # Basic info (amount, description, category)
│   │   ├── AddExpenseStep2Screen.tsx     # Payment selection (who paid)
│   │   ├── AddExpenseStep3Screen.tsx     # Split options (equal/unequal)
│   │   ├── ExpenseDetailScreen.tsx
│   │   ├── ExpenseHistoryScreen.tsx
│   │   └── EditExpenseScreen.tsx
│   │
│   ├── Friends/
│   │   ├── FriendsScreen.tsx
│   │   ├── FriendDetailScreen.tsx
│   │   ├── AddFriendScreen.tsx
│   │   └── FriendRequestsScreen.tsx
│   │
│   ├── Settlements/
│   │   ├── SettlementsScreen.tsx
│   │   ├── OptimizedSettlementsScreen.tsx
│   │   ├── SettleUpScreen.tsx
│   │   ├── PaymentMethodScreen.tsx
│   │   └── PaymentConfirmationScreen.tsx
│   │
│   └── Settings/
│       ├── ProfileScreen.tsx
│       ├── PreferencesScreen.tsx
│       ├── PaymentMethodsScreen.tsx
│       └── SecurityScreen.tsx
│
├── components/                   # Reusable UI components
│   ├── common/                   # Generic Material 3 components
│   │   ├── Button/
│   │   │   ├── Button.tsx
│   │   │   ├── Button.styles.ts
│   │   │   └── Button.types.ts
│   │   │
│   │   ├── Card/
│   │   │   ├── Card.tsx
│   │   │   └── Card.styles.ts
│   │   │
│   │   ├── TextField/
│   │   │   ├── TextField.tsx
│   │   │   ├── TextField.styles.ts
│   │   │   └── TextField.types.ts
│   │   │
│   │   ├── RadioGroup/
│   │   ├── Checkbox/
│   │   ├── Avatar/
│   │   ├── Badge/
│   │   ├── Chip/
│   │   ├── Snackbar/
│   │   ├── Modal/
│   │   └── LoadingSpinner/
│   │
│   ├── layout/                   # Layout components
│   │   ├── AppBar/
│   │   │   ├── AppBar.tsx
│   │   │   └── AppBar.styles.ts
│   │   │
│   │   ├── BottomNavigation/
│   │   │   ├── BottomNavigation.tsx
│   │   │   └── BottomNavigation.styles.ts
│   │   │
│   │   ├── Screen/
│   │   │   ├── Screen.tsx        # Base screen wrapper with common layout
│   │   │   └── Screen.styles.ts
│   │   │
│   │   ├── FloatingActionButton/
│   │   ├── Container/
│   │   └── SafeAreaWrapper/
│   │
│   └── feature/                  # Feature-specific components
│       ├── expenses/
│       │   ├── ExpenseCard/
│       │   │   ├── ExpenseCard.tsx
│       │   │   ├── ExpenseCard.styles.ts
│       │   │   └── ExpenseCard.types.ts
│       │   │
│       │   ├── ExpenseForm/
│       │   ├── ExpenseList/
│       │   ├── SplitOptions/
│       │   │   ├── EqualSplit.tsx
│       │   │   ├── UnequalSplit.tsx
│       │   │   ├── SharesSplit.tsx
│       │   │   ├── PercentageSplit.tsx
│       │   │   └── ExactAmountSplit.tsx
│       │   │
│       │   ├── CategorySelector/
│       │   ├── ReceiptCapture/
│       │   └── PaymentSelector/
│       │
│       ├── groups/
│       │   ├── GroupCard/
│       │   ├── GroupList/
│       │   ├── GroupHeader/
│       │   ├── GroupSummary/
│       │   ├── MemberList/
│       │   └── InviteMember/
│       │
│       ├── friends/
│       │   ├── FriendCard/
│       │   ├── FriendList/
│       │   ├── BalanceIndicator/
│       │   └── FriendSearch/
│       │
│       ├── settlements/
│       │   ├── SettlementCard/
│       │   ├── OptimizedSettlementList/
│       │   ├── PaymentMethodSelector/
│       │   ├── BalanceSummary/
│       │   └── DebtVisualization/
│       │
│       └── analytics/
│           ├── SpendingChart/
│           ├── MonthlyChart/
│           └── CategoryBreakdown/
│
├── services/                     # API service calls and business logic
│   ├── api/
│   │   ├── client.ts            # Base API client configuration
│   │   ├── interceptors.ts      # Request/response interceptors
│   │   └── endpoints.ts         # API endpoint constants
│   │
│   ├── auth/
│   │   ├── authService.ts       # Authentication API calls
│   │   ├── googleAuth.ts        # Google Sign-in integration
│   │   └── tokenService.ts      # Token management
│   │
│   ├── groups/
│   │   ├── groupService.ts      # Group CRUD operations
│   │   ├── memberService.ts     # Group member management
│   │   └── inviteService.ts     # Group invitation handling
│   │
│   ├── expenses/
│   │   ├── expenseService.ts    # Expense CRUD operations
│   │   ├── splitService.ts      # Split calculation logic
│   │   └── receiptService.ts    # Receipt processing
│   │
│   ├── settlements/
│   │   ├── settlementService.ts # Settlement calculations
│   │   ├── optimizationService.ts # Debt optimization algorithms
│   │   └── paymentService.ts    # Payment recording
│   │
│   ├── users/
│   │   ├── userService.ts       # User profile management
│   │   └── friendsService.ts    # Friends management
│   │
│   └── notifications/
│       ├── notificationService.ts
│       ├── pushNotifications.ts
│       └── emailService.ts
│
├── hooks/                        # Reusable custom hooks
│   ├── auth/
│   │   ├── useAuth.ts           # Authentication state and methods
│   │   ├── useGoogleAuth.ts     # Google Sign-in hook
│   │   └── useTokenRefresh.ts   # Automatic token refresh
│   │
│   ├── data/
│   │   ├── useGroups.ts         # Groups data fetching and management
│   │   ├── useExpenses.ts       # Expenses data operations
│   │   ├── useFriends.ts        # Friends data management
│   │   ├── useSettlements.ts    # Settlement calculations
│   │   └── useNotifications.ts  # Notifications management
│   │
│   ├── ui/
│   │   ├── useTheme.ts          # Theme switching and customization
│   │   ├── useModal.ts          # Modal state management
│   │   ├── useSnackbar.ts       # Snackbar notifications
│   │   └── useKeyboard.ts       # Keyboard handling
│   │
│   └── utils/
│       ├── useDebounce.ts       # Debounced values
│       ├── useLocalStorage.ts   # Local storage operations
│       ├── useNetworkStatus.ts  # Network connectivity
│       └── usePermissions.ts    # Device permissions
│
├── store/                        # Global state management
│   ├── slices/                   # Redux Toolkit slices
│   │   ├── authSlice.ts         # User authentication state
│   │   ├── groupSlice.ts        # Groups data state
│   │   ├── expenseSlice.ts      # Expenses state
│   │   ├── friendSlice.ts       # Friends data state
│   │   ├── settlementSlice.ts   # Settlement calculations state
│   │   ├── uiSlice.ts          # UI state (modals, loading, etc.)
│   │   └── notificationSlice.ts # Notifications state
│   │
│   ├── middleware/
│   │   ├── authMiddleware.ts    # Authentication middleware
│   │   ├── apiMiddleware.ts     # API call middleware
│   │   └── persistMiddleware.ts # Data persistence middleware
│   │
│   ├── selectors/
│   │   ├── authSelectors.ts     # Authentication selectors
│   │   ├── groupSelectors.ts    # Group data selectors
│   │   └── expenseSelectors.ts  # Expense data selectors
│   │
│   ├── hooks.ts                 # Typed Redux hooks
│   ├── store.ts                 # Redux store configuration
│   └── types.ts                 # Redux state type definitions
│
├── assets/                       # Static assets
│   ├── fonts/                   # Custom fonts
│   │   ├── Roboto-Regular.ttf
│   │   ├── Roboto-Medium.ttf
│   │   └── Roboto-Bold.ttf
│   │
│   ├── images/                  # Static images
│   │   ├── logo/
│   │   ├── icons/
│   │   ├── illustrations/
│   │   └── placeholders/
│   │
│   ├── lottie/                  # Animation files
│   │   ├── loading.json
│   │   ├── success.json
│   │   └── empty-state.json
│   │
│   └── audio/                   # Sound files
│       ├── notification.mp3
│       └── success.mp3
│
├── constants/                    # App constants and configuration
│   ├── theme/
│   │   ├── colors.ts           # Material 3 color palette
│   │   ├── typography.ts       # Typography scale and styles
│   │   ├── spacing.ts          # Spacing system
│   │   ├── shadows.ts          # Elevation and shadow styles
│   │   └── theme.ts            # Main theme configuration
│   │
│   ├── api.ts                  # API endpoints and configuration
│   ├── categories.ts           # Expense categories
│   ├── currencies.ts           # Supported currencies
│   ├── dimensions.ts           # Screen dimensions and breakpoints
│   └── validation.ts           # Validation rules and messages
│
├── utils/                       # Utility functions and helpers
│   ├── formatters/
│   │   ├── currency.ts         # Currency formatting
│   │   ├── date.ts             # Date formatting
│   │   ├── number.ts           # Number formatting
│   │   └── text.ts             # Text manipulation
│   │
│   ├── validators/
│   │   ├── email.ts            # Email validation
│   │   ├── password.ts         # Password validation
│   │   ├── amount.ts           # Amount validation
│   │   └── forms.ts            # Form validation schemas
│   │
│   ├── calculations/
│   │   ├── splitCalculator.ts  # Expense split calculations
│   │   ├── balanceCalculator.ts # Balance calculations
│   │   ├── settlementOptimizer.ts # Settlement optimization
│   │   └── analytics.ts        # Analytics calculations
│   │
│   ├── storage/
│   │   ├── asyncStorage.ts     # AsyncStorage helpers
│   │   ├── secureStorage.ts    # Secure storage for sensitive data
│   │   └── cache.ts            # Caching utilities
│   │
│   ├── permissions/
│   │   ├── camera.ts           # Camera permissions
│   │   ├── notifications.ts    # Notification permissions
│   │   └── contacts.ts         # Contacts permissions
│   │
│   └── helpers/
│       ├── deviceInfo.ts       # Device information utilities
│       ├── network.ts          # Network utilities
│       ├── deepLinking.ts      # Deep linking handlers
│       └── errorHandling.ts    # Error handling utilities
│
├── types/                       # TypeScript type definitions
│   ├── api.ts                  # API response types
│   ├── entities.ts             # Business entity types
│   ├── navigation.ts           # Navigation parameter types
│   ├── forms.ts                # Form data types
│   └── common.ts               # Common shared types
│
├── config/                      # App configuration
│   ├── env.ts                  # Environment configuration
│   ├── firebase.ts             # Firebase configuration
│   ├── analytics.ts            # Analytics configuration
│   └── notifications.ts        # Push notifications configuration
│
├── __tests__/                   # Test files
│   ├── components/             # Component tests
│   ├── screens/                # Screen tests
│   ├── hooks/                  # Hook tests
│   ├── services/               # Service tests
│   ├── utils/                  # Utility tests
│   └── __mocks__/              # Mock files
│
├── App.tsx                      # Root application component
├── index.js                     # Entry point
├── app.json                     # Expo configuration
├── package.json                 # Dependencies and scripts
├── tsconfig.json               # TypeScript configuration
├── babel.config.js             # Babel configuration
├── metro.config.js             # Metro bundler configuration
└── .env                        # Environment variables
```

## 🎯 Key Architecture Principles

### 1. Feature-Based Organization
- Screens, components, and logic for each feature are grouped together
- Easier to locate and maintain related code
- Supports team collaboration with clear ownership boundaries

### 2. Separation of Concerns
- **Screens**: UI components that represent full screens
- **Components**: Reusable UI elements
- **Services**: Business logic and API interactions
- **Hooks**: Reusable stateful logic
- **Store**: Global state management
- **Utils**: Pure functions and helpers

### 3. Material 3 Compliance
- Theme system built around Material 3 design tokens
- Component variants following Material 3 specifications
- Consistent spacing, typography, and color usage

### 4. TypeScript First
- Comprehensive type definitions for all entities
- Type-safe navigation parameters
- Strongly typed API responses and form data

### 5. Testing Strategy
- Collocated test files with source code
- Comprehensive testing for business logic
- Component testing with React Native Testing Library
- E2E testing for critical user flows

## 📱 Screen Organization

### Navigation Structure
```
App
├── AuthNavigator (Stack)
│   ├── LoginScreen
│   ├── SignupScreen
│   └── OnboardingScreen
│
└── MainTabNavigator (Bottom Tabs)
    ├── HomeTab (Stack)
    │   ├── HomeScreen
    │   ├── NotificationsScreen
    │   └── ActivityDetailScreen
    │
    ├── GroupsTab (Stack)
    │   ├── GroupsListScreen
    │   ├── GroupDetailsScreen
    │   ├── CreateGroupScreen
    │   ├── JoinGroupScreen
    │   └── ExpenseFlow (Modal Stack)
    │       ├── AddExpenseStep1Screen
    │       ├── AddExpenseStep2Screen
    │       └── AddExpenseStep3Screen
    │
    └── FriendsTab (Stack)
        ├── FriendsScreen
        ├── FriendDetailScreen
        └── SettlementFlow (Modal Stack)
            ├── SettlementsScreen
            ├── OptimizedSettlementsScreen
            └── SettleUpScreen
```

## 🔧 Development Workflow

### Component Development
1. Create component folder with TypeScript file
2. Define props interface in `.types.ts` file
3. Implement styles in `.styles.ts` file
4. Add component tests in `__tests__` folder
5. Export from index file for clean imports

### Screen Development
1. Create screen component in appropriate feature folder
2. Implement navigation types for parameters
3. Connect to global state via hooks
4. Add business logic via custom hooks
5. Style with Material 3 theme system

### State Management
1. Define entity types in `types/` folder
2. Create Redux slice with actions and reducers
3. Implement selectors for derived state
4. Create custom hooks for component integration
5. Add middleware for side effects

## 🚀 Performance Considerations

### Code Splitting
- Lazy load screens using React Navigation
- Split large components into smaller chunks
- Use dynamic imports for heavy libraries

### Optimization Strategies
- Implement FlatList for large data sets
- Use React.memo for expensive components
- Optimize image loading with progressive enhancement
- Cache API responses with React Query

### Bundle Management
- Minimize app bundle size with tree shaking
- Use Hermes JavaScript engine for better performance
- Implement over-the-air updates with Expo Updates

This folder structure ensures maintainability, scalability, and follows React Native best practices while supporting the Material 3 design system implementation.
