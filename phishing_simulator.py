from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Updated HTML structure with more realistic phishing content
mailbox_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Mailbox</title>
    <style>
        body {
            font-family: Segoe UI, Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }
        .mailbox {
            display: flex;
            height: 100vh;
        }
        /* Left panel (email list) */
        .email-list {
            width: 300px;
            background-color: #f3f3f3;
            overflow-y: scroll;
            padding: 15px;
            border-right: 1px solid #ddd;
        }
        .email-item {
            padding: 15px;
            border-bottom: 1px solid #ddd;
            cursor: pointer;
            background-color: #f9f9f9;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .email-item:hover {
            background-color: #e1e1e1;
        }
        /* Right panel (email content) */
        .email-content {
            flex-grow: 1;
            padding: 20px;
            background-color: white;
            overflow-y: auto;
        }
        .header {
            background-color: #0078d4;
            color: white;
            padding: 10px;
            text-align: center;
            font-size: 20px;
        }
        .back-button {
            background-color: #ccc;
            color: #333;
            padding: 10px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
            margin-top: 20px;
        }
        .back-button:hover {
            background-color: #999;
        }
    </style>
</head>
<body>
    <div class="mailbox">
        <!-- Left panel with list of emails -->
        <div class="email-list">
            <div class="email-item" onclick="showEmail(1)">
                <strong>Urgent Request from Your CEO</strong>
            </div>
            <div class="email-item" onclick="showEmail(2)">
                <strong>Legal Action Regarding Company Data Breach</strong>
            </div>
            <div class="email-item" onclick="showEmail(3)">
                <strong>Account Lockout Alert</strong>
            </div>
        </div>

        <!-- Right panel with email content -->
        <div class="email-content">
            <div class="header" id="email-header">Inbox</div>
            <div class="email-view" id="email-1" style="display:none;">
                <h3>Urgent Request from Your CEO</h3>
                <p>Dear [Employee Name],</p>
                <p>I need you to urgently wire $15,000 to our supplier for an outstanding payment. Please ensure that the transfer is made immediately as it’s time-sensitive. The bank account details are below:</p>
                <ul>
                    <li>Account Name: Global Suppliers Ltd</li>
                    <li>Account Number: 987654321</li>
                    <li>Bank: XYZ International Bank</li>
                </ul>
                <p>This is a high-priority request that needs to be completed by the end of the day. Please confirm once the transfer is done. Let me know if you have any questions.</p>
                <p>Best regards,<br>
                [CEO's Name]<br>
                CEO, [Company Name]</p>
                <p><a href="/phishing_failure?reason=spear_phishing" class="back-button">Click here to confirm the transfer</a></p>
                <button class="back-button" onclick="backToInbox()">Back to Inbox</button>
            </div>
            <div class="email-view" id="email-2" style="display:none;">
                <h3>Legal Action Regarding Company Data Breach</h3>
                <p>Dear [Executive Name],</p>
                <p>This is an urgent legal notice regarding a significant data breach within your organization. Our firm has been assigned to handle this matter, and immediate action is required to avoid severe legal consequences.</p>
                <p>Attached, you will find a legal document detailing the breach and what actions must be taken. Failure to comply will result in penalties for the company.</p>
                <p>Please review the document and confirm your next steps as soon as possible. For your convenience, click the link below to access the full legal document:</p>
                <p><a href="/phishing_failure?reason=whaling" class="back-button">View Legal Document</a></p>
                <p>Regards,<br>
                Legal Department, [Firm Name]</p>
                <button class="back-button" onclick="backToInbox()">Back to Inbox</button>
            </div>
            <div class="email-view" id="email-3" style="display:none;">
                <h3>Account Lockout Alert</h3>
                <p>Dear [User Name],</p>
                <p>We noticed suspicious activity on your account and have temporarily locked it for security reasons. To regain access, you must verify your identity by following the instructions below.</p>
                <p>Click the link below to unlock your account and regain full access:</p>
                <p><a href="/phishing_failure?reason=social_engineering" class="back-button">Unlock Your Account</a></p>
                <p>If you did not initiate this request, please contact our support team immediately.</p>
                <p>Best regards,<br>
                Account Security Team</p>
                <button class="back-button" onclick="backToInbox()">Back to Inbox</button>
            </div>
        </div>
    </div>

    <script>
        function showEmail(emailId) {
            // Hide all email views
            let allEmails = document.querySelectorAll('.email-view');
            allEmails.forEach(email => email.style.display = 'none');

            // Show the clicked email view
            document.getElementById('email-' + emailId).style.display = 'block';

            // Change the header text
            let header = document.getElementById('email-header');
            if (emailId === 1) {
                header.textContent = 'Urgent Request from Your CEO';
            } else if (emailId === 2) {
                header.textContent = 'Legal Action Regarding Company Data Breach';
            } else if (emailId === 3) {
                header.textContent = 'Account Lockout Alert';
            }
        }

        function backToInbox() {
            // Hide all email views
            let allEmails = document.querySelectorAll('.email-view');
            allEmails.forEach(email => email.style.display = 'none');

            // Show the inbox list
            document.getElementById('email-header').textContent = 'Inbox';
        }
    </script>
</body>
</html>
'''

# Failure page after clicking on phishing links
failure_page = '''
<!DOCTYPE html>
<html>
<head>
    <title>Phishing Simulation - Failed</title>
    <style>
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 40px auto;
            background-color: #ffffff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h2 {
            font-size: 28px;
            color: #d9534f;
            margin-bottom: 20px;
            text-align: center;
        }

        .reason {
            font-size: 18px;
            line-height: 1.6;
        }

        .reason strong {
            font-weight: bold;
            color: #d9534f;
        }

        ul {
            padding-left: 20px;
            margin-bottom: 30px;
        }

        ul li {
            margin-bottom: 10px;
            font-size: 16px;
        }

        .btn {
            background-color: #0078d4;
            color: white;
            padding: 10px 20px;
            text-align: center;
            border-radius: 5px;
            font-size: 16px;
            display: inline-block;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #005a8d;
        }

        .footer {
            text-align: center;
            font-size: 14px;
            color: #777;
            margin-top: 30px;
        }
    </style>
</head>
<body>

    <div class="container">
        <h2>You've Failed the Phishing Simulation!</h2>

        <p class="reason"><strong>Reason:</strong> {{ reason_description }}</p>
        
        <p>This was a simulation to help you recognize phishing attempts. Here's why this attempt was dangerous:</p>
        <ul>
            <li>{{ reason }}</li>
        </ul>

        <p>Stay cautious when dealing with unexpected requests, especially involving money, confidential information, or urgency.</p>

        <a href="/" class="btn">Back to Inbox</a>
    </div>

</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(mailbox_page)

@app.route('/phishing_failure')
def phishing_failure():
    reason = request.args.get('reason')

    # Define descriptions for each reason
    reason_descriptions = {
        'spear_phishing': "The CEO would never ask employees to wire money through email, especially with such urgency. Always confirm suspicious requests with your manager in person or via phone.",
        'whaling': "Legal documents should never be accessed via unsolicited email links. Always verify such communications by contacting the firm directly.",
        'social_engineering': "Legitimate companies do not send account unlock links via email. Always go to the official website to verify account security."
    }

    reason_description = reason_descriptions.get(reason, "Unknown reason")

    return render_template_string(failure_page, reason=reason, reason_description=reason_description)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
