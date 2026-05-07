import os
import json
from datetime import datetime

# Note: This is a template for the lead forwarding engine. 
# Real implementation requires Twilio SDK and an LLM API (OpenAI/Anthropic).

class LeadForwarder:
    def __init__(self, partner_phone, twilio_sid=None, twilio_token=None):
        self.partner_phone = partner_to_phone(partner_phone)
        self.twilio_sid = twilio_sid
        self.twilio_token = twilio_token

    def process_incoming_lead(self, payload):
        """
        Processes the incoming webhook payload from the website form.
        Payload example: {'name': 'John Doe', 'phone': '+15550001111', 'issue': 'AC stopped working'}
        """
        print(f"[*] Received new lead at {datetime.now()}")
        
        # 1. Extract Data
        customer_info = payload.get('name'), payload.get('phone')
        issue_description = payload.get('issue', 'No description provided.')

        # 2. Sentiment Analysis (MOCK)
        # In production, this would call an LLM to identify the "Trust Gap" opportunity.
        sentiment = self._analyze_sentiment(issue_description)
        
        # 3. Formulate Notification Message
        notification = (
            f"🚨 NEW HVAC LEAD - AUSTIN\n"
            f"Customer: {customer_info[0]}\n"
            f"Contact: {customer_info[1]}\n"
            f"Issue: {issue_description}\n"
            f"Urgency/Sentiment: {sentiment}"
        )

        # 4. Route to Partner (MOCK Twilio SMS)
        self._send_sms_to_partner(notification)
        
        return {"status": "success", "message": "Lead routed."}

    def _analyze_sentiment(self, text):
        # Mocking LLM logic for identifying trust-gap triggers
        triggers = ["expensive", "scam", "hidden fee", "unprofessional", "worst"]
        if any(t in text.lower() for t in triggers):
            return "HIGH (Trust Gap Opportunity Detected!)"
        return "Standard"

    def _send_sms_to_partner(self, message):
        # In production: use twilio.rest.Client
        print(f"[SMS SENT TO {self.partner_phone}]:\n{message}")

def partner_to_phone(p):
    return p if p.startswith('+') else f"+{p}"

if __name__ == "__main__":
    # MOCK EXECUTION FOR TESTING
    forwarder = LeadForwarder("+15125550123")
    
    test_payloads = [
        {"name": "Alice Smith", "phone": "+15559876543", "issue": "AC is blowing warm air."},
        {"name": "Bob Jones", "phone": "+15551234444", "issue": "Previous company charged me a hidden fee, looking for honest repair."}
    ]

    for payload in test_payloads:
        forwarder.process_incoming_lead(payload)
