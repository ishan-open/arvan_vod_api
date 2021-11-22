from .resources import (
    Audio, AudioTrack,
    Channel, Domain,
    File, GeneralReport,
    Profile, Subtitle,
    Video, Watermark,
)


class VodApi:
    def __init__(self, api_key: str):
        self.api_key = api_key

    @property
    def audio(self) -> Audio:
        """
        Audio

        Returns
        -------
        Audio
        """
        return Audio(self.api_key)

    @property
    def audio_track(self) -> AudioTrack:
        """
        Audio Track

        Returns
        -------
        AduioTrack
        """
        return AudioTrack(self.api_key)

    @property
    def channel(self) -> Channel:
        """
        Channel

        Returns
        -------
        Channel
        """
        return Channel(self.api_key)

    @property
    def file(self) -> File:
        """
        File

        Returns
        -------
        File
        """
        return File(self.api_key)

    @property
    def profile(self) -> Profile:
        """
        Profile

        Returns
        -------
        Profile
        """
        return Profile(self.api_key)

    @property
    def general_report(self) -> GeneralReport:
        """
        General Report

        Returns
        -------
        GeneralReport
        """
        return GeneralReport(self.api_key)

    @property
    def subtitle(self) -> Subtitle:
        """
        Subtitle

        Returns
        -------
        Subtitle
        """
        return Subtitle(self.api_key)

    @property
    def domain(self) -> Domain:
        """
        Domain

        Returns
        -------
        Domain
        """
        return Domain(self.api_key)

    @property
    def video(self) -> Video:
        """
        Video

        Returns
        -------
        Video
        """
        return Video(self.api_key)

    @property
    def watermark(self) -> Watermark:
        """
        Watermark

        Returns
        -------
        Watermark
        """
        return Watermark(self.api_key)
