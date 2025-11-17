# Friends Screens

## Friends List Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ Splitwiser    [🔔] [👤]     │
│─────────────────────────────│
│                             │
│ Your Friends                │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Alex             │     │
│ │ You owe: $25        │     │
│ │ 3 groups together   │     │
│ │                [>]  │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Sarah            │     │
│ │ Owes you: $45       │     │
│ │ 2 groups together   │     │
│ │                [>]  │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Mike             │     │
│ │ All settled up      │     │
│ │ 1 group together    │     │
│ │                [>]  │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ + ADD FRIEND        │     │
│ └─────────────────────┘     │
│                             │
│ [HOME] [GROUPS] [FRIENDS]   │
└─────────────────────────────┘
```

### Description
List of user's friends with balance summaries and shared group information. Each friend card shows avatar, name, balance status, and shared group count with quick access to detailed view.

### Key Features
- Friend cards with balance status and shared groups count
- Color-coded balance indicators (owed vs owes)
- Quick balance overview across all groups
- Add friend functionality
- Search and filter capabilities
- Overall friends balance summary

### Component Breakdown

#### Friend Cards
- **Avatar**: Profile picture or initial placeholder
- **Name**: Friend's display name
- **Balance Status**: Net balance across all shared groups
- **Shared Groups**: Count of groups where both users are members
- **Navigation Arrow**: Tap to view friend details

#### Balance Indicators
- **You Owe**: Red text indicating debt to friend
- **Owes You**: Green text indicating friend's debt
- **Settled**: Neutral text for zero balance
- **Amount**: Precise balance amount with currency

#### Add Friend Section
- **Add Button**: Primary action to add new friends
- **Search Integration**: Find friends by email/phone
- **Import Contacts**: Sync with device contacts
- **QR Code**: Share personal QR for easy adding

### Interactions
- Tap friend card to view detailed friend profile
- Swipe friend card for quick actions (settle up, send reminder)
- Pull-to-refresh to update all friend balances
- Search friends by name or filter by balance status

## Friend Detail Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Alex              [⋮]     │
│─────────────────────────────│
│                             │
│ ┌─────────────────────┐     │
│ │       👤 Alex       │     │
│ │   alex@email.com    │     │
│ │                     │     │
│ │   Overall Balance   │     │
│ │   You owe: $25      │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │   SETTLE UP         │     │
│ └─────────────────────┘     │
│                             │
│ Shared Groups (3)           │
│ ┌─────────────────────┐     │
│ │ 🏠 Roommates        │     │
│ │ You owe: $15        │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ ✈️ Weekend Trip     │     │
│ │ You owe: $10        │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 🍽️ Dinner Club      │     │
│ │ All settled         │     │
│ └─────────────────────┘     │
│                             │
│ Recent Activity             │
│ ┌─────────────────────┐     │
│ │ Dinner - $60        │     │
│ │ Alex paid • 2 days  │     │
│ └─────────────────────┘     │
│                             │
└─────────────────────────────┘
```

### Description
Detailed view of a specific friend showing overall balance, shared groups with individual balances, recent activity, and settlement options. Provides comprehensive overview of financial relationship.

### Key Features
- Friend profile information with contact details
- Overall balance summary across all groups
- Shared groups list with individual balances
- Recent activity feed for shared expenses
- Settle up functionality for quick payments
- Direct messaging and contact options

### Component Breakdown

#### Friend Profile Card
- **Profile Picture**: Large avatar display
- **Contact Info**: Name, email, phone (if available)
- **Overall Balance**: Net amount across all shared groups
- **Quick Actions**: Message, call, settle up

#### Settle Up Button
- **Primary Action**: Prominent settlement initiation
- **Quick Settlement**: For simple equal splits
- **Advanced Settlement**: For complex multi-group balances

#### Shared Groups Section
- **Group Cards**: Name, emoji, individual balance per group
- **Navigation**: Tap to go to specific group details
- **Balance Breakdown**: Clear per-group balance display

#### Recent Activity
- **Activity Feed**: Recent expenses involving both users
- **Expense Details**: Amount, payer, timestamp, group context
- **Navigation**: Tap to view full expense details

#### Profile Actions Menu
- **Edit Friend**: Modify friend's display name or contact info
- **Send Reminder**: Gentle payment reminder notifications
- **Block/Remove**: Remove friend relationship with confirmation
- **Export History**: Download shared expense history

### Interactions
- Tap shared group to navigate to group details
- Tap recent activity to view expense details
- Settle up with payment method selection
- Contact friend through integrated communication
- Access profile management options

