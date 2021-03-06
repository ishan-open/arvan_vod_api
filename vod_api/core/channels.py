class ChannelDataCore:
    def __init__(self, response: dict):
        self.response = response
        self.id = response['id']
        self.title = response['title']
        self.description = response['description']
        self.secure_link_enabled = response['secure_link_enabled']
        self.secure_link_key = response['secure_link_key']
        self.secure_link_with_ip = response['secure_link_with_ip']
        self.ads_enabled = response['ads_enabled']
        self.present_type = response['present_type']
        self.campaign_id = response['campaign_id']
