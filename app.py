import streamlit as st
import streamlit.components.v1 as components

st.title("💧 Water Reminder App")

# Firebase Web Push public key
vapid_key = "BN3a4zBhXjbWCinjESZCLQvcDUfTpBKgxuk4nI8fWmh7sbwhcS6krwzEHmumbqErBYOsXCuRA1Efb9ngzTAVoWA"

# Firebase configuration
firebase_config = {
  "apiKey": "AIzaSyCL217HNw8_j9RP3HvBmRKh2rES8d6VmCU",
  "authDomain": "waterapp-5abba.firebaseapp.com",
  "projectId": "waterapp-5abba",
  "storageBucket": "waterapp-5abba.firebasestorage.app",
  "messagingSenderId": "158189055939",
  "appId": "1:158189055939:web:c97be940ddf1e42cca5776",
  "measurementId": "G-J7DCFKCNCJ"
}

firebase_script = f"""
<script src="https://www.gstatic.com/firebasejs/9.22.2/firebase-app.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.2/firebase-messaging.js"></script>

<script>
  const firebaseConfig = {{
    apiKey: "{firebase_config['apiKey']}",
    authDomain: "{firebase_config['authDomain']}",
    projectId: "{firebase_config['projectId']}",
    storageBucket: "{firebase_config['storageBucket']}",
    messagingSenderId: "{firebase_config['messagingSenderId']}",
    appId: "{firebase_config['appId']}",
    measurementId: "{firebase_config['measurementId']}"
  }};

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  const messaging = firebase.messaging();

  // Request permission
  Notification.requestPermission().then(permission => {{
      if (permission === 'granted') {{
          messaging.getToken({{vapidKey: "{vapid_key}"}}).then(token => {{
              document.body.innerHTML = "<h4>Device Token:</h4><p>" + token + "</p>";
          }});
      }} else {{
          document.body.innerHTML = "<p>Notifications not allowed.</p>";
      }}
  }});
</script>
"""

components.html(firebase_script, height=400)
