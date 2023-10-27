
# Mock server class for demonstration
class MockEmailServer:
    def connect(self):
        return "Connected"
    def fetch_emails(self):
        return ["email1", "email2", "email3"]
    def parse(self, email):
        return f"Parsed: {email}"

# Extended EmailInterceptor class with additional features
class EmailInterceptor:
    def __init__(self, email_server):
        self.email_server = email_server
        self.cache = {}
        self.logs = []
        
    def log(self, message):
        self.logs.append(message)
        
    def connect_to_server(self):
        try:
            connection = self.email_server.connect()
            self.log(f"Connected to server: {connection}")
            return connection
        except Exception as e:
            self.log(f"Connection failed: {e}")
            return None

    def disconnect_from_server(self):
        try:
            self.log("Disconnected from server.")
            return "Disconnected"
        except Exception as e:
            self.log(f"Failed to disconnect: {e}")
            return None

    def fetch_emails(self, batch_size=None):
        try:
            emails = self.email_server.fetch_emails()
            if batch_size:
                emails = emails[:batch_size]
            self.log(f"Fetched {len(emails)} emails.")
            return emails
        except Exception as e:
            self.log(f"Failed to fetch emails: {e}")
            return None

    def parse_emails(self, batch_size=None):
        parsed_emails = []
        try:
            emails = self.fetch_emails(batch_size)
            if emails:
                for email in emails:
                    parsed_email = self.email_server.parse(email)
                    parsed_emails.append(parsed_email)
                    self.cache[email] = parsed_email
                self.log(f"Parsed {len(parsed_emails)} emails.")
            return parsed_emails
        except Exception as e:
            self.log(f"Failed to parse emails: {e}")
            return None

    def filter_emails(self, keyword):
        try:
            filtered_emails = [email for email in self.cache.values() if keyword in email]
            self.log(f"Filtered {len(filtered_emails)} emails with keyword: {keyword}.")
            return filtered_emails
        except Exception as e:
            self.log(f"Failed to filter emails: {e}")
            return None

    def clear_cache(self):
        try:
            self.cache.clear()
            self.log("Cache cleared.")
            return "Cache cleared"
        except Exception as e:
            self.log(f"Failed to clear cache: {e}")
            return None
    