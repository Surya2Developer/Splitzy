# Main Navigation & Home Screen

## Home Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ Splitwiser    [🔔] [👤]     │
│─────────────────────────────│
│                             │
│ Overall Balance             │
│ ┌─────────────────────┐     │
│ │ You are owed: $125  │     │
│ └─────────────────────┘     │
│                             │
│ Recent Activity             │
│ ┌─────────────────────┐     │
│ │ Dinner with Alex    │     │
│ │ You paid: $60       │     │
│ │ You lent: $30       │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ Weekend Trip        │     │
│ │ Alex paid: $45      │     │
│ │ You owe: $15        │     │
│ └─────────────────────┘     │
│                             │
│ Monthly Summary             │
│ [Chart visualization]       │
│                             │
│                             │
│ [HOME] [GROUPS] [FRIENDS]   │
└─────────────────────────────┘
```

### Description
Dashboard showing overall balance summary in an elevated card, recent activity feed with transaction details, and monthly spending analytics. Top bar includes notification bell icon and profile avatar. Bottom navigation with three main tabs.

### Key Features
- App bar with notification icon (badge for unread count) and profile avatar
- Overall balance card with elevated surface and prominent typography
- Activity feed with individual transaction cards showing payment direction
- Chart component for spending analytics (monthly/weekly views)
- Bottom navigation bar with three primary tabs
- Pull-to-refresh functionality for updating data

### Component Breakdown

#### App Bar
- **Title**: "Splitwiser" using `titleLarge` typography
- **Notification Icon**: Bell icon with badge for unread notifications
- **Profile Avatar**: User profile picture, tappable for profile menu
- **Background**: Surface color with subtle elevation

#### Overall Balance Card
- **Card Type**: Elevated card with level 1 elevation
- **Content**: Balance amount with color coding (green for positive, red for negative)
- **Typography**: `headlineMedium` for amount, `bodyMedium` for label
- **Action**: Tappable to view detailed balance breakdown

#### Recent Activity Section
- **Section Header**: "Recent Activity" using `titleMedium`
- **Activity Cards**: Individual transaction cards with:
  - Expense description (`titleSmall`)
  - Amount and payment direction (`bodyMedium`)
  - Participant information (`bodySmall`)
  - Timestamp (`labelSmall`)

#### Monthly Summary
- **Chart Component**: Interactive spending chart
- **Chart Types**: Bar chart, pie chart, or line chart options
- **Data Views**: Current month, last 3 months, yearly view
- **Categories**: Spending breakdown by expense categories

#### Bottom Navigation
- **Tabs**: Home, Groups, Friends
- **Active State**: Primary color indication
- **Icons**: Material Design icons with labels
- **Badge Support**: Notification badges on tabs when relevant

### Interactions
- **Pull to Refresh**: Swipe down to refresh all data
- **Card Taps**: Navigate to detailed views
- **Notification Tap**: Open notifications screen
- **Profile Tap**: Open profile/settings menu
- **Chart Interaction**: Tap chart segments for details

### Data States
- **Loading State**: Skeleton loading for cards
- **Empty State**: Friendly message for new users
- **Error State**: Retry mechanism for failed loads
- **Offline State**: Cached data with sync indicator

## Notifications Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Notifications             │
│─────────────────────────────│
│                             │
│ Today                       │
│ ┌─────────────────────┐     │
│ │ 🔔 Alex added expense │     │
│ │ "Dinner" - $45      │     │
│ │ Weekend Trip • 2h ago │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 💰 Sarah settled up │     │
│ │ Paid you $25        │     │
│ │ Apartment • 4h ago  │     │
│ └─────────────────────┘     │
│                             │
│ Yesterday                   │
│ ┌─────────────────────┐     │
│ │ 👥 New group invite │     │
│ │ "Book Club"         │     │
│ │ From John • 1d ago  │     │
│ └─────────────────────┘     │
│                             │
│                             │
│ [Mark all as read]          │
│                             │
└─────────────────────────────┘
```

### Description
Chronologically organized notifications with clear visual hierarchy and actionable items.

### Key Features
- Grouped by date sections
- Different notification types with appropriate icons
- Clear call-to-action for each notification
- Mark as read functionality
- Deep linking to relevant screens

### Notification Types
- **Expense Added**: New expense in a group
- **Payment Settled**: Someone paid their debt
- **Group Invite**: Invitation to join a group
- **Balance Update**: Significant balance changes
- **Reminder**: Payment due reminders

## Profile Menu

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Profile                   │
│─────────────────────────────│
│                             │
│    [Large Avatar]           │
│    John Doe                 │
│    john.doe@email.com       │
│                             │
│ ┌─────────────────────┐     │
│ │ 📝 Edit Profile     │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 💳 Payment Methods  │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ ⚙️ Settings         │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 🌙 Dark Mode        │ ⚬  │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 🚪 Log Out          │     │
│ └─────────────────────┘     │
│                             │
└─────────────────────────────┘
```

### Description
User profile management with key account actions and preferences.

### Key Features
- Large profile picture with edit capability
- Quick access to frequently used settings
- Dark mode toggle
- Clear logout option with confirmation

### Menu Options
- **Edit Profile**: Change name, email, profile picture
- **Payment Methods**: Manage linked payment accounts
- **Settings**: App preferences and privacy settings
- **Dark Mode**: Toggle between light and dark themes
- **Log Out**: Sign out with confirmation dialog

## Activity Detail Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Activity Details          │
│─────────────────────────────│
│                             │
│ Dinner at Luigi's           │
│ $85.50 • Food              │
│ June 28, 2024 • 7:30 PM    │
│                             │
│ ┌─────────────────────┐     │
│ │ Paid by: You        │     │
│ │ Split: Equally (4)  │     │
│ │ Group: Weekend Trip │     │
│ └─────────────────────┘     │
│                             │
│ Split Details               │
│ ┌─────────────────────┐     │
│ │ You         $21.38  │     │
│ │ Alex        $21.38  │     │
│ │ Sarah       $21.37  │     │
│ │ John        $21.37  │     │
│ └─────────────────────┘     │
│                             │
│ [ Receipt Image ]           │
│                             │
│                             │
│ [EDIT] [DELETE]             │
│                             │
└─────────────────────────────┘
```

### Description
Detailed view of a single expense showing all participants, amounts, and metadata.

### Key Features
- Complete expense information
- Participant breakdown with individual amounts
- Receipt image display
- Edit/delete actions for expense creator
- Group context and navigation

This home navigation structure provides users with quick access to their most important information while maintaining clear paths to detailed views and actions.
