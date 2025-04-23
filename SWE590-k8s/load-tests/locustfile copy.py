from locust import HttpUser, task, between
import base64


# class ZulipUser(HttpUser):
#     wait_time = between(5, 15)

#     @task
#     def send_message(self):
#         # you can find your API key at https://k8s.uzmankaza.com/#settings/account-and-privacy
#         headers = {
# 'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
#         }

#         data = {
#             'type': 'private',
#             # change this to the email of the user you want to send a message to, email format is user<id>@<domain>
#             'to': 'user9@k8s.uzmankaza.com',
#             'content': 'With mirth and laughter let old wrinkles come.'
#         }
#         self.client.post("/api/v1/messages", headers=headers, data=data)

print()


class ZulipUser(HttpUser):
    wait_time = between(2, 10)
    email = "lamikaan@gmail.com"
    api_key = "EtWkfyX8BH3nbCubqm8KPPTO9tDZTpi3"  # replace with your user's API key

    @task(5)
    def view_index_page(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        }
        self.client.get("/", headers=headers)

    @task(4)
    def view_streams_page(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        }
        self.client.get("/api/v1/streams", headers=headers)

    @task(3)
    def send_message_to_stream_1(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        }
        data = {"type": "stream",
                "to": "general",
                "content": "test message sent using locust",
                "topic": "test_1"}
        self.client.post("/api/v1/messages", data=data, headers=headers)

    @task(2)
    def send_message_to_stream_2(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        }
        data = {"type": "stream",
                "to": "general",
                "content": "@**Ali Kenan** sa using locust",
                "topic": "test_2"}
        self.client.post("/api/v1/messages", data=data, headers=headers)

    @task(1)
    def send_private_message_to_user(self):
        headers = {
            'Authorization': 'Basic ' + base64.b64encode(f"{self.email}:{self.api_key}".encode()).decode()
        }
        data = {"type": "private",
                "to": "user8@k8s.uzmankaza.com",
                "content": "private test message sent using locust"}
        self.client.post("/api/v1/messages", data=data, headers=headers)
