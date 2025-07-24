import requests

# API endpoint
url = 'http://127.0.0.1:5000/summarize'

# Chat data you provided
chat_data = [
    {
        "sender": "Anshu Igdtuw",
        "message": "Meko abhi bhi ni aaya",
        "time": "8:35 PM"
    },
    {
        "sender": "Anushka Agg Igdtuw",
        "reply_to": "Anshu Igdtuw",
        "message": "27 ko aayega ab 😂",
        "time": "8:35 PM"
    },
    {
        "sender": "A",
        "message": "attitude",
        "time": "8:35 PM"
    },
    {
        "sender": "Anshu Igdtuw",
        "reply_to": "Anvi Nayyar",
        "quoted_message": "Areee nhi aisa ni h bilkul...tum hi toh ho mere 🥺🥺",
        "message": "Kehre mera bss chle toh tumhe block krdu 😂",
        "time": "8:35 PM"
    },
    {
        "sender": "Anushka Agg Igdtuw",
        "message": "if i m not wrong",
        "time": "8:35 PM"
    },
    {
        "sender": "Anvi Nayyar",
        "reply_to": "Anshu Igdtuw",
        "quoted_message": "Aaj k kaam k h bss",
        "message": "Achaa fir pdhu ya tum brief do",
        "time": "8:35 PM"
    },
    {
        "sender": "Anushka Agg Igdtuw",
        "message": "btao aarti",
        "time": "8:35 PM"
    },
    {
        "sender": "Anshu Igdtuw",
        "message": "Vo toh bss cllg me need rehti h 😂",
        "time": "8:35 PM"
    }
]

# Wrap the chat data in the expected structure
payload = {
    "chat": chat_data
}

# Send POST request
response = requests.post(url, json=payload)

# Print results
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

try:
    print("Summary:", response.json()['summary'])
except Exception as e:
    print("Error extracting summary:", e)
