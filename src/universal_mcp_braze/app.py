from typing import Any
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class BrazeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='braze', integration=integration, **kwargs)
        self.base_url = "https://rest.iad-01.braze.com"

    def query_hard_bounced_emails(self, start_date=None, end_date=None, limit=None, offset=None, email=None) -> Any:
        """
        Retrieves a list of permanently undelivered email addresses with optional date range, pagination, and email filtering.

        Args:
            start_date (string): (Optional*) String in YYYY-MM-DD format Start date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: '2019-01-01'.
            end_date (string): (Optional*) String in YYYY-MM-DD format String in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: '2019-02-01'.
            limit (string): (Optional) Integer Optional field to limit the number of results returned. Defaults to 100, maximum is 500. Example: '100'.
            offset (string): (Optional) Integer Optional beginning point in the list to retrieve from. Example: '1'.
            email (string): (Optional*) String If provided, we will return whether or not the user has hard bounced. *You must provide either an `email` or a `start_date`, and an `end_date`. Example: 'example@braze.com'.

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses, important
        """
        url = f"{self.base_url}/email/hard_bounces"
        query_params = {k: v for k, v in [('start_date', start_date), ('end_date', end_date), ('limit', limit), ('offset', offset), ('email', email)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_list_of_unsubscribed_email_addresses(self, start_date=None, end_date=None, limit=None, offset=None, sort_direction=None, email=None) -> Any:
        """
        Retrieves a list of unsubscribed email addresses within a specified date range, optionally filtered by email, with pagination and sorting support.

        Args:
            start_date (string): (Optional*) String in YYYY-MM-DD format Start date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API. Example: '2020-01-01'.
            end_date (string): (Optional*) String in YYYY-MM-DD format End date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API. Example: '2020-02-01'.
            limit (string): (Optional) Integer Optional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500. Example: '1'.
            offset (string): (Optional) Integer Optional beginning point in the list to retrieve from Example: '1'.
            sort_direction (string): (Optional) String Pass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest. Example: 'desc'.
            email (string): (Optional*) String If provided, we will return whether or not the user has unsubscribed Example: 'example@braze.com'.

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses
        """
        url = f"{self.base_url}/email/unsubscribes"
        query_params = {k: v for k, v in [('start_date', start_date), ('end_date', end_date), ('limit', limit), ('offset', offset), ('sort_direction', sort_direction), ('email', email)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def change_email_subscription_status(self, email=None, subscription_state=None) -> Any:
        """
        Posts a request to retrieve the current delivery status of a specified email.

        Args:
            email (string): email Example: 'example@braze.com'.
            subscription_state (string): subscription_state
                Example:
                ```json
                {
                  "email": "example@braze.com",
                  "subscription_state": "subscribed"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses
        """
        request_body = {
            'email': email,
            'subscription_state': subscription_state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/email/status"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_hard_bounced_emails(self, email=None) -> Any:
        """
        Removes email addresses from a bounce list using the Braze API.

        Args:
            email (string): email
                Example:
                ```json
                {
                  "email": "example@braze.com"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses
        """
        request_body = {
            'email': email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/email/bounce/remove"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_email_addresses_from_spam_list(self, email=None) -> Any:
        """
        Removes specified email addresses from both the Braze spam list and the associated email provider's spam list using a POST request.

        Args:
            email (string): email
                Example:
                ```json
                {
                  "email": "example@braze.com"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses
        """
        request_body = {
            'email': email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/email/spam/remove"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def blacklist_email_addresses(self, email=None) -> Any:
        """
        Unsubscribes a user from email and marks them as hard bounced.

        Args:
            email (array): email
                Example:
                ```json
                {
                  "email": [
                    "blacklist_email1",
                    "blacklist_email2"
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Email Lists & Addresses
        """
        request_body = {
            'email': email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/email/blacklist"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_analytics(self, campaign_id=None, length=None, ending_at=None) -> Any:
        """
        Retrieves a data series for a campaign, providing analytics such as message send, open, and click metrics over a specified time period defined by the campaign ID, series length, and ending date.

        Args:
            campaign_id (string): (Required) String Campaign API identifier Example: '{{campaign_identifier}}'.
            length (string): (Required) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '7'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Date on which the data series should end - defaults to time of the request Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, Campaign
        """
        url = f"{self.base_url}/campaigns/data_series"
        query_params = {k: v for k, v in [('campaign_id', campaign_id), ('length', length), ('ending_at', ending_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_details(self, campaign_id=None) -> Any:
        """
        Retrieves detailed information for a specified campaign using its unique identifier (campaign_id).

        Args:
            campaign_id (string): (Required) String Campaign API identifier Example: '{{campaign_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, Campaign
        """
        url = f"{self.base_url}/campaigns/details"
        query_params = {k: v for k, v in [('campaign_id', campaign_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_list(self, page=None, include_archived=None, sort_direction=None, last_edit_time_gt=None) -> Any:
        """
        Retrieves a paginated list of campaigns with optional filtering parameters for archived status, sorting, and edit time range.

        Args:
            page (string): (Optional) Integer The page of campaigns to return, defaults to 0 (returns the first set of up to 100) Example: '0'.
            include_archived (string): (Optional) Boolean Whether or not to include archived campaigns, defaults to false Example: 'false'.
            sort_direction (string): (Optional) String Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. Example: 'desc'.
            last_edit_time_gt (string): (Optional) DateTime (ISO 8601 string) Filters the results and only returns campaigns that were edited greater than the time provided till now. Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, Campaign
        """
        url = f"{self.base_url}/campaigns/list"
        query_params = {k: v for k, v in [('page', page), ('include_archived', include_archived), ('sort_direction', sort_direction), ('last_edit.time[gt]', last_edit_time_gt)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_analytics(self, campaign_id=None, send_id=None, length=None, ending_at=None) -> Any:
        """
        Retrieves a data series for campaign sends with optional filtering by campaign ID, send ID, length, and ending timestamp.

        Args:
            campaign_id (string): (Required) String Campaign API identifier. Example: '{{campaign_identifier}}'.
            send_id (string): (Required) String Send API identifier. Example: '{{send_identifier}}'.
            length (string): (Required) Integer Maximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 inclusive. Example: '30'.
            ending_at (string): (Optional) Datetime ISO 8601 string Date on which the data series should end. Defaults to time of the request. Example: '2014-12-10T23:59:59-05:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, Campaign
        """
        url = f"{self.base_url}/sends/data_series"
        query_params = {k: v for k, v in [('campaign_id', campaign_id), ('send_id', send_id), ('length', length), ('ending_at', ending_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_data_series_analytics(self, canvas_id=None, ending_at=None, starting_at=None, length=None, include_variant_breakdown=None, include_step_breakdown=None, include_deleted_step_data=None) -> Any:
        """
        Exports time series data for a Canvas, allowing users to retrieve analytics based on parameters such as canvas ID, time range, and optional breakdowns by variant, step, or deleted step data.

        Args:
            canvas_id (string): (Required) String Canvas API Identifier Example: '{{canvas_id}}'.
            ending_at (string): (Required) DateTime (ISO 8601 string) Date on which the data export should end - defaults to time of the request Example: '2018-05-30T23:59:59-5:00'.
            starting_at (string): (Optional) DateTime (ISO 8601 string) Date on which the data export should begin (either length or starting_at are required) Example: '2018-05-28T23:59:59-5:00'.
            length (string): (Optional) DateTime (ISO 8601 string) Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) Example: '10'.
            include_variant_breakdown (string): (Optional) Boolean Whether or not to include variant stats (defaults to false) Example: 'true'.
            include_step_breakdown (string): (Optional) Boolean Whether or not to include step stats (defaults to false) Example: 'true'.
            include_deleted_step_data (string): (Optional) Boolean Whether or not to include step stats for deleted steps (defaults to false) Example: 'true'.

        Returns:
            Any: API response data.

        Tags:
            Export, Canvas
        """
        url = f"{self.base_url}/canvas/data_series"
        query_params = {k: v for k, v in [('canvas_id', canvas_id), ('ending_at', ending_at), ('starting_at', starting_at), ('length', length), ('include_variant_breakdown', include_variant_breakdown), ('include_step_breakdown', include_step_breakdown), ('include_deleted_step_data', include_deleted_step_data)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_data_analytics_summary(self, canvas_id=None, ending_at=None, starting_at=None, length=None, include_variant_breakdown=None, include_step_breakdown=None, include_deleted_step_data=None) -> Any:
        """
        Retrieves summarized analytics data for a specific Canvas, including time-based metrics and optional breakdowns by variants or steps, based on parameters like time range and data granularity.

        Args:
            canvas_id (string): (Required) String Canvas API identifier Example: '{{canvas_id}}'.
            ending_at (string): (Required) DateTime (ISO 8601 string) Date on which the data export should end - defaults to time of the request Example: '2018-05-30T23:59:59-5:00'.
            starting_at (string): (Optional) DateTime (ISO 8601 string) Date on which the data export should begin (either length or starting_at required) Example: '2018-05-28T23:59:59-5:00'.
            length (string): (Optional) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required) Example: '5'.
            include_variant_breakdown (string): (Optional) Boolean Whether or not to include variant stats (defaults to false) Example: 'true'.
            include_step_breakdown (string): (Optional) Boolean Whether or not to include step stats (defaults to false) Example: 'true'.
            include_deleted_step_data (string): (Optional) Boolean Whether or not to include step stats for deleted steps (defaults to false) Example: 'true'.

        Returns:
            Any: API response data.

        Tags:
            Export, Canvas
        """
        url = f"{self.base_url}/canvas/data_summary"
        query_params = {k: v for k, v in [('canvas_id', canvas_id), ('ending_at', ending_at), ('starting_at', starting_at), ('length', length), ('include_variant_breakdown', include_variant_breakdown), ('include_step_breakdown', include_step_breakdown), ('include_deleted_step_data', include_deleted_step_data)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_details(self, canvas_id=None) -> Any:
        """
        Retrieves and returns detailed information about a Canvas resource identified by the provided `canvas_id`.

        Args:
            canvas_id (string): (Required) String Canvas API Identifier Example: '{{canvas_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, Canvas
        """
        url = f"{self.base_url}/canvas/details"
        query_params = {k: v for k, v in [('canvas_id', canvas_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_list(self, page=None, include_archived=None, sort_direction=None, last_edit_time_gt=None) -> Any:
        """
        Retrieves a paginated list of Canvases including names, API identifiers, and associated tags, sorted in groups and filterable by parameters like archival status and edit time.

        Args:
            page (string): (Optional) Integer The page of Canvases to return, defaults to `0` (returns the first set of up to 100) Example: '1'.
            include_archived (string): (Optional) Boolean Whether or not to include archived Canvases, defaults to `false`. Example: 'false'.
            sort_direction (string): (Optional) String Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. Example: 'desc'.
            last_edit_time_gt (string): (Optional) DateTime (ISO 8601 string) Filters the results and only returns Canvases that were edited greater than the time provided till now. Example: '2020-06-28T23:59:59-5:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, Canvas
        """
        url = f"{self.base_url}/canvas/list"
        query_params = {k: v for k, v in [('page', page), ('include_archived', include_archived), ('sort_direction', sort_direction), ('last_edit.time[gt]', last_edit_time_gt)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def custom_events_list(self, page=None) -> Any:
        """
        Retrieves a list of events using the "GET" method at the "/events/list" endpoint, optionally paginating results using the "page" query parameter.

        Args:
            page (string): (Optional) Integer The page of event names to return, defaults to 0 (returns the first set of up to 250) Example: '3'.

        Returns:
            Any: API response data.

        Tags:
            Export, Custom Events
        """
        url = f"{self.base_url}/events/list"
        query_params = {k: v for k, v in [('page', page)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def custom_events_analytics(self, event=None, length=None, unit=None, ending_at=None, app_id=None, segment_id=None) -> Any:
        """
        Retrieves a data series for an event using the specified parameters and returns the relevant data.

        Args:
            event (string): (Required) String The name of the custom event for which to return analytics Example: 'event_name'.
            length (string): (Required) Integer Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '24'.
            unit (string): (Optional) String Unit of time between data points - can be "day" or "hour" (defaults to "day") Example: 'hour'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request Example: '2014-12-10T23:59:59-05:00'.
            app_id (string): (Optional) String App API identifier retrieved from the Developer Console to limit analytics to a specific app Example: '{{app_identifier}}'.
            segment_id (string): (Optional) String Segment API identifier indicating the analytics enabled segment for which event analytics should be returned Example: '{{segment_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, Custom Events
        """
        url = f"{self.base_url}/events/data_series"
        query_params = {k: v for k, v in [('event', event), ('length', length), ('unit', unit), ('ending_at', ending_at), ('app_id', app_id), ('segment_id', segment_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def daily_new_users_by_date(self, length=None, ending_at=None, app_id=None) -> Any:
        """
        Retrieves a data series for new users using the "GET" method, filtered by the specified length, ending date, and app ID.

        Args:
            length (string): (Required) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '14'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier; if excluded, results for all apps in app group will be returned Example: '{{app_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, KPI
        """
        url = f"{self.base_url}/kpi/new_users/data_series"
        query_params = {k: v for k, v in [('length', length), ('ending_at', ending_at), ('app_id', app_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def daily_active_users_by_date(self, length=None, ending_at=None, app_id=None) -> Any:
        """
        Retrieves a data series for daily active users (DAU) based on specified parameters such as length, ending date, and application ID.

        Args:
            length (string): (Required) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '10'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier; if excluded, results for all apps in app group will be returned Example: '{{app_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, KPI
        """
        url = f"{self.base_url}/kpi/dau/data_series"
        query_params = {k: v for k, v in [('length', length), ('ending_at', ending_at), ('app_id', app_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def monthly_active_users_for_last30_days(self, length=None, ending_at=None, app_id=None) -> Any:
        """
        Retrieves a data series for monthly active users (MAU) using the "GET" method at "/kpi/mau/data_series," allowing customization with parameters for series length, end date, and application ID.

        Args:
            length (string): (Required) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '7'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request Example: '2018-06-28T23:59:59-05:00'.
            app_id (string): (Optional) String App API identifier; if excluded, results for all apps in app group will be returned Example: '{{app_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, KPI
        """
        url = f"{self.base_url}/kpi/mau/data_series"
        query_params = {k: v for k, v in [('length', length), ('ending_at', ending_at), ('app_id', app_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def kpis_for_daily_app_uninstalls_by_date(self, length=None, ending_at=None, app_id=None) -> Any:
        """
        Retrieves a series of KPI uninstall data over a specified period with configurable length, end date, and app identifier.

        Args:
            length (string): (Required) Integer Max number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '14'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier; if excluded, results for all apps in app group will be returned Example: '{{app_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, KPI
        """
        url = f"{self.base_url}/kpi/uninstalls/data_series"
        query_params = {k: v for k, v in [('length', length), ('ending_at', ending_at), ('app_id', app_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_card_analytics(self, card_id=None, length=None, unit=None, ending_at=None) -> Any:
        """
        Retrieves a list of data series for a specific card, allowing users to filter by card ID, length, unit, and ending date.

        Args:
            card_id (string): (Required) String Card API identifier Example: '{{card_identifier}}'.
            length (string): (Required) Integer Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive Example: '14'.
            unit (string): (Optional) String Unit of time between data points - can be "day" or "hour" (defaults to "day") Example: 'day'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Date on which the data series should end - defaults to time of the request Example: '2018-06-28T23:59:59-5:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, News Feed
        """
        url = f"{self.base_url}/feed/data_series"
        query_params = {k: v for k, v in [('card_id', card_id), ('length', length), ('unit', unit), ('ending_at', ending_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_cards_details(self, card_id=None) -> Any:
        """
        Retrieves detailed information about a specific card based on the provided `card_id` using the "GET" method.

        Args:
            card_id (string): (Required) String Card API identifier Example: '{{card_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, News Feed
        """
        url = f"{self.base_url}/feed/details"
        query_params = {k: v for k, v in [('card_id', card_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_cards_list(self, page=None, include_archived=None, sort_direction=None) -> Any:
        """
        Retrieves a paginated list of feed items with optional filtering for archived items and sorting direction.

        Args:
            page (string): (Optional) Integer The page of cards to return, defaults to 0 (returns the first set of up to 100) Example: '1'.
            include_archived (string): (Optional) Boolean Whether or not to include archived cards, defaults to false Example: 'true'.
            sort_direction (string): (Optional) String Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest. Example: 'desc'.

        Returns:
            Any: API response data.

        Tags:
            Export, News Feed
        """
        url = f"{self.base_url}/feed/list"
        query_params = {k: v for k, v in [('page', page), ('include_archived', include_archived), ('sort_direction', sort_direction)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_list(self, page=None, sort_direction=None) -> Any:
        """
        Retrieves a list of segments, each with details such as name, API identifier, and analytics tracking status, allowing optional pagination and sorting by creation time.

        Args:
            page (string): (Optional) Integer The page of segments to return, defaults to 0 (returns the first set of up to 100) Example: '1'.
            sort_direction (string): (Optional) String Pass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest. Example: 'desc'.

        Returns:
            Any: API response data.

        Tags:
            Export, Segment
        """
        url = f"{self.base_url}/segments/list"
        query_params = {k: v for k, v in [('page', page), ('sort_direction', sort_direction)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_analytics(self, segment_id=None, length=None, ending_at=None) -> Any:
        """
        Retrieves a data series for a specified segment based on the segment ID, data length, and ending date using the API endpoint at "/segments/data_series" via the GET method.

        Args:
            segment_id (string): (Required) String Segment API identifier. Example: '{{segment_identifier}}'.
            length (string): (Required) Integer Max number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive. Example: '14'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request. Example: '2018-06-27T23:59:59-5:00'.

        Returns:
            Any: API response data.

        Tags:
            Export, Segment
        """
        url = f"{self.base_url}/segments/data_series"
        query_params = {k: v for k, v in [('segment_id', segment_id), ('length', length), ('ending_at', ending_at)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_details(self, segment_id=None) -> Any:
        """
        Retrieves detailed information about a specific segment, identified by its ID, using the GET method at the "/segments/details" endpoint.

        Args:
            segment_id (string): (Required) String Segment API identifier Example: '{{segment_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, Segment
        """
        url = f"{self.base_url}/segments/details"
        query_params = {k: v for k, v in [('segment_id', segment_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def app_sessions_by_time(self, length=None, unit=None, ending_at=None, app_id=None, segment_id=None) -> Any:
        """
        Retrieves data series for sessions using the specified length, unit, ending time, application ID, and segment ID through a GET request to the "/sessions/data_series" endpoint.

        Args:
            length (string): (Required) Integer Max number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive. Example: '14'.
            unit (string): (Optional) String Unit of time between data points - can be "day" or "hour" (defaults to "day"). Example: 'day'.
            ending_at (string): (Optional) DateTime (ISO 8601 string) Point in time when the data series should end - defaults to time of the request. Example: '2018-06-28T23:59:59-5:00'.
            app_id (string): (Optional) String App API identifier retrieved from the Developer Console to limit analytics to a specific app. Example: '{{app_identifier}}'.
            segment_id (string): (Optional) String Segment API identifier indicating the analytics enabled segment for which sessions should be returned. Example: '{{segment_identifier}}'.

        Returns:
            Any: API response data.

        Tags:
            Export, Session Analytics
        """
        url = f"{self.base_url}/sessions/data_series"
        query_params = {k: v for k, v in [('length', length), ('unit', unit), ('ending_at', ending_at), ('app_id', app_id), ('segment_id', segment_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_identifier(self, braze_id=None, device_id=None, email_address=None, external_ids=None, fields_to_export=None, phone=None, user_aliases=None) -> Any:
        """
        Exports user IDs using a POST request and returns the result upon successful completion.

        Args:
            braze_id (string): braze_id Example: 'braze_identifier'.
            device_id (string): device_id Example: '1234567'.
            email_address (string): email_address Example: 'example@braze.com'.
            external_ids (array): external_ids Example: "['user_identifier1', 'user_identifier2']".
            fields_to_export (array): fields_to_export Example: "['first_name', 'email', 'purchases']".
            phone (string): phone Example: '+11112223333'.
            user_aliases (array): user_aliases
                Example:
                ```json
                {
                  "braze_id": "braze_identifier",
                  "device_id": "1234567",
                  "email_address": "example@braze.com",
                  "external_ids": [
                    "user_identifier1",
                    "user_identifier2"
                  ],
                  "fields_to_export": [
                    "first_name",
                    "email",
                    "purchases"
                  ],
                  "phone": "+11112223333",
                  "user_aliases": [
                    {
                      "alias_label": "example_label",
                      "alias_name": "example_alias"
                    }
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Export, Users
        """
        request_body = {
            'braze_id': braze_id,
            'device_id': device_id,
            'email_address': email_address,
            'external_ids': external_ids,
            'fields_to_export': fields_to_export,
            'phone': phone,
            'user_aliases': user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/export/ids"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_segment(self, callback_endpoint=None, fields_to_export=None, output_format=None, segment_id=None) -> Any:
        """
        Initiates a user segment export process and returns the export status upon successful creation.

        Args:
            callback_endpoint (string): callback_endpoint Example: 'example_endpoint'.
            fields_to_export (array): fields_to_export Example: "['first_name', 'email', 'purchases']".
            output_format (string): output_format Example: 'zip'.
            segment_id (string): segment_id
                Example:
                ```json
                {
                  "callback_endpoint": "example_endpoint",
                  "fields_to_export": [
                    "first_name",
                    "email",
                    "purchases"
                  ],
                  "output_format": "zip",
                  "segment_id": "segment_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Export, Users
        """
        request_body = {
            'callback_endpoint': callback_endpoint,
            'fields_to_export': fields_to_export,
            'output_format': output_format,
            'segment_id': segment_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/export/segment"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_global_control_group(self, callback_endpoint=None, fields_to_export=None, output_format=None) -> Any:
        """
        Exports the global control group data for users using the API endpoint at path "/users/export/global_control_group" via the POST method.

        Args:
            callback_endpoint (string): callback_endpoint
            fields_to_export (array): fields_to_export Example: "['email', 'braze_id']".
            output_format (string): output_format
                Example:
                ```json
                {
                  "callback_endpoint": "",
                  "fields_to_export": [
                    "email",
                    "braze_id"
                  ],
                  "output_format": "zip"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Export, Users
        """
        request_body = {
            'callback_endpoint': callback_endpoint,
            'fields_to_export': fields_to_export,
            'output_format': output_format,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/export/global_control_group"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_upcoming_scheduled_campaigns_and_canvases(self, end_time=None) -> Any:
        """
        Retrieves a list of scheduled broadcasts between the current time and a specified end time using the GET method.

        Args:
            end_time (string): (Required) String in ISO 8601 format End date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API. Example: '2018-09-01T00:00:00-04:00'.

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        url = f"{self.base_url}/messages/scheduled_broadcasts"
        query_params = {k: v for k, v in [('end_time', end_time)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_messages(self, schedule_id=None) -> Any:
        """
        Deletes a scheduled message and returns a status message upon success.

        Args:
            schedule_id (string): schedule_id
                Example:
                ```json
                {
                  "schedule_id": "schedule_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'schedule_id': schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/messages/schedule/delete"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_api_triggered_campaigns(self, campaign_id=None, schedule_id=None) -> Any:
        """
        Deletes scheduled triggers for campaigns using a POST request to the "/campaigns/trigger/schedule/delete" endpoint.

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            schedule_id (string): schedule_id
                Example:
                ```json
                {
                  "campaign_id": "campaign_identifier",
                  "schedule_id": "schedule_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'campaign_id': campaign_id,
            'schedule_id': schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/campaigns/trigger/schedule/delete"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_api_triggered_campaigns(self, audience=None, broadcast=None, campaign_id=None, recipients=None, schedule=None, send_id=None, trigger_properties=None) -> Any:
        """
        Creates and schedules a triggered campaign action, returning a success status upon completion.

        Args:
            audience (object): audience
            broadcast (boolean): broadcast Example: 'False'.
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            recipients (array): recipients Example: "[{'canvas_entry_properties': {}, 'external_user_id': 'external_user_identifier', 'trigger_properties': {}, 'user_alias': 'example_alias'}]".
            schedule (object): schedule
            send_id (string): send_id Example: 'send_identifier'.
            trigger_properties (object): trigger_properties
                Example:
                ```json
                {
                  "audience": {
                    "AND": [
                      {
                        "custom_attribute": {
                          "comparison": "equals",
                          "custom_attribute_name": "eye_color",
                          "value": "blue"
                        }
                      },
                      {
                        "custom_attribute": {
                          "comparison": "includes_value",
                          "custom_attribute_name": "favorite_foods",
                          "value": "pizza"
                        }
                      },
                      {
                        "OR": [
                          {
                            "custom_attribute": {
                              "comparison": "less_than_x_days_ago",
                              "custom_attribute_name": "last_purchase_time",
                              "value": 2
                            }
                          },
                          {
                            "push_subscription_status": {
                              "comparison": "is",
                              "value": "opted_in"
                            }
                          }
                        ]
                      },
                      {
                        "email_subscription_status": {
                          "comparison": "is_not",
                          "value": "subscribed"
                        }
                      },
                      {
                        "last_used_app": {
                          "comparison": "after",
                          "value": "2019-07-22T13:17:55+0000"
                        }
                      }
                    ]
                  },
                  "broadcast": false,
                  "campaign_id": "campaign_identifier",
                  "recipients": [
                    {
                      "canvas_entry_properties": {},
                      "external_user_id": "external_user_identifier",
                      "trigger_properties": {},
                      "user_alias": "example_alias"
                    }
                  ],
                  "schedule": {
                    "at_optimal_time": false,
                    "in_local_time": false,
                    "time": ""
                  },
                  "send_id": "send_identifier",
                  "trigger_properties": {}
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'audience': audience,
            'broadcast': broadcast,
            'campaign_id': campaign_id,
            'recipients': recipients,
            'schedule': schedule,
            'send_id': send_id,
            'trigger_properties': trigger_properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/campaigns/trigger/schedule/create"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_api_triggered_canvases(self, audience=None, broadcast=None, canvas_entry_properties=None, canvas_id=None, recipients=None, schedule=None) -> Any:
        """
        Schedules API-triggered Canvas messages for delivery based on specified actions.

        Args:
            audience (object): audience
            broadcast (boolean): broadcast Example: 'False'.
            canvas_entry_properties (object): canvas_entry_properties
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            recipients (array): recipients Example: "[{'canvas_entry_properties': {}, 'external_user_id': 'external_user_identifier', 'trigger_properties': '', 'user_alias': 'example_alias'}]".
            schedule (object): schedule
                Example:
                ```json
                {
                  "audience": {
                    "AND": [
                      {
                        "custom_attribute": {
                          "comparison": "equals",
                          "custom_attribute_name": "eye_color",
                          "value": "blue"
                        }
                      },
                      {
                        "custom_attribute": {
                          "comparison": "includes_value",
                          "custom_attribute_name": "favorite_foods",
                          "value": "pizza"
                        }
                      },
                      {
                        "OR": [
                          {
                            "custom_attribute": {
                              "comparison": "less_than_x_days_ago",
                              "custom_attribute_name": "last_purchase_time",
                              "value": 2
                            }
                          },
                          {
                            "push_subscription_status": {
                              "comparison": "is",
                              "value": "opted_in"
                            }
                          }
                        ]
                      },
                      {
                        "email_subscription_status": {
                          "comparison": "is_not",
                          "value": "subscribed"
                        }
                      },
                      {
                        "last_used_app": {
                          "comparison": "after",
                          "value": "2019-07-22T13:17:55+0000"
                        }
                      }
                    ]
                  },
                  "broadcast": false,
                  "canvas_entry_properties": {},
                  "canvas_id": "canvas_identifier",
                  "recipients": [
                    {
                      "canvas_entry_properties": {},
                      "external_user_id": "external_user_identifier",
                      "trigger_properties": "",
                      "user_alias": "example_alias"
                    }
                  ],
                  "schedule": {
                    "at_optimal_time": false,
                    "in_local_time": false,
                    "time": ""
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'audience': audience,
            'broadcast': broadcast,
            'canvas_entry_properties': canvas_entry_properties,
            'canvas_id': canvas_id,
            'recipients': recipients,
            'schedule': schedule,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/canvas/trigger/schedule/create"
        query_params = {k: v for k, v in [('', )] if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_messages(self, messages=None, schedule=None, schedule_id=None) -> Any:
        """
        Updates a scheduled message and returns a success status upon completion.

        Args:
            messages (object): messages
            schedule (object): schedule
            schedule_id (string): schedule_id
                Example:
                ```json
                {
                  "messages": {
                    "android_push": {
                      "alert": "Updated message!",
                      "title": "Updated title!"
                    },
                    "apple_push": {
                      "alert": "Updated Message!",
                      "badge": 1
                    },
                    "sms": {
                      "app_id": "app_identifier",
                      "body": "This is my SMS body.",
                      "message_variation_id": "message_variation_identifier",
                      "subscription_group_id": "subscription_group_identifier"
                    }
                  },
                  "schedule": {
                    "time": "2017-05-24T20:30:36Z"
                  },
                  "schedule_id": "schedule_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'messages': messages,
            'schedule': schedule,
            'schedule_id': schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/messages/schedule/update"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_api_triggered_campaigns(self, campaign_id=None, schedule=None, schedule_id=None) -> Any:
        """
        Updates the schedule of a campaign trigger using the POST method and returns a status message.

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            schedule (object): schedule
            schedule_id (string): schedule_id
                Example:
                ```json
                {
                  "campaign_id": "campaign_identifier",
                  "schedule": {
                    "in_local_time": true,
                    "time": "2017-05-24T21:30:00Z"
                  },
                  "schedule_id": "schedule_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'campaign_id': campaign_id,
            'schedule': schedule,
            'schedule_id': schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/campaigns/trigger/schedule/update"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_api_triggered_canvases(self, canvas_id=None, schedule=None, schedule_id=None) -> Any:
        """
        Updates a scheduled Canvas trigger's configuration using a POST request and returns a success status upon completion.

        Args:
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            schedule (object): schedule
            schedule_id (string): schedule_id
                Example:
                ```json
                {
                  "canvas_id": "canvas_identifier",
                  "schedule": {
                    "in_local_time": true,
                    "time": "2017-05-24T21:30:00Z"
                  },
                  "schedule_id": "schedule_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Schedule Mesages
        """
        request_body = {
            'canvas_id': canvas_id,
            'schedule': schedule,
            'schedule_id': schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/canvas/trigger/schedule/update"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_send_ids_for_message_send_tracking(self, campaign_id=None, send_id=None) -> Any:
        """
        Creates a new send operation with the specified ID and returns a success status upon completion.

        Args:
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            send_id (string): send_id
                Example:
                ```json
                {
                  "campaign_id": "campaign_identifier",
                  "send_id": "send_identifier"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Send Messages
        """
        request_body = {
            'campaign_id': campaign_id,
            'send_id': send_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/sends/id/create"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sending_campaign_messages_via_api_triggered_delivery(self, audience=None, broadcast=None, campaign_id=None, recipients=None, send_id=None, trigger_properties=None) -> Any:
        """
        Triggers a campaign send operation using a POST request to the "/campaigns/trigger/send" endpoint and returns a successful response upon completion.

        Args:
            audience (object): audience
            broadcast (boolean): broadcast Example: 'False'.
            campaign_id (string): campaign_id Example: 'campaign_identifier'.
            recipients (object): recipients
            send_id (string): send_id Example: 'send_identifier'.
            trigger_properties (string): trigger_properties
                Example:
                ```json
                {
                  "audience": {
                    "AND": [
                      {
                        "custom_attribute": {
                          "comparison": "equals",
                          "custom_attribute_name": "eye_color",
                          "value": "blue"
                        }
                      },
                      {
                        "custom_attribute": {
                          "comparison": "includes_value",
                          "custom_attribute_name": "favorite_foods",
                          "value": "pizza"
                        }
                      },
                      {
                        "OR": [
                          {
                            "custom_attribute": {
                              "comparison": "less_than_x_days_ago",
                              "custom_attribute_name": "last_purchase_time",
                              "value": 2
                            }
                          },
                          {
                            "push_subscription_status": {
                              "comparison": "is",
                              "value": "opted_in"
                            }
                          }
                        ]
                      },
                      {
                        "email_subscription_status": {
                          "comparison": "is_not",
                          "value": "subscribed"
                        }
                      },
                      {
                        "last_used_app": {
                          "comparison": "after",
                          "value": "2019-07-22T13:17:55+0000"
                        }
                      }
                    ]
                  },
                  "broadcast": false,
                  "campaign_id": "campaign_identifier",
                  "recipients": {
                    "attributes": "",
                    "external_user_id": "external_user_identifier",
                    "send_to_existing_only": true,
                    "trigger_properties": "",
                    "user_alias": {
                      "alias_label": "example_label",
                      "alias_name": "example_name"
                    }
                  },
                  "send_id": "send_identifier",
                  "trigger_properties": ""
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Send Messages, important
        """
        request_body = {
            'audience': audience,
            'broadcast': broadcast,
            'campaign_id': campaign_id,
            'recipients': recipients,
            'send_id': send_id,
            'trigger_properties': trigger_properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/campaigns/trigger/send"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sending_canvas_messages_via_api_triggered_delivery(self, audience=None, broadcast=None, canvas_entry_properties=None, canvas_id=None, recipients=None) -> Any:
        """
        Sends Canvas messages via API-triggered delivery, allowing users to store message content in the dashboard while specifying recipients and timing through the API.

        Args:
            audience (object): audience
            broadcast (boolean): broadcast Example: 'False'.
            canvas_entry_properties (object): canvas_entry_properties
            canvas_id (string): canvas_id Example: 'canvas_identifier'.
            recipients (object): recipients
                Example:
                ```json
                {
                  "audience": {
                    "AND": [
                      {
                        "custom_attribute": {
                          "comparison": "equals",
                          "custom_attribute_name": "eye_color",
                          "value": "blue"
                        }
                      },
                      {
                        "custom_attribute": {
                          "comparison": "includes_value",
                          "custom_attribute_name": "favorite_foods",
                          "value": "pizza"
                        }
                      },
                      {
                        "OR": [
                          {
                            "custom_attribute": {
                              "comparison": "less_than_x_days_ago",
                              "custom_attribute_name": "last_purchase_time",
                              "value": 2
                            }
                          },
                          {
                            "push_subscription_status": {
                              "comparison": "is",
                              "value": "opted_in"
                            }
                          }
                        ]
                      },
                      {
                        "email_subscription_status": {
                          "comparison": "is_not",
                          "value": "subscribed"
                        }
                      },
                      {
                        "last_used_app": {
                          "comparison": "after",
                          "value": "2019-07-22T13:17:55+0000"
                        }
                      }
                    ]
                  },
                  "broadcast": false,
                  "canvas_entry_properties": {
                    "product_name": "shoes",
                    "product_price": 79.99
                  },
                  "canvas_id": "canvas_identifier",
                  "recipients": {
                    "attributes": {
                      "first_name": "Alex"
                    },
                    "canvas_entry_properties": "",
                    "external_user_id": "user_identifier",
                    "send_to_existing_only": true,
                    "trigger_properties": "",
                    "user_alias": {
                      "alias_label": "example_label",
                      "alias_name": "example_name"
                    }
                  }
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Messaging, Send Messages
        """
        request_body = {
            'audience': audience,
            'broadcast': broadcast,
            'canvas_entry_properties': canvas_entry_properties,
            'canvas_id': canvas_id,
            'recipients': recipients,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/canvas/trigger/send"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_ssubscription_group_status_email(self, subscription_group_id=None, external_id=None, email=None, phone=None) -> Any:
        """
        Retrieves the subscription status for a user specified by their external_id, email, or phone number within a subscription group.

        Args:
            subscription_group_id (string): (Required) String The `id` of your subscription group. Example: '{{subscription_group_id}}'.
            external_id (string): (Required*) String The `external_id` of the user (must include at least one and at most 50 `external_ids`). Only external_id or email is accepted for email subscription groups Example: '{{external_identifier}}'.
            email (string): (Required* ) String The email address of the user. Can be passed as an array of string with a max of 50. Only external_id or email is accepted for email subscription groups Example: 'example@braze.com'.
            phone (string): (Required*) String The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format. Only external_id or phone is accepted for SMS subscription groups Example: '+11112223333'.

        Returns:
            Any: API response data.

        Tags:
            Subscription Groups, SMS
        """
        url = f"{self.base_url}/subscription/status/get"
        query_params = {k: v for k, v in [('subscription_group_id', subscription_group_id), ('external_id', external_id), ('email', email), ('phone', phone)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_ssubscription_group_email(self, external_id=None, email=None, limit=None, offset=None, phone=None) -> Any:
        """
        Retrieves the subscription status of users by querying identifiers such as external_id, email, or phone, with pagination support via limit and offset parameters.

        Args:
            external_id (string): (Required) String The external_id of the user. Must include at least one and at most 50 `external_ids`. Example: '{{external_id}}'.
            email (string): (Required) String The email address of the user. Must include at least one address and at most 50 addresses. Example: 'example@braze.com'.
            limit (string): (Optional) Integer The limit on the maximum number of results returned. Default (and max) limit is 100. Example: '100'.
            offset (string): (Optional) Integer Number of templates to skip before returning rest of the templates that fit the search criteria. Example: '1'.
            phone (string): (Required*) String The phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format. Example: '+11112223333'.

        Returns:
            Any: API response data.

        Tags:
            Subscription Groups, SMS
        """
        url = f"{self.base_url}/subscription/user/status"
        query_params = {k: v for k, v in [('external_id', external_id), ('email', email), ('limit', limit), ('offset', offset), ('phone', phone)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_user_ssubscription_group_status_email(self, external_id=None, phone=None, subscription_group_id=None, subscription_state=None) -> Any:
        """
        Updates subscription statuses for up to 50 users in a subscription group via batch processing.

        Args:
            external_id (string): external_id Example: 'external_identifier'.
            phone (array): phone Example: "['+12223334444', '+11112223333']".
            subscription_group_id (string): subscription_group_id Example: 'subscription_group_identifier'.
            subscription_state (string): subscription_state
                Example:
                ```json
                {
                  "email": [
                    "example1@email.com",
                    "example2@email.com"
                  ],
                  "external_id": "example-user",
                  "subscription_group_id": "subscription_group_identifier",
                  "subscription_state": "unsubscribed"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Subscription Groups, SMS
        """
        request_body = {
            'external_id': external_id,
            'phone': phone,
            'subscription_group_id': subscription_group_id,
            'subscription_state': subscription_state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/subscription/status/set"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_available_content_blocks(self, modified_after=None, modified_before=None, limit=None, offset=None) -> Any:
        """
        Retrieves a list of content blocks using the GET method at the "/content_blocks/list" path, allowing filtering by modification dates with parameters like "modified_after" and "modified_before", and pagination control via "limit" and "offset".

        Args:
            modified_after (string): (Optional) String in ISO 8601 Retrieve only content blocks updated at or after the given time. Example: '2020-01-01T01:01:01.000000'.
            modified_before (string): (Optional) String in ISO 8601 Retrieve only content blocks updated at or before the given time. Example: '2020-02-01T01:01:01.000000'.
            limit (string): (Optional) Positive Number Maximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000. Example: '100'.
            offset (string): (Optional) Positive Number Number of content blocks to skip before returning rest of the templates that fit the search criteria. Example: '1'.

        Returns:
            Any: API response data.

        Tags:
            Templates, Content Blocks
        """
        url = f"{self.base_url}/content_blocks/list"
        query_params = {k: v for k, v in [('modified_after', modified_after), ('modified_before', modified_before), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def see_content_block_information(self, content_block_id=None, include_inclusion_data=None) -> Any:
        """
        Retrieves information about a specified Content Block using its identifier, optionally including data on where it is used in campaigns or Canvases.

        Args:
            content_block_id (string): (Required) String The Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier. Example: '{{content_block_id}}'.
            include_inclusion_data (string): (Optional) Boolean When set to ‘true’, the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases. Example: 'No'.

        Returns:
            Any: API response data.

        Tags:
            Templates, Content Blocks
        """
        url = f"{self.base_url}/content_blocks/info"
        query_params = {k: v for k, v in [('content_block_id', content_block_id), ('include_inclusion_data', include_inclusion_data)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_content_block(self, content=None, description=None, name=None, state=None, tags=None) -> Any:
        """
        Creates a new content block using the provided data and returns a success response upon completion.

        Args:
            content (string): content Example: 'HTML content within block'.
            description (string): description Example: 'This is my content block'.
            name (string): name Example: 'content_block'.
            state (string): state Example: 'draft'.
            tags (array): tags
                Example:
                ```json
                {
                  "content": "HTML content within block",
                  "description": "This is my content block",
                  "name": "content_block",
                  "state": "draft",
                  "tags": [
                    "marketing"
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Templates, Content Blocks
        """
        request_body = {
            'content': content,
            'description': description,
            'name': name,
            'state': state,
            'tags': tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/content_blocks/create"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_content_block(self, content=None, content_block_id=None, description=None, name=None, state=None, tags=None) -> Any:
        """
        Updates content blocks using a POST request and returns a success status upon completion.

        Args:
            content (string): content Example: 'HTML or text content within block'.
            content_block_id (string): content_block_id Example: 'content_block_id'.
            description (string): description Example: 'This is my content block'.
            name (string): name Example: 'content_block'.
            state (string): state Example: 'draft'.
            tags (array): tags
                Example:
                ```json
                {
                  "content": "HTML or text content within block",
                  "content_block_id": "content_block_id",
                  "description": "This is my content block",
                  "name": "content_block",
                  "state": "draft",
                  "tags": [
                    "marketing"
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Templates, Content Blocks
        """
        request_body = {
            'content': content,
            'content_block_id': content_block_id,
            'description': description,
            'name': name,
            'state': state,
            'tags': tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/content_blocks/update"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_available_email_templates(self, modified_after=None, modified_before=None, limit=None, offset=None) -> Any:
        """
        Retrieves a list of available email templates with optional filtering by modification time and pagination parameters.

        Args:
            modified_after (string): (Optional) String in ISO 8601 Retrieve only templates updated at or after the given time. Example: '2020-01-01T01:01:01.000000'.
            modified_before (string): (Optional) String in ISO 8601 Retrieve only templates updated at or before the given time Example: '2020-02-01T01:01:01.000000'.
            limit (string): (Optional) Positive Number Maximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000. Example: '1'.
            offset (string): (Optional) Positive Number Number of templates to skip before returning rest of the templates that fit the search criteria. Example: '0'.

        Returns:
            Any: API response data.

        Tags:
            Templates, Email Templates
        """
        url = f"{self.base_url}/templates/email/list"
        query_params = {k: v for k, v in [('modified_after', modified_after), ('modified_before', modified_before), ('limit', limit), ('offset', offset)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def see_email_template_information(self, email_template_id=None) -> Any:
        """
        Retrieves information about a specific email template using the "GET" method at the "/templates/email/info" path, based on the provided `email_template_id` query parameter.

        Args:
            email_template_id (string): (Required) String Your email template's API Identifier. Example: '{{email_template_id}}'.

        Returns:
            Any: API response data.

        Tags:
            Templates, Email Templates
        """
        url = f"{self.base_url}/templates/email/info"
        query_params = {k: v for k, v in [('email_template_id', email_template_id)] if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_email_template(self, body=None, plaintext_body=None, preheader=None, subject=None, tags=None, template_name=None) -> Any:
        """
        Creates a new email template and returns a confirmation upon successful creation.

        Args:
            body (string): body Example: 'This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.'.
            plaintext_body (string): plaintext_body Example: 'This is the text within my email body and here is a link to https://www.braze.com/.'.
            preheader (string): preheader Example: 'My preheader is pretty cool.'.
            subject (string): subject Example: 'Welcome to my email template!'.
            tags (array): tags Example: "['Tag1', 'Tag2']".
            template_name (string): template_name
                Example:
                ```json
                {
                  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
                  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
                  "preheader": "My preheader is pretty cool.",
                  "subject": "Welcome to my email template!",
                  "tags": [
                    "Tag1",
                    "Tag2"
                  ],
                  "template_name": "email_template_name"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Templates, Email Templates
        """
        request_body = {
            'body': body,
            'plaintext_body': plaintext_body,
            'preheader': preheader,
            'subject': subject,
            'tags': tags,
            'template_name': template_name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/templates/email/create"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_email_template(self, body=None, email_template_id=None, plaintext_body=None, preheader=None, subject=None, tags=None, template_name=None) -> Any:
        """
        Updates an email template and returns a success status upon completion using a POST request.

        Args:
            body (string): body Example: "Check out this week's digital lookbook to inspire your outfits. Take a look at https://www.braze.com/".
            email_template_id (string): email_template_id Example: 'email_template_id'.
            plaintext_body (string): plaintext_body Example: 'This is the updated text within my email body and here is a link to https://www.braze.com/.'.
            preheader (string): preheader Example: 'We want you to have the best looks this Summer'.
            subject (string): subject Example: "This Week's Styles".
            tags (array): tags Example: "['Tag1', 'Tag2']".
            template_name (string): template_name
                Example:
                ```json
                {
                  "body": "Check out this week's digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
                  "email_template_id": "email_template_id",
                  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
                  "preheader": "We want you to have the best looks this Summer",
                  "subject": "This Week's Styles",
                  "tags": [
                    "Tag1",
                    "Tag2"
                  ],
                  "template_name": "Weekly Newsletter"
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            Templates, Email Templates
        """
        request_body = {
            'body': body,
            'email_template_id': email_template_id,
            'plaintext_body': plaintext_body,
            'preheader': preheader,
            'subject': subject,
            'tags': tags,
            'template_name': template_name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/templates/email/update"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def external_id_remove(self, external_id_renames=None) -> Any:
        """
        Removes external user identifiers and returns a successful status response upon completion.

        Args:
            external_id_renames (array): external_id_renames
                Example:
                ```json
                {
                  "external_ids": [
                    "existing_deprecated_external_id_string"
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            User Data, External ID Migration
        """
        request_body = {
            'external_id_renames': external_id_renames,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/external_ids/remove"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_new_user_aliases(self, user_aliases=None) -> Any:
        """
        Creates a new user alias using the API and returns a status message.

        Args:
            user_aliases (array): user_aliases
                Example:
                ```json
                {
                  "user_aliases": [
                    {
                      "alias_label": "example_label",
                      "alias_name": "example_name",
                      "external_id": "external_identifier"
                    }
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            User Data
        """
        request_body = {
            'user_aliases': user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/alias/new"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_delete(self, braze_ids=None, external_ids=None, user_aliases=None) -> Any:
        """
        Deletes a user using the API and returns a status message.

        Args:
            braze_ids (array): braze_ids Example: "['braze_identifier1', 'braze_identifier2']".
            external_ids (array): external_ids Example: "['external_identifier1', 'external_identifier2']".
            user_aliases (array): user_aliases
                Example:
                ```json
                {
                  "braze_ids": [
                    "braze_identifier1",
                    "braze_identifier2"
                  ],
                  "external_ids": [
                    "external_identifier1",
                    "external_identifier2"
                  ],
                  "user_aliases": [
                    "user_alias1",
                    "user_alias2"
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            User Data
        """
        request_body = {
            'braze_ids': braze_ids,
            'external_ids': external_ids,
            'user_aliases': user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/delete"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def identify_users(self, aliases_to_identify=None) -> Any:
        """
        Identifies a user and returns a success status upon verification.

        Args:
            aliases_to_identify (array): aliases_to_identify
                Example:
                ```json
                {
                  "aliases_to_identify": [
                    {
                      "external_id": "external_identifier",
                      "user_alias": {
                        "alias_label": "example_label",
                        "alias_name": "example_alias"
                      }
                    }
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            User Data, important
        """
        request_body = {
            'aliases_to_identify': aliases_to_identify,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/identify"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_track(self, attributes=None, events=None, purchases=None) -> Any:
        """
        Tracks user activity by sending data to the API endpoint at "/users/track" using the POST method.

        Args:
            attributes (array): attributes Example: "[{'array_attribute': ['banana', 'apple'], 'boolean_attribute_1': True, 'external_id': 'user_identifier', 'integer_attribute': 25, 'string_attribute': 'fruit'}]".
            events (array): events Example: "[{'app_id': 'app_identifier', 'external_id': 'user_identifier', 'name': 'watched_trailer', 'time': '2013-07-16T19:20:30+1:00'}]".
            purchases (array): purchases
                Example:
                ```json
                {
                  "attributes": [
                    {
                      "array_attribute": [
                        "banana",
                        "apple"
                      ],
                      "boolean_attribute_1": true,
                      "external_id": "user_identifier",
                      "integer_attribute": 25,
                      "string_attribute": "fruit"
                    }
                  ],
                  "events": [
                    {
                      "app_id": "app_identifier",
                      "external_id": "user_identifier",
                      "name": "watched_trailer",
                      "time": "2013-07-16T19:20:30+1:00"
                    }
                  ],
                  "purchases": [
                    {
                      "app_id": "app_identifier",
                      "currency": "USD",
                      "external_id": "user_identifier",
                      "price": 12.12,
                      "product_id": "product_name",
                      "properties": {
                        "date_property": "2014-02-02T00:00:00Z",
                        "integer_property": 3,
                        "string_property": "Russell"
                      },
                      "quantity": 6,
                      "time": "2017-05-12T18:47:12Z"
                    }
                  ]
                }
                ```

        Returns:
            Any: API response data.

        Tags:
            User Data, important
        """
        request_body = {
            'attributes': attributes,
            'events': events,
            'purchases': purchases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        url = f"{self.base_url}/users/track"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_tools(self):
        return [
            self.query_hard_bounced_emails,
            self.query_list_of_unsubscribed_email_addresses,
            self.change_email_subscription_status,
            self.remove_hard_bounced_emails,
            self.remove_email_addresses_from_spam_list,
            self.blacklist_email_addresses,
            self.campaign_analytics,
            self.campaign_details,
            self.campaign_list,
            self.send_analytics,
            self.canvas_data_series_analytics,
            self.canvas_data_analytics_summary,
            self.canvas_details,
            self.canvas_list,
            self.custom_events_list,
            self.custom_events_analytics,
            self.daily_new_users_by_date,
            self.daily_active_users_by_date,
            self.monthly_active_users_for_last30_days,
            self.kpis_for_daily_app_uninstalls_by_date,
            self.news_feed_card_analytics,
            self.news_feed_cards_details,
            self.news_feed_cards_list,
            self.segment_list,
            self.segment_analytics,
            self.segment_details,
            self.app_sessions_by_time,
            self.user_profile_export_by_identifier,
            self.user_profile_export_by_segment,
            self.user_profile_export_by_global_control_group,
            self.get_upcoming_scheduled_campaigns_and_canvases,
            self.delete_scheduled_messages,
            self.delete_scheduled_api_triggered_campaigns,
            self.schedule_api_triggered_campaigns,
            self.schedule_api_triggered_canvases,
            self.update_scheduled_messages,
            self.update_scheduled_api_triggered_campaigns,
            self.update_scheduled_api_triggered_canvases,
            self.create_send_ids_for_message_send_tracking,
            self.sending_campaign_messages_via_api_triggered_delivery,
            self.sending_canvas_messages_via_api_triggered_delivery,
            self.list_user_ssubscription_group_status_email,
            self.list_user_ssubscription_group_email,
            self.update_user_ssubscription_group_status_email,
            self.list_available_content_blocks,
            self.see_content_block_information,
            self.create_content_block,
            self.update_content_block,
            self.list_available_email_templates,
            self.see_email_template_information,
            self.create_email_template,
            self.update_email_template,
            self.external_id_remove,
            self.create_new_user_aliases,
            self.user_delete,
            self.identify_users,
            self.user_track
        ]
