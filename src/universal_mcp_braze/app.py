from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class BrazeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='braze', integration=integration, **kwargs)
        self.base_url = "https://rest.iad-01.braze.com"


    def query_hard_bounced_emails(self, email: Annotated[Any, '(Optional*) String\n\nIf provided, we will return whether or not the user has hard bounced.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.'] = None, end_date: Annotated[Any, '(Optional*) String in YYYY-MM-DD format\n\nString in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.'] = None, limit: Annotated[Any, '(Optional) Integer\n\nOptional field to limit the number of results returned. Defaults to 100, maximum is 500.'] = None, offset: Annotated[Any, '(Optional) Integer\n\nOptional beginning point in the list to retrieve from.'] = None, start_date: Annotated[Any, '(Optional*) String in YYYY-MM-DD format \n\nStart date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.\n'] = None) -> Any:
        """
        Queries and retrieves a list of email addresses that have hard bounced email messages within a specified time frame.
        
        Args:
            email: Optional string; if provided, returns whether the user has hard bounced.
            end_date: Required string in YYYY-MM-DD format; end date of the range to retrieve hard bounces.
            limit: Optional integer; limits the number of results. Defaults to 100, maximum is 500.
            offset: Optional integer; the starting point for retrieving results from.
            start_date: Optional string in YYYY-MM-DD format; start date of the range. Either this or an `email` must be provided.
        
        Returns:
            A JSON response containing a list of email addresses that have hard bounced along with the time they hard bounced.
        
        Raises:
            requests.exceptions.HTTPError: Raised if an HTTP request returns an unsuccessful status code.
        
        Tags:
            scrape, email, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "start_date": start_date,
                "end_date": end_date,
                "limit": limit,
                "offset": offset,
                "email": email,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def query_list_of_unsubscribed_email_addresses(self, email: Annotated[Any, '(Optional*) String\n\nIf provided, we will return whether or not the user has unsubscribed'] = None, end_date: Annotated[Any, '(Optional*)  String in YYYY-MM-DD format\n\nEnd date of the range to retrieve unsubscribes. This is treated as midnight in UTC time by the API.'] = None, limit: Annotated[Any, '(Optional) Integer\n\nOptional field to limit the number of results returned. Limit must be greater than 1. Defaults to 100, maximum is 500.'] = None, offset: Annotated[Any, '(Optional) Integer \n\nOptional beginning point in the list to retrieve from'] = None, sort_direction: Annotated[Any, '(Optional) String\n\nPass in the value `asc` to sort unsubscribes from oldest to newest. Pass in `desc` to sort from newest to oldest. If sort_direction is not included, the default order is newest to oldest.'] = None, start_date: Annotated[Any, '(Optional*) String in YYYY-MM-DD format\n\nStart date of the range to retrieve unsubscribes, must be earlier than end_date. This is treated as midnight in UTC time by the API.'] = None) -> Any:
        """
        Retrieve emails that have unsubscribed within a specified date range or for a specific email address, supporting pagination and sorting.
        
        Args:
            email: Optional email address to check specific unsubscribes (mutually exclusive with date range parameters)
            end_date: Optional end date of query range (YYYY-MM-DD format), treated as UTC midnight. Requires `start_date` if used.
            limit: Maximum results to return (1-500), defaults to 100.
            offset: Starting index for pagination.
            sort_direction: Sort order ('asc' for oldest-first, 'desc' for newest-first). Defaults to 'desc'.
            start_date: Optional start date of query range (YYYY-MM-DD format), treated as UTC midnight. Requires `end_date` if used.
        
        Returns:
            JSON response containing list of unsubscribed emails and associated metadata
        
        Raises:
            HTTPError: If API request fails (e.g., invalid date range, authentication failure, or server error)
        
        Tags:
            email, unsubscribe-list, pagination, query, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "start_date": start_date,
                "end_date": end_date,
                "limit": limit,
                "offset": offset,
                "sort_direction": sort_direction,
                "email": email,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def change_email_subscription_status(self, email: Annotated[Any, ''] = None, subscription_state: Annotated[Any, ''] = None) -> Any:
        """
        Updates the email subscription status for one or multiple users, handling both existing and future-associated email addresses.
        
        Args:
            email: String email address to modify or array of up to 50 email addresses. Required.
            subscription_state: Subscription status to set: 'subscribed', 'unsubscribed', or 'opted_in'. Required.
        
        Returns:
            Parsed JSON response from the API call with the operation results.
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            email-subscription, user-management, api-endpoint, important, batch-operations
        """
        request_body = {
            "email": email,
            "subscription_state": subscription_state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_hard_bounced_emails(self, email: Annotated[Any, ''] = None) -> Any:
        """
        Removes email addresses from the Braze bounce list and the provider's bounce list.
        
        Args:
            email: String or array of up to 50 email addresses to remove from the bounce list.
        
        Returns:
            JSON response from the server after processing the request.
        
        Raises:
            HTTPError: Raised if there is an issue with the request, such as a non-200 status response.
        
        Tags:
            email-management, bounce-list, important
        """
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_email_addresses_from_spam_list(self, email: Annotated[Any, ''] = None) -> Any:
        """
        Remove email addresses from Braze spam lists and associated provider lists. Validates input and submits removal request.
        
        Args:
            email: String email address or array of up to 50 email addresses to remove from spam lists
        
        Returns:
            Parsed JSON response from Braze API endpoint
        
        Raises:
            HTTPError: Raised for invalid requests, server errors, or network issues during API communication
        
        Tags:
            email, spam-list, async-job, management, important
        """
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def blacklist_email_addresses(self, email: Annotated[list[Any], ''] = None) -> Any:
        """
        Blacklist specified email addresses to unsubscribe users from emails and mark them as hard bounced.
        
        Args:
            email: String email address or array of up to 50 email addresses to blacklist. Required.
        
        Returns:
            Parsed JSON response from the API containing blacklist operation results.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures like invalid input emails, authentication issues, or server errors.
        
        Tags:
            email, blacklist, unsubscribe, important, management
        """
        request_body = {
            "email": email,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_analytics(self, campaign_id: Annotated[Any, '(Required) String\n\nCampaign API identifier'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nDate on which the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None) -> Any:
        """
        Retrieves a daily series of campaign analytics, including message statistics by channel.
        
        Args:
            campaign_id: Required string representing the Campaign API identifier.
            ending_at: Optional ISO 8601 string for the date when the data series should end.
            length: Required integer specifying the maximum number of days before ending_at to include, between 1 and 100 inclusive.
        
        Returns:
            A JSON object containing campaign analytics data.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request to retrieve campaign analytics fails.
        
        Tags:
            analytics, campaign, important, export
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "campaign_id": campaign_id,
                "length": length,
                "ending_at": ending_at,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_details(self, campaign_id: Annotated[Any, '(Required) String\n\nCampaign API identifier'] = None) -> Any:
        """
        Retrieves detailed information about a campaign specified by its campaign_id.
        
        Args:
            campaign_id: Campaign API identifier (string). Required for retrieving specific campaign details.
        
        Returns:
            JSON response containing campaign details such as name, description, channels, and conversion behaviors.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            important, management, campaign, export
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "campaign_id": campaign_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def campaign_list(self, include_archived: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include archived campaigns, defaults to false'] = None, page: Annotated[Any, '(Optional) Integer\n\nThe page of campaigns to return, defaults to 0 (returns the first set of up to 100)'] = None, sort_direction: Annotated[Any, '(Optional) String\n\nPass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.'] = None) -> Any:
        
        """
        Retrieve a paginated list of campaigns with optional filters for archived status, page number, and sorting order.
        
        Args:
            include_archived: Boolean indicating whether to include archived campaigns. Defaults to false.
            page: Integer specifying the page number of results (0-based indexing). Defaults to 0 (first page).
            sort_direction: String ('desc' or 'asc') to sort by creation time. Defaults to ascending (oldest first).
        
        Returns:
            Parsed JSON response containing the paginated list of campaigns and associated metadata.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request fails due to server errors (4xx/5xx status codes).
        
        Tags:
            list, campaign, pagination, management, query, retrieve, featured, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
                "include_archived": include_archived,
                "sort_direction": sort_direction,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def send_analytics(self, campaign_id: Annotated[Any, '(Required) String\n\nCampaign API identifier.'] = None, ending_at: Annotated[Any, '(Optional) Datetime ISO 8601 string\n\nDate on which the data series should end. Defaults to time of the request.'] = None, length: Annotated[Any, '(Required) Integer\n\nMaximum number of days before `ending_at` to include in the returned series. Must be between 1 and 100 inclusive.'] = None, send_id: Annotated[Any, '(Required) String\n\nSend API identifier.'] = None) -> Any:
        """
        Retrieves a daily series of send analytics for a specific campaign and send, including metrics like deliveries, opens, conversions, and revenue.
        
        Args:
            campaign_id: (Required) Campaign API identifier used to fetch analytics data.
            ending_at: (Optional) Datetime ISO 8601 string specifying the end date for the data series. Defaults to request time if not provided.
            length: (Required) Integer representing the number of days before the ending_at date to include in the series. Must be between 1 and 100 inclusive.
            send_id: (Required) Send API identifier used to identify the specific campaign send.
        
        Returns:
            JSON response containing analytics metrics such as sent/delivered counts, opens, conversions, revenue, and unique recipients, structured according to Braze's send analytics schema.
        
        Raises:
            requests.HTTPError: Raised when the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            export, campaign, analytics, retrieve, send, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "campaign_id": campaign_id,
                "send_id": send_id,
                "length": length,
                "ending_at": ending_at,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_data_series_analytics(self, canvas_id: Annotated[Any, '(Required) String\n\nCanvas API Identifier'] = None, ending_at: Annotated[Any, '(Required) DateTime (ISO 8601 string)\n\nDate on which the data export should end - defaults to time of the request'] = None, include_deleted_step_data: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include step stats for deleted steps (defaults to false)'] = None, include_step_breakdown: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include step stats (defaults to false)'] = None, include_variant_breakdown: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include variant stats (defaults to false)'] = None, length: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)'] = None, starting_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string) \n\nDate on which the data export should begin (either length or starting_at are required)'] = None) -> Any:
        """
        Exports time series data for a specified Canvas, allowing customization of the data range and content.
        
        Args:
            canvas_id: Canvas API Identifier (required)
            ending_at: Date on which the data export should end (ISO 8601 string, defaults to time of request)
            include_deleted_step_data: Whether to include step stats for deleted steps (Boolean, defaults to False)
            include_step_breakdown: Whether to include step stats (Boolean, defaults to False)
            include_variant_breakdown: Whether to include variant stats (Boolean, defaults to False)
            length: Max number of days before ending_at to include (ISO 8601 string, either length or starting_at required)
            starting_at: Date on which the data export should begin (ISO 8601 string, either length or starting_at required)
        
        Returns:
            JSON response with Canvas data series analytics
        
        Raises:
            HTTPError: If the HTTP request fails
        
        Tags:
            export, canvas, analytics, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "canvas_id": canvas_id,
                "ending_at": ending_at,
                "starting_at": starting_at,
                "length": length,
                "include_variant_breakdown": include_variant_breakdown,
                "include_step_breakdown": include_step_breakdown,
                "include_deleted_step_data": include_deleted_step_data,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_data_analytics_summary(self, canvas_id: Annotated[Any, '(Required) String \n\nCanvas API identifier'] = None, ending_at: Annotated[Any, '(Required) DateTime (ISO 8601 string)\n\nDate on which the data export should end - defaults to time of the request'] = None, include_deleted_step_data: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include step stats for deleted steps (defaults to false)'] = None, include_step_breakdown: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include step stats (defaults to false)'] = None, include_variant_breakdown: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include variant stats (defaults to false)'] = None, length: Annotated[Any, '(Optional) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 14 inclusive (either length or starting_at required)'] = None, starting_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nDate on which the data export should begin (either length or starting_at required)'] = None) -> Any:
        """
        Generates a summary of analytics data for a specified Canvas, including rollups of time series metrics, variant statistics, and step performance details.
        
        Args:
            canvas_id: (Required) Canvas API identifier as a string.
            ending_at: (Required) ISO 8601 datetime string marking the end of the data export range (defaults to request time).
            include_deleted_step_data: (Optional) Boolean; set to True to include metrics for deleted steps.
            include_step_breakdown: (Optional) Boolean; set to True to include step-level statistics.
            include_variant_breakdown: (Optional) Boolean; set to True to include variant statistics.
            length: (Optional) Integer (1-14) specifying days before ending_at to include (required if not using starting_at).
            starting_at: (Optional) ISO 8601 datetime string marking the start of the data export range (required if not using length).
        
        Returns:
            JSON response containing the Canvas' analytics summary, including total metrics, optional variant/step breakdowns, and operation status.
        
        Raises:
            HTTPError: Raised for HTTP request failures or API errors (e.g., invalid parameters, authentication issues).
        
        Tags:
            export, analytics, canvas, async-job, data-rollup, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "canvas_id": canvas_id,
                "ending_at": ending_at,
                "starting_at": starting_at,
                "length": length,
                "include_variant_breakdown": include_variant_breakdown,
                "include_step_breakdown": include_step_breakdown,
                "include_deleted_step_data": include_deleted_step_data,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_details(self, canvas_id: Annotated[Any, '(Required) String\n\nCanvas API Identifier '] = None) -> Any:
        """
        Retrieve metadata and structural details about a Braze Canvas using its API identifier, including creation date, steps, variants, and associated channels.
        
        Args:
            canvas_id: (Required) String. Canvas API identifier specifying which Canvas to retrieve metadata for.
        
        Returns:
            Dictionary containing Canvas metadata such as creation time, variants, steps, channel usage, and status information. Matches the structure shown in the detailed API response schema.
        
        Raises:
            HTTPError: If the API request fails due to an invalid canvas_id, authentication issues, or server errors (raised by response.raise_for_status())
        
        Tags:
            export, canvas, metadata, braze, api-client, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "canvas_id": canvas_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def canvas_list(self, include_archived: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include archived Canvases, defaults to `false`.'] = None, page: Annotated[Any, '(Optional) Integer\n\nThe page of Canvases to return, defaults to `0` (returns the first set of up to 100)'] = None, sort_direction: Annotated[Any, '(Optional) String\n\nPass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.'] = None) -> Any:
        
        """
        Retrieves a list of canvases with optional pagination, archival inclusion, and sorting parameters.
        
        Args:
            include_archived: (Optional) Boolean. Whether to include archived Canvases. Defaults to false.
            page: (Optional) Integer. Page number to retrieve (0 returns first set of up to 100 Canvases). Defaults to 0.
            sort_direction: (Optional) String. Sort direction for results ('desc' for newest-first, 'asc' for oldest-first). Defaults to 'asc'.
        
        Returns:
            Dictionary containing the API response data with retrieved Canvases.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the API request fails due to invalid parameters or server errors.
        
        Tags:
            list, pagination, api-client, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
                "include_archived": include_archived,
                "sort_direction": sort_direction,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def custom_events_list(self, page: Annotated[Any, '(Optional) Integer\n\nThe page of event names to return, defaults to 0 (returns the first set of up to 250)'] = None) -> Any:
        """
        Fetches a list of custom events recorded for the app, returning them in groups of up to 250, sorted alphabetically.
        
        Args:
            page: (Optional) Integer. The page of event names to return. Defaults to None, which returns the first set of events.
        
        Returns:
            A JSON response containing 'message' and 'events' keys. 'message' indicates the status of the export, and 'events' is a list of custom event names.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters a fatal error, such as a Bad Request, Unauthorized, Rate Limited, or Internal Server Error.
        
        Tags:
            export, custom-events, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def custom_events_analytics(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier retrieved from the Developer Console to limit analytics to a specific app'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request'] = None, event: Annotated[Any, '(Required) String\n\nThe name of the custom event for which to return analytics '] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None, segment_id: Annotated[Any, '(Optional) String\n\nSegment API identifier indicating the analytics enabled segment for which event analytics should be returned'] = None, unit: Annotated[Any, '(Optional) String\n\nUnit of time between data points - can be "day" or "hour" (defaults to "day")'] = None) -> Any:
        """
        Retrieves analytics data for custom events over a specified time period, returning event counts segmented by time unit.
        
        Args:
            app_id: (Optional) String. App API identifier from Developer Console to scope analytics to a specific app.
            ending_at: (Optional) DateTime (ISO 8601 string). End timestamp for the data series. Defaults to request time.
            event: (Required) String. Name of the custom event to analyze.
            length: (Required) Integer (1-100). Number of time units (days/hours) before ending_at to include.
            segment_id: (Optional) String. Segment API identifier to filter analytics by user segment.
            unit: (Optional) String. Time unit between data points ('day' or 'hour'). Defaults to 'day'.
        
        Returns:
            JSON response containing time-series event counts in 'data' array and status message ('success' or error details).
        
        Raises:
            HTTPError: Raised for 4XX/5XX responses (400 Bad Request for invalid parameters, 401 Unauthorized for invalid API key, 429 Rate-Limited, 5XX server errors).
        
        Tags:
            custom-events, analytics, export, time-series, api-client, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "event": event,
                "length": length,
                "unit": unit,
                "ending_at": ending_at,
                "app_id": app_id,
                "segment_id": segment_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def daily_new_users_by_date(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier; if excluded, results for all apps in app group will be returned'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None) -> Any:
        """
        Retrieves a daily series of the total number of new users on each date within a specified period and optionally for a specific app.
        
        Args:
            app_id: The app API identifier; if not provided, results will include all apps in the app group.
            ending_at: The date and time in ISO 8601 format when the data series should end; defaults to the time of the request.
            length: The maximum number of days before the end date to include in the returned series; required, must be between 1 and 100 inclusive.
        
        Returns:
            JSON data containing a daily series of new users for each date within the specified period.
        
        Raises:
            HTTPError: Raised when an HTTP request error occurs, such as a failed response or timeout.
        
        Tags:
            export, kpi, dashboards, analytics, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "length": length,
                "ending_at": ending_at,
                "app_id": app_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def daily_active_users_by_date(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier; if excluded, results for all apps in app group will be returned'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None) -> Any:
        """
        Retrieves a daily series of unique active users (DAU) by date for a specific app or app group.
        
        Args:
            app_id: (Optional) App API identifier; if excluded, results include all apps in the app group
            ending_at: (Optional) ISO 8601 datetime string for series end date (defaults to request time)
            length: (Required) Days in series (1-100 inclusive)
        
        Returns:
            Dictionary containing success status and data array with 'time' (date) and 'dau' (count) entries
        
        Raises:
            HTTPError: If API request fails (4XX/5XX status codes)
        
        Tags:
            export, kpi, active-users, analytics, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "length": length,
                "ending_at": ending_at,
                "app_id": app_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def monthly_active_users_for_last30_days(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier; if excluded, results for all apps in app group will be returned'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None) -> Any:
        """
        Retrieves a daily series of unique active users for the last specified days. If no app_id is provided, returns data for all apps in the app group.
        
        Args:
            app_id: Optional String: App API identifier; if excluded, results for all apps in the group will be returned.
            ending_at: Optional DateTime (ISO 8601 string): Ending point of the data series; defaults to the time of the request if not specified.
            length: Required Integer: Maximum number of days before the ending date to include in the returned data series; must be between 1 and 100.
        
        Returns:
            JSON object containing a daily series of unique active users with timestamps as ISO 8601 dates.
        
        Raises:
            requests.exceptions.HTTPError: Raised if there are any problems with the HTTP request, such as invalid response status codes.
        
        Tags:
            query, kpi, reporting, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "length": length,
                "ending_at": ending_at,
                "app_id": app_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def kpis_for_daily_app_uninstalls_by_date(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier; if excluded, results for all apps in app group will be returned'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None) -> Any:
        """
        Retrieves a daily series of total app uninstalls as KPIs by date within a specified date range.
        
        Args:
            app_id: (Optional) String
        
        App API identifier; if omitted, results include all apps in the app group.
            ending_at: (Optional) DateTime (ISO 8601 string)
        
        End timestamp for the data series (defaults to request time).
            length: (Required) Integer
        
        Number of days before ending_at to include (1-100 inclusive).
        
        Returns:
            Dictionary containing 'message' status and 'data' list with date-uninstall pairs in ISO 8601 format.
        
        Raises:
            HTTPError: Raised for failed API requests due to network errors, invalid parameters, or authentication issues.
        
        Tags:
            export, kpi, app-analytics, http-client, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "length": length,
                "ending_at": ending_at,
                "app_id": app_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_card_analytics(self, card_id: Annotated[Any, '(Required) String\n\nCard API identifier'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nDate on which the data series should end - defaults to time of the request'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive'] = None, unit: Annotated[Any, '(Optional) String\n\nUnit of time between data points - can be "day" or "hour" (defaults to "day")'] = None) -> Any:
        """
        Retrieve a time-series of engagement analytics for a specified news feed card.
        
        Args:
            card_id: (Required) String. Card API identifier.
            ending_at: (Optional) DateTime (ISO 8601 string). End date/time of the data series (defaults to request time).
            length: (Required) Integer (1-100 inclusive). Number of time units (days/hours) to include prior to ending_at.
            unit: (Optional) String. Time unit between data points ("day" or "hour", defaults to "day").
        
        Returns:
            Dictionary containing analytics data series (response.json() format) with keys 'message' and 'data' array of timestamped metrics including impressions, clicks, and unique counts.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP error responses (4xx/5xx status codes) from the API.
        
        Tags:
            export, news-feed, analytics, time-series, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "card_id": card_id,
                "length": length,
                "unit": unit,
                "ending_at": ending_at,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_cards_details(self, card_id: Annotated[Any, '(Required) String\n\nCard API identifier '] = None) -> Any:
        """
        Retrieves detailed information about a news feed card by its identifier.
        
        Args:
            card_id: The Card API identifier for the news feed card to retrieve. It is a string and is required for this endpoint.
        
        Returns:
            A JSON response containing details of the news feed card, including its name, publication dates, tags, and other relevant information.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            news-feed, export, card-details, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "card_id": card_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def news_feed_cards_list(self, include_archived: Annotated[Any, '(Optional) Boolean\n\nWhether or not to include archived cards, defaults to false'] = None, page: Annotated[Any, '(Optional) Integer\n\nThe page of cards to return, defaults to 0 (returns the first set of up to 100)'] = None, sort_direction: Annotated[Any, '(Optional) String\n\nPass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If sort_direction is not included, the default order is oldest to newest.'] = None) -> Any:
        """
        Retrieves a paginated list of News Feed cards including their metadata, supporting filtering and sorting.
        
        Args:
            include_archived: Whether to include archived cards (defaults to False if not specified).
            page: The pagination offset (0 returns first 100 items, defaults to 0).
            sort_direction: Sort order ('desc' for newest-first, 'asc' or omitted for oldest-first).
        
        Returns:
            JSON response containing card details including IDs, types, titles, and tags. Contains 'message' status and 'cards' array.
        
        Raises:
            requests.exceptions.HTTPError: Raised for unsuccessful HTTP responses (e.g., 4XX/5XX status codes).
        
        Tags:
            news-feed, list, export, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
                "include_archived": include_archived,
                "sort_direction": sort_direction,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_list(self, page: Annotated[Any, '(Optional) Integer\n\nThe page of segments to return, defaults to 0 (returns the first set of up to 100)'] = None, sort_direction: Annotated[Any, '(Optional) String\n\nPass in the value `desc` to sort by creation time from newest to oldest. Pass in `asc` to sort from oldest to newest. If `sort_direction` is not included, the default order is oldest to newest.'] = None) -> Any:
        """
        Exports a list of segments, each containing its name, Segment API Identifier, and analytics tracking status.
        
        Args:
            page: The page of segments to return (optional, defaults to 0).
            sort_direction: Sort direction (optional, 'asc' or 'desc'). Defaults to 'asc' (oldest to newest).
        
        Returns:
            A JSON response containing the status and a list of segments with their details.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request encounters an error.
        
        Tags:
            export, segment, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "page": page,
                "sort_direction": sort_direction,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_analytics(self, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request.'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of days before `ending_at` to include in the returned series - must be between 1 and 100 inclusive.'] = None, segment_id: Annotated[Any, '(Required) String\n\nSegment API identifier.'] = None) -> Any:
        """
        Retrieves a daily series of segment size over time for a given segment ID.
        
        Args:
            ending_at: Optional DateTime (ISO 8601 string) specifying the end time for the data series.
            length: Required Integer specifying the max number of days before `ending_at` to include in the series (between 1 and 100).
            segment_id: Required String representing the Segment API identifier.
        
        Returns:
            JSON response containing the daily segment size data, including status and data series.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as network errors or invalid response status codes.
        
        Tags:
            analytics, segment, export, data-series, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "segment_id": segment_id,
                "length": length,
                "ending_at": ending_at,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def segment_details(self, segment_id: Annotated[Any, '(Required) String\n\nSegment API identifier'] = None) -> Any:
        """
        Retrieves detailed information about a Braze segment using its API identifier.
        
        Args:
            segment_id: The Segment API identifier (string). Required.
        
        Returns:
            Dictionary containing segment details including name, description, timestamps, and tags. Keys include 'message', 'created_at', 'updated_at', 'name', 'description', 'text_description', and 'tags'.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails with a 4XX/5XX status code, typically due to invalid authentication, missing segment_id, or server errors.
        
        Tags:
            retrieve, segment, details, api, braze, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "segment_id": segment_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def app_sessions_by_time(self, app_id: Annotated[Any, '(Optional) String\n\nApp API identifier retrieved from the Developer Console to limit analytics to a specific app.'] = None, ending_at: Annotated[Any, '(Optional) DateTime (ISO 8601 string)\n\nPoint in time when the data series should end - defaults to time of the request.'] = None, length: Annotated[Any, '(Required) Integer\n\nMax number of units (days or hours) before ending_at to include in the returned series - must be between 1 and 100 inclusive.'] = None, segment_id: Annotated[Any, '(Optional) String\n\nSegment API identifier indicating the analytics enabled segment for which sessions should be returned.'] = None, unit: Annotated[Any, '(Optional) String\n\nUnit of time between data points - can be "day" or "hour" (defaults to "day"). '] = None) -> Any:
        """
        Retrieves a time series of session counts for a specific app over a designated period.
        
        Args:
            app_id: (Optional) String. App API identifier from the Developer Console to limit analytics to a specific app.
            ending_at: (Optional) DateTime (ISO 8601 string). End time of the data series (defaults to request time).
            length: (Required) Integer. Number of time units (1-100 inclusive) before ending_at to include in the series.
            segment_id: (Optional) String. Segment API identifier for analytics-enabled segment filtering.
            unit: (Optional) String. Time unit between data points ('day' or 'hour', defaults to 'day').
        
        Returns:
            Dictionary containing a 'data' list of time/session count entries and a status 'message'.
        
        Raises:
            HTTPError: Raised for API request failures (non-2xx status codes).
        
        Tags:
            analytics, export, sessions, time-series, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "length": length,
                "unit": unit,
                "ending_at": ending_at,
                "app_id": app_id,
                "segment_id": segment_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_identifier(self, braze_id: Annotated[Any, ''] = None, device_id: Annotated[Any, ''] = None, email_address: Annotated[Any, ''] = None, external_ids: Annotated[list[Any], ''] = None, fields_to_export: Annotated[list[Any], ''] = None, phone: Annotated[Any, ''] = None, user_aliases: Annotated[list[Any], ''] = None) -> Any:
        """
        Exports user profile data by specifying one or more user identifiers, returning comprehensive user information including custom attributes, events, devices, and campaign interactions.
        
        Args:
            braze_id: Optional Braze identifier for the user
            device_id: Optional device identifier (only one device_id or email_address allowed per request)
            email_address: Optional email address of the user (only one email_address or device_id allowed per request)
            external_ids: Optional array of external identifiers (up to 50)
            fields_to_export: Optional array of field names to export. Defaults to all fields if not provided
            phone: Optional phone number of the user
            user_aliases: Optional array of user alias objects (up to 50)
        
        Returns:
            Dictionary containing user data, export status, and invalid identifiers. Includes arrays of user objects and any invalid user IDs detected.
        
        Raises:
            HTTPError: Raised for invalid API requests, authentication failures, or server errors (4XX/5XX status codes)
        
        Tags:
            export, users, api, data-retrieval, user-profiles, important
        """
        request_body = {
            "braze_id": braze_id,
            "device_id": device_id,
            "email_address": email_address,
            "external_ids": external_ids,
            "fields_to_export": fields_to_export,
            "phone": phone,
            "user_aliases": user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_segment(self, callback_endpoint: Annotated[Any, ''] = None, fields_to_export: Annotated[list[Any], ''] = None, output_format: Annotated[Any, ''] = None, segment_id: Annotated[Any, ''] = None) -> Any:
        """
        Exports user profiles within a specified segment, returning the export status.
        
        Args:
            callback_endpoint: Optional endpoint to post a download URL to when the export is available.
            fields_to_export: Required list of user data fields to export (custom attributes can also be exported).
            output_format: Optional output format; defaults to 'zip' when using an S3 bucket.
            segment_id: Required identifier for the segment to be exported.
        
        Returns:
            JSON response containing the export status, file prefix, and optional download URL.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            export, users, important, async_job
        """
        request_body = {
            "callback_endpoint": callback_endpoint,
            "fields_to_export": fields_to_export,
            "output_format": output_format,
            "segment_id": segment_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_profile_export_by_global_control_group(self, callback_endpoint: Annotated[Any, ''] = None, fields_to_export: Annotated[list[Any], ''] = None, output_format: Annotated[Any, ''] = None) -> Any:
        """
        Exports user profiles by global control group with specified options
        
        Args:
            callback_endpoint: Endpoint to receive the result of the export operation (optional)
            fields_to_export: List of fields from the user profiles to be exported (optional)
            output_format: Format of the exported data (optional)
        
        Returns:
            JSON response containing the exported user profiles
        
        Raises:
            HTTPError: Raised if the HTTP request to export user profiles fails for any reason
        
        Tags:
            export, users, async_job, important
        """
        request_body = {
            "callback_endpoint": callback_endpoint,
            "fields_to_export": fields_to_export,
            "output_format": output_format,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_upcoming_scheduled_campaigns_and_canvases(self, end_time: Annotated[Any, '(Required) String in ISO 8601 format\n\nEnd date of the range to retrieve upcoming scheduled Campaigns and Canvases. This is treated as midnight in UTC time by the API.'] = None) -> Any:
        """
        Retrieve upcoming scheduled Campaigns and Canvases between the current time and a specified end time in ISO 8601 format. Results include scheduled broadcasts with next occurrence details, limited to Braze-created schedules.
        
        Args:
            end_time: (Required) String in ISO 8601 format treated as midnight in UTC by the API. End date of the range for upcoming scheduled Campaigns/Canvases.
        
        Returns:
            JSON response containing 'scheduled_broadcasts' list with entries for each Campaign/Canvas (name, ID, type, tags, next_send_time, schedule_type).
        
        Raises:
            HTTPError: When the API request fails (e.g., authentication error, invalid parameters, or server issues).
        
        Tags:
            retrieve, schedule, campaigns, canvases, messaging, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "end_time": end_time,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_messages(self, schedule_id: Annotated[Any, ''] = None) -> Any:
        """
        Deletes a scheduled message by its schedule ID if the message has not been sent.
        
        Args:
            schedule_id: The ID of the scheduled message to be deleted.
        
        Returns:
            The response from the server as JSON.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, scheduled-messages, messaging, important
        """
        request_body = {
            "schedule_id": schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_scheduled_api_triggered_campaigns(self, campaign_id: Annotated[Any, ''] = None, schedule_id: Annotated[Any, ''] = None) -> Any:
        """
        Deletes scheduled API-triggered campaigns, canceling messages before sending.
        
        Args:
            campaign_id: Campaign identifier string (required).
            schedule_id: Schedule identifier string to delete (required).
        
        Returns:
            JSON response containing the deletion result.
        
        Raises:
            HTTPError: If the request fails due to invalid parameters or server error.
        
        Tags:
            delete, async-job, messaging, schedule, important
        """
        request_body = {
            "campaign_id": campaign_id,
            "schedule_id": schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_scheduled_messages(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Create and schedule messages (e.g., campaigns, canvases) to be sent at a designated time using the API.
        
        Args:
            request_body: Optional JSON object containing message scheduling parameters like broadcast, recipients, campaign ID, and schedule details.
        
        Returns:
            JSON response containing the scheduled message identifier.
        
        Raises:
            requests.exceptions.RequestException: Raised if there is a problem with the HTTP request (e.g., network failure, invalid URL).
        
        Tags:
            schedule-messages, messaging, api, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_api_triggered_campaigns(self, audience: Annotated[dict[str, Any], ''] = None, broadcast: Annotated[bool, ''] = None, campaign_id: Annotated[Any, ''] = None, recipients: Annotated[list[Any], ''] = None, schedule: Annotated[dict[str, Any], ''] = None, send_id: Annotated[Any, ''] = None, trigger_properties: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Schedule API-triggered campaigns with templated content, allowing scheduled message delivery up to 90 days in advance.
        
        Args:
            audience: Connected audience object (optional) for targeting users
            broadcast: Boolean flag determining broad delivery (optional, defaults to false if recipients omitted)
            campaign_id: Required campaign identifier for API-triggered message template
            recipients: Array of recipient objects (optional) for direct targeting
            schedule: Required schedule object defining delivery timing and recurrence
            send_id: Optional identifier for tracking specific sends
            trigger_properties: Key-value pairs for message personalization (optional)
        
        Returns:
            API response containing delivery confirmation and metadata
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (4xx/5xx status codes)
        
        Tags:
            schedule, messaging, campaign, api-triggered, async-delivery, important
        """
        request_body = {
            "audience": audience,
            "broadcast": broadcast,
            "campaign_id": campaign_id,
            "recipients": recipients,
            "schedule": schedule,
            "send_id": send_id,
            "trigger_properties": trigger_properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def schedule_api_triggered_canvases(self, audience: Annotated[dict[str, Any], ''] = None, broadcast: Annotated[bool, ''] = None, canvas_entry_properties: Annotated[dict[str, Any], ''] = None, canvas_id: Annotated[Any, ''] = None, recipients: Annotated[list[Any], ''] = None, schedule: Annotated[dict[str, Any], ''] = None) -> Any:
        
        """
        Schedules API-triggered canvases with customizable parameters.
        
        Args:
            audience: Dictionary representing the target audience.
            broadcast: Boolean indicating whether the canvas is broadcasted.
            canvas_entry_properties: Dictionary of properties for the canvas entry.
            canvas_id: Identifier of the canvas to schedule.
            recipients: List of recipients for the canvas.
            schedule: Dictionary containing scheduling details.
        
        Returns:
            JSON response from the server indicating the scheduling result.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            schedule, api-triggered, canvas-management, important
        """
        request_body = {
            "audience": audience,
            "broadcast": broadcast,
            "canvas_entry_properties": canvas_entry_properties,
            "canvas_id": canvas_id,
            "recipients": recipients,
            "schedule": schedule,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_messages(self, messages: Annotated[dict[str, Any], ''] = None, schedule: Annotated[dict[str, Any], ''] = None, schedule_id: Annotated[Any, ''] = None) -> Any:
        """
        Updates scheduled messages by modifying either the schedule configuration, message content, or both.
        
        Args:
            messages: Message content objects to update (supports multiple message types including email, SMS, and platform-specific formats). Omit to leave unchanged.
            schedule: Schedule configuration parameters (timing, recurrence, etc.) to update. Omit to leave unchanged.
            schedule_id: Unique identifier of the scheduled message campaign to modify (obtained during initial creation).
        
        Returns:
            Parsed JSON response containing the updated scheduled message details.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid schedule_id, malformed request bodies, or API authorization failures.
        
        Tags:
            update, messaging, schedule, async-job, api-client, important
        """
        request_body = {
            "messages": messages,
            "schedule": schedule,
            "schedule_id": schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_api_triggered_campaigns(self, campaign_id: Annotated[Any, ''] = None, schedule: Annotated[dict[str, Any], ''] = None, schedule_id: Annotated[Any, ''] = None) -> Any:
        """
        Updates scheduled API triggered campaigns by overwriting existing schedules or adding new ones.
        
        Args:
            campaign_id: Required: the identifier for the campaign.
            schedule: Required: a dictionary representing the schedule object.
            schedule_id: Optional: the schedule ID from previous requests.
        
        Returns:
            JSON response from the API following the update.
        
        Raises:
            HTTPError: Raised when the API request fails.
        
        Tags:
            update, api_triggered, campaign, schedule, messaging, management, important
        """
        request_body = {
            "campaign_id": campaign_id,
            "schedule": schedule,
            "schedule_id": schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_scheduled_api_triggered_canvases(self, canvas_id: Annotated[Any, ''] = None, schedule: Annotated[dict[str, Any], ''] = None, schedule_id: Annotated[Any, ''] = None) -> Any:
        """
        Updates scheduled API-triggered Canvas messages by specifying canvas ID, schedule, and optional schedule ID, with complete schedule overwrite behavior.
        
        Args:
            canvas_id: Required Canvas identifier (string)
            schedule: Required schedule configuration object that will replace existing schedule entirely
            schedule_id: Optional schedule identifier from initial creation response
        
        Returns:
            Response JSON containing updated schedule confirmation details
        
        Raises:
            HTTPError: Raised for failed API requests (4xx/5xx status codes)
        
        Tags:
            messaging, scheduled-messages, api-triggered, update, canvas, important
        """
        request_body = {
            "canvas_id": canvas_id,
            "schedule": schedule,
            "schedule_id": schedule_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_send_ids_for_message_send_tracking(self, campaign_id: Annotated[Any, ''] = None, send_id: Annotated[Any, ''] = None) -> Any:
        """
        Creates send identifiers for message send tracking in Braze, allowing programmatic message sending without campaign creation.
        
        Args:
            campaign_id: The campaign identifier, required as a string.
            send_id: An optional send identifier string.
        
        Returns:
            A JSON response including a 'send_id' for tracking the message send.
        
        Raises:
            requests.HTTPError: Raised if there is an issue with the HTTP request, such as exceeding the rate limit or invalid credentials.
        
        Tags:
            messaging, send-messages, important
        """
        request_body = {
            "campaign_id": campaign_id,
            "send_id": send_id,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sending_messages_immediately_via_api_only(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Sends immediate messages through Braze API using specified messaging objects and parameters.
        
        Args:
            request_body: Dictionary containing messaging configuration with fields like `broadcast`, `external_user_ids`, `messages`, etc. Must include valid Messaging Objects.
        
        Returns:
            Dictionary containing API response data including `dispatch_id` for tracking message transmission
        
        Raises:
            requests.exceptions.HTTPError: When API request fails due to invalid parameters, authentication issues, or server errors
            ValueError: If request_body contains improperly formatted messaging objects or missing critical parameters
        
        Tags:
            messaging, send-messages, api-integration, async-job, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sending_campaign_messages_via_api_triggered_delivery(self, audience: Annotated[dict[str, Any], ''] = None, broadcast: Annotated[bool, ''] = None, campaign_id: Annotated[Any, ''] = None, recipients: Annotated[dict[str, Any], ''] = None, send_id: Annotated[Any, ''] = None, trigger_properties: Annotated[Any, ''] = None) -> Any:
        """
        Initiates API-triggered message delivery for a Braze campaign, allowing control over recipients and message timing.
        
        Args:
            audience: Connected audience object specifying target users (replaces campaign's default audience if provided)
            broadcast: Boolean flag determining if message sends to entire campaign segment (required if recipients omitted)
            campaign_id: Braze campaign identifier for message content and targeting configuration
            recipients: Array of user objects with external_user_id and per-user trigger_properties (max 50 entries)
            send_id: Unique identifier for tracking the message dispatch
            trigger_properties: Global personalization key-value pairs applied to all recipients
        
        Returns:
            JSON response containing dispatch_id for the message transmission
        
        Raises:
            HTTPError: Raised for failed API requests (4xx/5xx http status codes)
        
        Tags:
            messaging, api-triggered, campaign, send, important
        """
        request_body = {
            "audience": audience,
            "broadcast": broadcast,
            "campaign_id": campaign_id,
            "recipients": recipients,
            "send_id": send_id,
            "trigger_properties": trigger_properties,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def sending_canvas_messages_via_api_triggered_delivery(self, audience: Annotated[dict[str, Any], ''] = None, broadcast: Annotated[bool, ''] = None, canvas_entry_properties: Annotated[dict[str, Any], ''] = None, canvas_id: Annotated[Any, ''] = None, recipients: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Sends Canvas messages via API triggered delivery, allowing customization of when and to whom messages are sent.
        
        Args:
            audience: Optional connected audience object used for targeting.
            broadcast: Optional flag indicating if the message should be sent to all users in the targeted segment.
            canvas_entry_properties: Optional object containing personalization key-value pairs for all users.
            canvas_id: Required string identifier for the Canvas message.
            recipients: Optional dictionary array for specified recipients with their canvas entry properties.
        
        Returns:
            JSON response from the API, typically containing a message dispatch ID.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a network error or malformed request.
        
        Tags:
            messaging, send-messages, important
        """
        request_body = {
            "audience": audience,
            "broadcast": broadcast,
            "canvas_entry_properties": canvas_entry_properties,
            "canvas_id": canvas_id,
            "recipients": recipients,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_ssubscription_group_status_email(self, email: Annotated[Any, '(Required* ) String\n\nThe email address of the user. Can be passed as an array of string with a max of 50.\n\nOnly external_id or email is accepted for email subscription groups'] = None, external_id: Annotated[Any, '(Required*) String\n\nThe `external_id` of the user (must include at least one and at most 50 `external_ids`).\n\nOnly external_id or email is accepted for email subscription groups'] = None, phone: Annotated[Any, '(Required*) String\n\nThe phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.\n\nOnly external_id or phone is accepted for SMS subscription groups\n'] = None, subscription_group_id: Annotated[Any, '(Required) String\n\nThe `id` of your subscription group.'] = None) -> Any:
        """
        Lists the subscription group status for a user based on the provided email or external ID.
        
        Args:
            email: The email address of the user. Can be a string or an array of strings with a maximum of 50 elements.
            external_id: The external ID of the user. Must be a string or an array of strings with a maximum of 50 elements.
            phone: The phone number of the user. Must be a string or an array of strings with a maximum of 50 elements. Recommended format is E.164.
            subscription_group_id: The ID of the subscription group.
        
        Returns:
            A JSON response containing the subscription status as 'subscribed', 'unsubscribed', or 'unknown'.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            email, external-id, subscription-group, list, status, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "subscription_group_id": subscription_group_id,
                "external_id": external_id,
                "email": email,
                "phone": phone,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_user_ssubscription_group_email(self, email: Annotated[Any, '(Required) String\n\nThe email address of the user. Must include at least one address and at most 50 addresses. '] = None, external_id: Annotated[Any, '(Required) String\n\nThe external_id of the user. Must include at least one and at most 50 `external_ids`.'] = None, limit: Annotated[Any, '(Optional) Integer\n\nThe limit on the maximum number of results returned. Default (and max) limit is 100.'] = None, offset: Annotated[Any, '(Optional) Integer\n\nNumber of templates to skip before returning rest of the templates that fit the search criteria.'] = None, phone: Annotated[Any, '(Required*) String\n\nThe phone number of the user (must include at least one phone number and at most 50 phone numbers). The recommendation is to provide this in the E.164 format.\n'] = None) -> Any:
        """
        Retrieves and lists the subscription groups for a user based on provided criteria like email, external_id, phone number, with options to limit and offset results.
        
        Args:
            email: The email address(es) of the user. Must include at least one address and at most 50 addresses.
            external_id: The external_id(s) of the user. Must include at least one and at most 50 external_ids.
            limit: The maximum number of results to return. Optional, default is 100.
            offset: The number of templates to skip before returning results.
            phone: The phone number(s) of the user. Must include at least one phone number and at most 50 phone numbers. Recommended format is E.164.
        
        Returns:
            JSON data containing the subscription groups for the specified user(s).
        
        Raises:
            requests.HTTPError: Raised if there is an HTTP request error, such as the server returning a status code that indicates failure.
        
        Tags:
            list, subscription-groups, users, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "external_id": external_id,
                "email": email,
                "limit": limit,
                "offset": offset,
                "phone": phone,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_user_ssubscription_group_status_email(self, external_id: Annotated[Any, ''] = None, phone: Annotated[list[Any], ''] = None, subscription_group_id: Annotated[Any, ''] = None, subscription_state: Annotated[Any, ''] = None) -> Any:
        """
        Updates a user's subscription group status via email using the Braze dashboard.
        
        Args:
            external_id: The external_id of the user (required if email is not used).
            phone: Optional phone number in E.164 format; must have existing tags.
            subscription_group_id: The ID of the subscription group (required).
            subscription_state: The state of subscription (required); can be 'subscribed' or 'unsubscribed'.
        
        Returns:
            JSON response from Braze containing a success message.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request to the Braze endpoint fails.
            json.JSONDecodeError: Raised if the response from Braze cannot be parsed as JSON.
        
        Tags:
            update, subscription-groups, email, important
        """
        request_body = {
            "external_id": external_id,
            "phone": phone,
            "subscription_group_id": subscription_group_id,
            "subscription_state": subscription_state,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_available_content_blocks(self, limit: Annotated[Any, '(Optional) Positive Number\n\nMaximum number of content blocks to retrieve, default to 100 if not provided, maximum acceptable value is 1000.'] = None, modified_after: Annotated[Any, '(Optional) String in ISO 8601\n\nRetrieve only content blocks updated at or after the given time.'] = None, modified_before: Annotated[Any, '(Optional) String in ISO 8601\n\nRetrieve only content blocks updated at or before the given time.'] = None, offset: Annotated[Any, '(Optional) Positive Number\n\nNumber of content blocks to skip before returning rest of the templates that fit the search criteria.'] = None) -> Any:
        """
        Retrieve a paginated list of content blocks with optional filters for modification time ranges.
        
        Args:
            limit: Positive integer (optional) specifying maximum items to retrieve (default 100, max 1000).
            modified_after: ISO 8601 timestamp (optional) to filter content blocks modified on or after this time.
            modified_before: ISO 8601 timestamp (optional) to filter content blocks modified on or before this time.
            offset: Positive integer (optional) specifying number of items to skip before retrieval.
        
        Returns:
            Dictionary containing 'count' (total matching items) and 'content_blocks' (list of dictionaries with content block metadata including ID, name, content type, liquid tag, timestamps, and tags).
        
        Raises:
            ValueError: Raised for invalid timestamps (non-ISO 8601 format or logic conflict between modified_after/modified_before)
            HTTPError: Raised for API request failures
        
        Tags:
            content-blocks, list, pagination, filter, templates, retrieval, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "modified_after": modified_after,
                "modified_before": modified_before,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def see_content_block_information(self, content_block_id: Annotated[Any, '(Required) String\n\nThe Content Block ID. This can be found by either listing Content Block information or going to the Developer Console, then API Settings, then scrolling to the bottom and searching for your Content Block API Identifier.'] = None, include_inclusion_data: Annotated[Any, '(Optional) Boolean\n\nWhen set to ‘true’, the API returns back the Message Variation API ID of Campaigns and Canvases where this content block is included, to be used in subsequent calls. The results exclude archived or deleted Campaigns or Canvases.'] = None) -> Any:
        """
        Retrieves information about an existing Content Block, including its details and optional inclusion data.
        
        Args:
            content_block_id: The ID of the Content Block to retrieve. This can be found in the Developer Console under API Settings.
            include_inclusion_data: When set to True, includes the Message Variation API IDs of Campaigns and Canvases where this Content Block is used.
        
        Returns:
            A JSON object containing Content Block details such as ID, name, content, description, type, tags, creation and edit times, inclusion count, and success message.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails, potentially due to invalid Content Block IDs or invalid request parameters.
        
        Tags:
            content-blocks, information, inclusion-data, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "content_block_id": content_block_id,
                "include_inclusion_data": include_inclusion_data,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_content_block(self, content: Annotated[Any, ''] = None, description: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, state: Annotated[Any, ''] = None, tags: Annotated[list[Any], ''] = None) -> Any:
        """
        Creates a new content block with the provided parameters and returns the newly created block's metadata.
        
        Args:
            content: HTML/text content for the block (required, must be string under 50kb)
            description: Brief description (optional, under 250 characters)
            name: Unique identifier (required, alphanumeric with '-_', under 100 chars)
            state: Content state: 'active' or 'draft' (default: 'active')
            tags: Existing tags as string array (optional)
        
        Returns:
            JSON response containing content_block_id, liquid_tag, created_at, and success message
        
        Raises:
            HTTPError: When invalid content format, name/description length violations, duplicate names, invalid tags, or Liquid parsing errors occur
            ValueError: Implicit validation failure for state/name/content rules before API call
        
        Tags:
            create, content-blocks, templates, api, important
        """
        request_body = {
            "content": content,
            "description": description,
            "name": name,
            "state": state,
            "tags": tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_content_block(self, content: Annotated[Any, ''] = None, content_block_id: Annotated[Any, ''] = None, description: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, state: Annotated[Any, ''] = None, tags: Annotated[list[Any], ''] = None) -> Any:
        """
        Updates a content block with provided parameters, ensuring validations for content, state, and metadata.
        
        Args:
            content: HTML or text content for the block. Must be a non-blank string under 50kb and contain valid Liquid syntax.
            content_block_id: Unique identifier of the content block to update. Required.
            description: Optional description (must be under 250 characters if provided).
            name: New name for the content block. Must be alphanumeric with dashes/underscores under 100 characters. Only editable in draft state.
            state: State update ('active' or 'draft'). Cannot transition active blocks to draft. Defaults to active if unspecified.
            tags: Array of existing tags to associate with the content block.
        
        Returns:
            Dictionary containing updated details like content_block_id, liquid_tag, creation timestamp, and success message.
        
        Raises:
            ValueError: Raised for invalid parameters: blank content, malformed Liquid syntax, name/description length violations, invalid characters in name, or invalid state transitions.
            HTTPError: On API request failures (e.g., non-existent tags, duplicate names, authentication issues, or server errors).
        
        Tags:
            templates, content-blocks, update, validation, important
        """
        request_body = {
            "content": content,
            "content_block_id": content_block_id,
            "description": description,
            "name": name,
            "state": state,
            "tags": tags,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_available_email_templates(self, limit: Annotated[Any, '(Optional) Positive Number\n\nMaximum number of templates to retrieve, default to 100 if not provided, maximum acceptable value is 1000.'] = None, modified_after: Annotated[Any, '(Optional) String in ISO 8601\n\nRetrieve only templates updated at or after the given time.'] = None, modified_before: Annotated[Any, '(Optional) String in ISO 8601\n\nRetrieve only templates updated at or before the given time'] = None, offset: Annotated[Any, '(Optional) Positive Number\n\nNumber of templates to skip before returning rest of the templates that fit the search criteria.'] = None) -> Any:
        """
        Lists available email templates from a Braze account, filtered by optional parameters such as limit, modified after/before times, and offset.
        
        Args:
            limit: Optional positive number; maximum number of templates to retrieve (default is 100, max 1000).
            modified_after: Optional string in ISO 8601 format; retrieve only templates updated at or after this time.
            modified_before: Optional string in ISO 8601 format; retrieve only templates updated at or before this time.
            offset: Optional positive number; number of templates to skip before returning the rest.
        
        Returns:
            A dictionary containing the count of returned templates and a list of templates with properties like email_template_id, template_name, creation and update times, and tags.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request, such as a connection error or invalid response.
        
        Tags:
            list, email-templates, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "modified_after": modified_after,
                "modified_before": modified_before,
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def see_email_template_information(self, email_template_id: Annotated[Any, "(Required) String\n\nYour email template's API Identifier."] = None) -> Any:
        """
        Retrieve details of a specific email template using its API identifier.
        
        Args:
            email_template_id: (Required) String
        
        The API identifier of the email template to retrieve information for. Must be a valid template ID registered on the Braze dashboard.
        
        Returns:
            A dictionary containing the email template's detailed configuration and metadata.
        
        Raises:
            HTTPError: Raised if the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            templates, email-templates, get, retrieve, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "email_template_id": email_template_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_email_template(self, body: Annotated[Any, ''] = None, plaintext_body: Annotated[Any, ''] = None, preheader: Annotated[Any, ''] = None, subject: Annotated[Any, ''] = None, tags: Annotated[list[Any], ''] = None, template_name: Annotated[Any, ''] = None) -> Any:
        """
        Creates an email template on the Braze dashboard using the Template REST API.
        
        Args:
            body: The HTML body of the email template.
            plaintext_body: A plaintext version of the email template body.
            preheader: The email preheader used to generate previews in some clients.
            subject: The email template subject line.
            tags: Existing tags for the template.
            template_name: The name of the email template.
        
        Returns:
            The JSON response from the API, typically including an email template ID.
        
        Raises:
            HTTPError: Raised if the API request fails due to HTTP errors (e.g., invalid request, unauthorized access).
        
        Tags:
            create, email-templates, braze-api, important
        """
        request_body = {
            "body": body,
            "plaintext_body": plaintext_body,
            "preheader": preheader,
            "subject": subject,
            "tags": tags,
            "template_name": template_name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_email_template(self, body: Annotated[Any, ''] = None, email_template_id: Annotated[Any, ''] = None, plaintext_body: Annotated[Any, ''] = None, preheader: Annotated[Any, ''] = None, subject: Annotated[Any, ''] = None, tags: Annotated[list[Any], ''] = None, template_name: Annotated[Any, ''] = None) -> Any:
        """
        Updates an email template using the Braze REST APIs.
        
        Args:
            body: Optional string representing the email template body that may include HTML.
            email_template_id: Required string representing the email template's API identifier.
            plaintext_body: Optional string for a plaintext version of the email template body.
            preheader: Optional string for the email preheader used in some clients.
            subject: Optional string for the email template subject line.
            tags: Optional list of tags that must already exist.
            template_name: Optional string for the name of the email template.
        
        Returns:
            JSON response from the Braze API after updating the email template.
        
        Raises:
            HTTPError: Raised if there is an HTTP request error, such as bad status code.
        
        Tags:
            update, email-templates, management, important
        """
        request_body = {
            "body": body,
            "email_template_id": email_template_id,
            "plaintext_body": plaintext_body,
            "preheader": preheader,
            "subject": subject,
            "tags": tags,
            "template_name": template_name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def external_id_remove(self, external_id_renames: Annotated[list[Any], ''] = None) -> Any:
        """
        Remove deprecated external IDs for users, returning confirmations and any errors encountered.
        
        Args:
            external_id_renames: A list of deprecated external IDs to remove (default is None).
        
        Returns:
            A JSON response containing a status message, successful removals, and error messages if applicable.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, external-id-management, user-data, async-job, important
        """
        request_body = {
            "external_id_renames": external_id_renames,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_new_user_aliases(self, user_aliases: Annotated[list[Any], ''] = None) -> Any:
        """
        Create new user aliases for existing users or create new unidentified users by adding their alias information.
        
        Args:
            user_aliases: Annotated list of new user alias objects. Each object may include an `external_id` to associate with an existing user.
        
        Returns:
            JSON response from the server.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails (e.g., status code 4XX or 5XX).
        
        Tags:
            create, user-aliases, management, important
        """
        request_body = {
            "user_aliases": user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_delete(self, braze_ids: Annotated[list[Any], ''] = None, external_ids: Annotated[list[Any], ''] = None, user_aliases: Annotated[list[Any], ''] = None) -> Any:
        """
        Deletes user profiles permanently using Braze identifiers. Only one identifier type (braze_ids, external_ids, or user_aliases) can be provided per request.
        
        Args:
            braze_ids: Braze user identifiers for users to delete (max 50 per request)
            external_ids: External identifiers for users to delete (max 50 per request)
            user_aliases: User alias objects for users to delete (max 50 per request)
        
        Returns:
            JSON response from Braze API after deletion request
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication issues, or server errors
        
        Tags:
            user-data-management, delete, core-operation, api-integration, user-profile, important
        """
        request_body = {
            "braze_ids": braze_ids,
            "external_ids": external_ids,
            "user_aliases": user_aliases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def identify_users(self, aliases_to_identify: Annotated[list[Any], ''] = None) -> Any:
        """
        Identifies users by associating aliases with an external ID, merging alias data into the identified user's record.
        
        Args:
            aliases_to_identify: List of alias objects requiring association with an external ID. Each entry must include a valid `external_id` and a `user_alias` containing `alias_name` and `alias_label`.
        
        Returns:
            Parsed JSON response from the API containing identification results or error details.
        
        Raises:
            requests.exceptions.HTTPError: Raised for failed API requests (non-2xx status codes), including invalid inputs or authentication issues.
        
        Tags:
            user-identification, aliases, external-id, important, user-data, api
        """
        request_body = {
            "aliases_to_identify": aliases_to_identify,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def user_track(self, attributes: Annotated[list[Any], ''] = None, events: Annotated[list[Any], ''] = None, purchases: Annotated[list[Any], ''] = None) -> Any:
        """
        Tracks user data including attributes, events, and purchases via Braze API, handling complex data requirements and rate limits.
        
        Args:
            attributes: Optional list of user attribute objects to update (see User Attributes Object documentation)
            events: Optional list of event objects to record (see Events Object documentation)
            purchases: Optional list of purchase objects to log (see Purchases Object documentation)
        
        Returns:
            Parsed JSON response containing processing results, potential non-fatal errors, or queue status
        
        Raises:
            HTTPError: Raised for 4XX/5XX status codes including bad requests (400), unauthorized access (401), rate limits (429), or server errors (5XX)
        
        Tags:
            user-data, track, async-job, important, braze, analytics
        """
        request_body = {
            "attributes": attributes,
            "events": events,
            "purchases": purchases,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
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
            self.create_scheduled_messages,
            self.schedule_api_triggered_campaigns,
            self.schedule_api_triggered_canvases,
            self.update_scheduled_messages,
            self.update_scheduled_api_triggered_campaigns,
            self.update_scheduled_api_triggered_canvases,
            self.create_send_ids_for_message_send_tracking,
            self.sending_messages_immediately_via_api_only,
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