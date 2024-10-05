# CharitOn

CharitOn is a web application designed to connect donors, institutes (like orphanages, elderly homes, or organizations providing free food), and suppliers to ensure efficient and transparent donations. It facilitates donations without direct monetary transfers to the needy, reducing the risk of misuse of funds. The app was developed during a 30-hour hackathon conducted by Vidyavardhini College of Engineering and Technology.

## Features

1. **Institutes Raise Requirements**: Institutes can specify the items they need, such as groceries or medical supplies.
2. **Donor Selection**: Donors can choose to contribute by specifying item type and quantity (e.g., 10 kg of rice).
3. **Shopkeeper Involvement**: The request is routed to nearby shopkeepers, who will fulfill the order and ship the items.
4. **No Direct Money Transfer**: Funds go directly to the shopkeeper, ensuring transparency.
5. **Distribution of Donations**: For larger donations, orders are distributed among different shops to avoid monopoly and fraud.
6. **Anomaly Detection**: The system tracks consumption per institute and flags any unusual patterns.
7. **Quality Feedback**: Institutes can provide feedback on the quality of the items received.

## Workflow

1. Institutes create a request for specific items.
2. Donors select a request and donate in terms of fixed amounts or item quantities.
3. The selected shopkeeper packs and ships the required items to the institute.
4. Money is transferred directly to the shopkeeper.
5. Feedback is collected from the institute regarding the quality of items supplied.

## Technical Stack

- Frontend: HTML, CSS, JavaScript
- Backend: Python(Flask)
- Database: SQLite3
- Payment Integration: (Stripe)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/HenriquesLee/VH24-BYTEBENDERS.git
   cd VH24-BYTEBENDERS
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python manage.py runserver
   ```

4. Open your browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```
