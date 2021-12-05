import requests

from .base import Base


class GeneralReport(Base):
    def __init__(self, api_key: str):
        super(GeneralReport, self).__init__(api_key)

    def get_domain_geo_report(self, period: str) -> dict:
        """
        Return Domain Geo Report. 

        Parameters
        ----------
        period : str
            Values: 1h,3h,6h,12h,24h,7d,30d

        Returns
        -------

        Example
        -------
        """
        parameters = {
            "period": period
        }
        res = requests.get(
                self._get_geo_report_url(),
                params=parameters,
                headers=self.auth
            )

        return res.json()

    def get_domain_statics_report(self) -> dict:
        """
        Return Domain statistics report. 

        Parameters
        ----------
        None

        Returns
        -------

        Example
        -------
        """
        res = requests.get(
                self._get_statics_report_url(), headers=self.auth
            )
        return res.json()

    def get_domain_traffic(self, period: str) -> dict:
        """
        Return Domain Traffic. 

        Parameters
        ----------
        period : str
            Values: 1h,3h,6h,12h,24h,7d,30d

        Returns
        -------

        Example
        -------
        """
        parameters = {
            "period": period
        }

        res = requests.get(
                self._get_traffic_url(),
                params=parameters,
                headers=self.auth
            )
        return res.json()

    def get_user_agent(self, period: str) -> dict:
        """
        Return User Agent. 

        Parameters
        ----------
        period : str
            Values: 1h,3h,6h,12h,24h,7d,30d

        Returns
        -------

        Example
        -------
        """
        parameters = {
            "period": period
        }

        res = requests.get(
                self._get_user_agent_url(),
                params=parameters,
                headers=self.auth
            )
        return res.json()

    def get_domain_visitors(self, period: str) -> dict:
        """
        Return Domain Visitors. 

        Parameters
        ----------
        period : str
            Values: 1h,3h,6h,12h,24h,7d,30d

        Returns
        -------

        Example
        -------
        """
        parameters = {
            "period": period
        }
        res = requests.get(
                self._get_visitors_url(),
                params=parameters,
                headers=self.auth
            )
        return res.json()

    def _get_geo_report_url(self) -> str:
        # https://napi.arvancloud.com/vod/2.0/report/geo
        return f"{self.base_url}/report/geo"

    def _get_statics_report_url(self) -> str:
        # https://napi.arvancloud.com/vod/2.0/report/statistics
        return f"{self.base_url}/report/statics"

    def _get_traffic_url(self) -> str:
        # https://napi.arvancloud.com/vod/2.0/report/traffics
        return f"{self.base_url}/report/traffics"

    def _get_user_agent_url(self) -> str:
        # https://napi.arvancloud.com/vod/2.0/report/user-agent
        return f"{self.base_url}/user-agent"

    def _get_visitors_url(self) -> str:
        # https://napi.arvancloud.com/vod/2.0/report/visitors
        return f"{self.base_url}/report/visitors"