## Add Friend Screen

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Add Friend                │
│─────────────────────────────│
│                             │
│        Add a Friend         │
│                             │
│ Find by email or phone      │
│ ┌─────────────────────┐     │
│ │ [alex@email.com___] │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │    SEND INVITE      │     │
│ └─────────────────────┘     │
│                             │
│        or                   │
│                             │
│ ┌─────────────────────┐     │
│ │   IMPORT CONTACTS   │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │   SHARE QR CODE     │     │
│ └─────────────────────┘     │
│                             │
│ Your QR Code                │
│ ┌─────────────────────┐     │
│ │  ████████████████   │     │
│ │  ██  ██  ██    ██   │     │
│ │  ██████████████████ │     │
│ │  ██    ██  ██  ██   │     │
│ │  ████████████████   │     │
│ └─────────────────────┘     │
│                             │
│ Share this code so friends  │
│ can add you easily!         │
│                             │
└─────────────────────────────┘
```

### Description
Screen for adding new friends through various methods: email/phone invitation, contact import, or QR code sharing. Provides multiple convenient ways to expand friend network.

### Key Features
- Email/phone number search and invitation
- Contact list integration for easy friend discovery
- Personal QR code for easy friend addition
- Invitation tracking and status updates
- Multiple contact methods support

### Component Breakdown

#### Manual Addition
- **Search Field**: Email or phone number input
- **Validation**: Real-time format checking
- **Send Invite**: Send friend request via email/SMS
- **Status Tracking**: Pending, accepted, declined invitations

#### Contact Import
- **Permission Request**: Access to device contacts
- **Contact List**: Scrollable list of contacts with Splitwiser accounts
- **Bulk Invites**: Select multiple contacts for invitation
- **Smart Filtering**: Show only contacts not already friends

#### QR Code Sharing
- **Personal QR**: User's unique friend code
- **Share Options**: Social media, messaging, email sharing
- **Code Regeneration**: Refresh code for security
- **Scanner**: Option to scan friend's QR code

#### Invitation Management
- **Sent Invites**: List of pending outgoing invitations
- **Received Invites**: Incoming friend requests requiring response
- **History**: Past invitation activity
- **Privacy Controls**: Who can find/add user

### Interactions
- Search contacts with real-time filtering
- Select multiple contacts for bulk invitations
- Share QR code through various platforms
- Accept/decline incoming friend requests
- Resend or cancel pending invitations

## Friend Search Results

### Wireframe Sketch
```
┌─────────────────────────────┐
│ ← Search Results            │
│─────────────────────────────│
│                             │
│ Results for "alex@email"    │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Alex Johnson     │     │
│ │ alex@email.com      │     │
│ │ 2 mutual friends    │     │
│ │            [ADD]    │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Alex Smith       │     │
│ │ alexsmith@email.com │     │
│ │ No mutual friends   │     │
│ │            [ADD]    │     │
│ └─────────────────────┘     │
│                             │
│ People you may know         │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Sarah Williams   │     │
│ │ From your contacts  │     │
│ │ 5 mutual friends    │     │
│ │            [ADD]    │     │
│ └─────────────────────┘     │
│                             │
│ ┌─────────────────────┐     │
│ │ 👤 Mike Chen        │     │
│ │ Friend of Alex      │     │
│ │ 1 mutual friend     │     │
│ │            [ADD]    │     │
│ └─────────────────────┘     │
│                             │
└─────────────────────────────┘
```

### Description
Search results screen showing potential friends based on search query, with additional suggestions based on mutual connections and contact list matches.

### Key Features
- Search results based on email/phone query
- Mutual friends indication for trust building
- Contact-based suggestions
- Friend-of-friend recommendations
- Add friend functionality with status tracking

### Component Breakdown

#### Search Results
- **User Cards**: Profile info with mutual friends count
- **Contact Info**: Email or phone number display
- **Mutual Connections**: Shared friends for verification
- **Add Button**: Send friend request action

#### Suggestions Section
- **Contact Matches**: People from device contacts on Splitwiser
- **Mutual Friends**: Friends of existing friends
- **Social Connections**: Integration with social platforms
- **Geographic Proximity**: Nearby users (optional)

#### Privacy Considerations
- **Search Visibility**: User privacy settings respect
- **Contact Permissions**: Appropriate contact access handling
- **Suggestion Opt-out**: User control over discoverability

### Interactions
- Send friend requests with personalized messages
- View mutual friends for verification
- Filter suggestions by connection type
- Block or hide specific suggestions
- Access user profiles (if public) before adding
