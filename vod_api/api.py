class VodApi:
    def __init__(self, api_key: str):
        self.api_key = api_key

    @property
    def audio(self):
        print("Audio!")

    @property
    def audio_track(self):
        """Audio Track"""
        print("Audio Track!")

    @property
    def channel(self):
        """Channel"""
        print("Channel!")

    @property
    def file(self):
        """File"""
        print("File!")

    @property
    def profile(self):
        """Profile"""
        print("Profile!")

    @property
    def general_report(self):
        """General Report"""
        print("General Report!")

    @property
    def subtitle(self):
        """Subtitle"""
        print("Subtitle!")

    @property
    def Domain(self):
        """Domain"""
        print("Domain!")

    @property
    def video(self):
        """Video"""
        print("Video!")

    @property
    def watermark(self):
        """Watermark"""
        print("Watermark")
