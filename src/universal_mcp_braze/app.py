from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class BrazeApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='braze', integration=integration, **kwargs)
        self.base_url = "https://rest.iad-01.braze.com"


    def query_hard_bounced_emails(self, email: Annotated[Any, '(Optional*) String\n\nIf provided, we will return whether or not the user has hard bounced.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.'] = None, end_date: Annotated[Any, '(Optional*) String in YYYY-MM-DD format\n\nString in YYYY-MM-DD format. End date of the range to retrieve hard bounces. This is treated as midnight in UTC time by the API.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.'] = None, limit: Annotated[Any, '(Optional) Integer\n\nOptional field to limit the number of results returned. Defaults to 100, maximum is 500.'] = None, offset: Annotated[Any, '(Optional) Integer\n\nOptional beginning point in the list to retrieve from.'] = None, start_date: Annotated[Any, '(Optional*) String in YYYY-MM-DD format \n\nStart date of the range to retrieve hard bounces, must be earlier than `end_date`. This is treated as midnight in UTC time by the API.\n\n*You must provide either an `email` or a `start_date`, and an `end_date`.\n'] = None) -> Any:
        """
        Query Hard Bounced Emails. This endpoint allows you to pull a list of email addresses that have “hard bounced” your email messages within a certain time frame.

> You must provide an `end_date`, as well as either an `email` or a `start_date`.<br><br>If your date range has more than `limit` number of hard bounces, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.

## Response

Entries are listed in descending order.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "emails": [
    {
      "email": "example1@braze.com",
      "hard_bounced_at": "2016-08-25 15:24:32 +0000"
    },
    {
      "email": "example2@braze.com",
      "hard_bounced_at": "2016-08-24 17:41:58 +0000"
    },
    {
      "email": "example3@braze.com",
      "hard_bounced_at": "2016-08-24 12:01:13 +0000"
    }
  ],
  "message": "success"
}
```
        
        Tags: Email Lists & Addresses
        
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
        Query List of Unsubscribed Email Addresses. Use the /email/unsubscribes endpoint to return emails that have unsubscribed during the time period from `start_date` to `end_date`. You can use this endpoint to set up a bi-directional sync between Braze and other email systems or your own database.

> You must provide either an email or a start_date and an end_date. <br><br>If your date range has more than `limit` number of unsubscribes, you will need to make multiple API calls, each time increasing the `offset` until a call returns either fewer than `limit` or zero results.
        
        Tags: Email Lists & Addresses
        
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
        Change Email Subscription Status. This endpoint allows you to set the email subscription state for your users. Users can be opted_in, unsubscribed, or subscribed (not specifically opted in or out).

You can set the email subscription state for an email address that is not yet associated with any of your users within Braze. When that email address is subsequently associated with a user, the email subscription state that you uploaded will be automatically set.

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `email` | Yes | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
| `subscription_state` | Yes | String | Either “subscribed”, “unsubscribed”, or “opted_in”. |
        
        Tags: Email Lists & Addresses
        
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
        Remove Hard Bounced Emails. This endpoint allows you to remove email addresses from your Braze bounce list. We will also remove them from the bounce list maintained by your email provider.

| Parameter | Required | Data Type | Description |
| ----------|-----------| --------|------- |
| `email` | Yes | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
        
        Tags: Email Lists & Addresses
        
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
        Remove Email Addresses from Spam List. This endpoint allows you to remove email addresses from your Braze spam list. We will also remove them from the spam list maintained by your email provider.

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `email` | Yes | String or array | String email address to modify, or an array of up to 50 email addresses to modify. |
        
        Tags: Email Lists & Addresses
        
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
        Blacklist Email Addresses. Blacklisting an email address will unsubscribe the user from email and mark them as hard bounced.

| Parameter | Required | Data Type | Description |
| ----------|-----------| ---------|------ |
| `email` | Yes | String or Array | String email address to modify, or an Array of up to 50 email addresses to modify. |
        
        Tags: Email Lists & Addresses
        
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
        Campaign Analytics. This endpoint allows you to retrieve a daily series of various stats for a campaign over time. Data returned includes how many messages were sent, opened, clicked, converted, etc., broken down by message channel. 

### Components Used
-[Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)


### Responses

#### Multi-Channel Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "messages" : {
                "ios_push" : [
                    {
                      "variation_name": "iOS_Push",
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                      "revenue": 0,
                      "unique_recipients": 1,
                      "conversions": 0,
                      "conversions_by_send_time": 0,
                      "conversions1": 0,
                      "conversions1_by_send_time": 0,
                      "conversions2": 0,
                      "conversions2_by_send_time": 0,
                      "conversions3": 0,
                      "conversions3_by_send_time": 0,
                      "carousel_slide_[NUM]_[TITLE]_click": (optional, int),
                      "notif_button_[NUM]_[TITLE]_click": (optional, int)
                    }
                ],
                "android_push" : [
                    {
                      "sent" : (int),
                      "direct_opens" : (int),
                      "total_opens" : (int),
                      "bounces" : (int),
                      "body_clicks" : (int)
                    }
                ],
                "webhook": [
                    {
                      "sent": (int),
                      "errors": (int)
                    }
                ],
                "email" : [
                    {
                      "sent": (int),
                      "opens": (int),
                      "unique_opens": (int),
                      "clicks": (int),
                      "unique_clicks": (int),
                      "unsubscribes": (int),
                      "bounces": (int),
                      "delivered": (int),
                      "reported_spam": (int)
                    }
                ],
                "sms" : [
                  {
                    "sent": (int),
                    "delivered": (int),
                    "undelivered": (int),
                    "delivery_failed": (int)
                  }
                ]
              },
           "conversions_by_send_time": (optional, int),
           "conversions1_by_send_time": (optional, int),
           "conversions2_by_send_time": (optional, int),
           "conversions3_by_send_time": (optional, int),
           "conversions": (int),
           "conversions1": (optional, int),
           "conversions2": (optional, int),
           "conversions3": (optional, int),
           "unique_recipients": (int),
           "revenue": (optional, float)
        },
        ...
    ],
    ...
}
```

#### Multivariate Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "conversions" : (int),
            "revenue": (float),
            "conversions_by_send_time": (int),
            "messages" : {
               "trigger_in_app_message": [{
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"impressions": (int),
      				"clicks": (int),
      				"first_button_clicks": (int),
      				"second_button_clicks": (int),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int).
      				"conversions3_by_send_time": (optional, int)
      			}, {
      				"variation_name": (optional, string),
      				"revenue": (optional, float),,
      				"unique_recipients": (int),
      				"conversions": (optional, int),
      				"conversions_by_send_time": (optional, int),
      				"conversions1": (optional, int),
      				"conversions1_by_send_time": (optional, int),
      				"conversions2": (optional, int),
      				"conversions2_by_send_time": (optional, int),
      				"conversions3": (optional, int),
      				"conversions3_by_send_time": (optional, int),
      				"enrolled": (optional, int)
      			}]
      		},
      		"conversions_by_send_time": (optional, int),
      		"conversions1_by_send_time": (optional, int),
      		"conversions2_by_send_time": (optional, int),
      		"conversions3_by_send_time": (optional, int),
      		"conversions": (optional, int,
      		"conversions1": (optional, int),
      		"conversions2": (optional, int),
      		"conversions3": (optional, int),
      		"unique_recipients": (int),
      		"revenue": (optional, float)
         }],
         ...
}
```

Possible message types are `email`, `in_app_message`, `webhook`, `android_push`, `apple_push`, `kindle_push`, `web_push`, `windows_phone8_push`, and `windows_universal_push`. All push message types will have the same statistics shown for `android_push` above.
        
        Tags: Export, Campaign
        
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
        Campaign Details. This endpoint allows you to retrieve relevant information on a specified campaign, which can be identified by the `campaign_id`. 

> The campaign_id for API campaigns can be found on the Developer Console page and the campaign details page within your dashboard or you can use the Campaign List Endpoint.

### Components Used
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)


### Campaign Details Endpoint API Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "created_at" : (string) date created as ISO 8601 date,
    "updated_at" : (string) date last updated as ISO 8601 date,
    "archived": (boolean) whether this Campaign is archived,
    "draft": (boolean) whether this Campaign is a draft,
    "name" : (string) campaign name,
    "description" : (string) campaign description,
    "schedule_type" : (string) type of scheduling action,
    "channels" : (array) list of channels to send via,
    "first_sent" : (string) date and hour of first sent as ISO 8601 date,
    "last_sent" : (string) date and hour of last sent as ISO 8601 date,
    "tags" : (array) tag names associated with the campaign,
    "messages": {
        "message_variation_id": (string) { // <=This is the actual id
            "channel": (string) channel type of the message (as in, "email", "ios_push", "webhook", "content_card", "in-app_message", "sms"),
            "name": (string) name of the message in the Dashboard (eg., "Variation 1")
            ... channel-specific fields for this message, see below ...
        }
    },
    "conversion_behaviors": (array) conversion event behaviors assigned to the campaign (see below)
}
```

#### Messages

The `messages` response will contain information about each message. Example message responses for channels are below:

##### Push Channels

```json
{
    "channel": (string) description of the channel, such as "ios_push" or "android_push"
    "alert": (string) alert body text,
    "extras": (hash) any key value pairs provided
}
```

##### Email Channel

```json
{
    "channel": "email",
    "subject": (string) subject,
    "body": (string) HTML body,
    "from": (string) from address and display name,
    "reply_to": (string) reply-to for message, if different than "from" address,
    "title": (string) name of the email,
    "extras": (hash) any key value pairs provided
}
```

##### Content Card Channel

```json
{
    "channel": "content_cards",
    "name": (string) name of variant,
    "extras": (hash) any key value pairs provided; only present if at least one key-value pair has been set
}
```

##### Webhook Channel

```json
{
    "channel": "webhook",
    "url": (string) url for webhook,
    "body": (string) payload body,
    "type": (string) body content type,
    "headers": (hash) specified request headers,
    "method": (string) HTTP method (e.g., "POST" or "GET"),
}
```

##### SMS Channel

```json
{
  "channel": "sms",
  "body": (string) payload body,
  "from": (string) list of numbers associated with the subscription group,
  "subscription_group_id": (string) API id of the subscription group targeted in the SMS message
}
```

##### Control Messages

```json
{
    "channel": (string) description of the channel that the control is for,
    "type": "control"
}
```

#### Conversion Behaviors

The `conversion_behaviors` array will contain information about each conversion event behavior set for the campaign. These behaviors are in order as set by the campaign. For example, Conversion Event A will be the first item in the array, Conversion Event B will be second, etc. Example conversion event behavior responses for are below:

##### Clicks Email

```json
{
    "type": "Clicks Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

##### Opens Email

```json
{
    "type": "Opens Email",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

##### Makes Purchase (any purchase)

```json
{
    "type": "Makes Any Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours
}
```

##### Makes Purchase (specific product)

```json
{
    "type": "Makes Specific Purchase",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "product": (string) name of the product, i.e. - "Feline Body Armor"
}
```

##### Performs Custom Event

```json
{
    "type": "Performs Custom Event",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "custom_event_name": (string) name of the event, i.e. - "Used Feline Body Armor"
}
```

##### Upgrades App

```json
{
    "type": "Upgrades App",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```

##### Uses App

```json
{
    "type": "Starts Session",
    "window": (integer) number of seconds during which the user can convert on this event, i.e. - 86400, which is 24 hours,
    "app_ids": (array|null) array of app ids, i.e. - ["12345", "67890"], or `null` if "Track sessions for any app" is selected in the UI
}
```
        
        Tags: Export, Campaign
        
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
        Send Analytics. This endpoint allows you to retrieve a daily series of various stats for a tracked `send_id`. Braze stores send analytics for 14 days after the send.

Campaign conversions will be attributed towards the most recent send id that a given user has received from the campaign.

> The `send_id` is only generated for API campaign sends targeting segments, connected audiences or broadcasts. When relevant, the `send_id` is included in response for the `messages/send`, `messages/schedule`, `campaign/trigger/send` and `campaign/trigger/schedule` endpoints.

### Components Used
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)

### Send Analytics Endpoint API Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
            "variation_name": (string) variation name,
            "sent": (int) the number of sends,
            "delivered": (int) the number of messages successfully delivered,
            "undelivered": (int) the number of undelivered,
            "delivery_failed": (int) the number of rejected,
            "direct_opens": (int) the number of direct opens,
            "total_opens": (int) the number of total opens,
            "bounces": (int) the number of bounces,
            "body_clicks": (int) the number of body clicks,
            "revenue": (float) the number of dollars of revenue (USD),
            "unique_recipients": (int) the number of unique recipients,
            "conversions": (int) the number of conversions,
            "conversions_by_send_time": (int) the number of conversions,
            "conversions1": (int, optional) the number of conversions for the second conversion event,
            "conversions1_by_send_time": (int, optional) the number of conversions for the second conversion event by send time,
            "conversions2": (int, optional) the number of conversions for the third conversion event,
            "conversions2_by_send_time": (int, optional) the number of conversions for the third conversion event by send time,
            "conversions3": (int, optional) the number of conversions for the fourth conversion event,
            "conversions3_by_send_time": (int, optional) the number of conversions for the fourth conversion event by send time
          }
        ]
      },
      "conversions_by_send_time": 0,
      "conversions1_by_send_time": 0,
      "conversions2_by_send_time": 0,
      "conversions3_by_send_time": 0,
      "conversions": 0,
      "conversions1": 0,
      "conversions2": 0,
      "conversions3": 0,
      "unique_recipients": 1,
      "revenue": 0
    }
  ],
  "message": "success"
}
```
        
        Tags: Export, Campaign
        
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
        Canvas Data Series Analytics. This endpoint allows you to export time series data for a Canvas.

### Components Used
- [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) Canvas name,
    "stats": [
      {
        "time": (string) date as ISO 8601 date,
        "total_stats": {
          "revenue": (float),
          "conversions": (int),
          "conversions_by_entry_time": (int),
          "entries": (int)
        },
        "variant_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
            "name": (string) name of variant,
            "revenue": (int),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "entries": (int)
          },
          ... (more variants)
        },
        "step_stats": (optional) {
          "00000000-0000-0000-0000-0000000000000": (API identifier for step) {
            "name": (string) name of step,
            "revenue": (float),
            "conversions": (int),
            "conversions_by_entry_time": (int),
            "messages": {
              "email": [
                {
                  "sent": (int),
                  "opens": (int),
                  "unique_opens": (int),
                  "clicks": (int),
                  ... (more stats)
                }
              ],
              ... (more channels)
            }
          },
          ... (more steps)
        }
      },
      ... (more stats by time)
    ]
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```
        
        Tags: Export, Canvas
        
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
        Canvas Data Analytics Summary. This endpoint allows you to export rollups of time series data for a Canvas, providing a concise summary of a Canvas' results.

### Components Used
- [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "data": {
    "name": (string) Canvas name,
    "total_stats": {
      "revenue": (float),
      "conversions": (int),
      "conversions_by_entry_time": (int),
      "entries": (int)
    },
    "variant_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (API identifier for variant) {
        "name": (string) name of variant,
        "revenue": (float),
        "conversions": (int),
        "entries": (int)
      },
      ... (more variants)
    },
    "step_stats": (optional) {
      "00000000-0000-0000-0000-0000000000000": (API identifier for step) {
        "name": (string) name of step,
        "revenue": (float),
        "conversions": (int),
        "conversions_by_entry_time": (int),
        "messages": {
          "android_push": (name of channel) [
            {
              "sent": (int),
              "opens": (int),
              "influenced_opens": (int),
              "bounces": (int)
              ... (more stats for channel)
            }
          ],
          ... (more channels)
        }
      },
      ... (more steps)
    }
  },
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```
        
        Tags: Export, Canvas
        
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
        Canvas Details. This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more.

### Components Used
- [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "created_at": (string) date created as ISO 8601 date,
  "updated_at": (string) date updated as ISO 8601 date,
  "name": (string) Canvas name,
  "description": (string) Canvas description,
  "archived": (boolean) whether this Canvas is archived,
  "draft": (boolean) whether this Canvas is a draft,
  "schedule_type": (string) type of scheduling action,
  "first_entry": (string) date of first entry as ISO 8601 date,
  "last_entry": (string) date of last entry as ISO 8601 date,
  "channels": (array of strings) step channels used with Canvas,
  "variants": [
    {
      "name": (string) name of variant,
      "id": (string) API identifier of the variant,
      "first_step_ids": (array of strings) API identifiers for first steps in variant,
      "first_step_id": (string) API identifier of first step in variant (deprecated in November 2017, only included if the variant has only one first step)
    },
    ... (more variations)
  ],
  "tags": (array of strings) tag names associated with the Canvas,
  "steps": [
    {
      "name": (string) name of step,
      "id": (string) API identifier of the step,
      "next_step_ids": (array of strings) API identifiers of steps following step,
      "channels": (array of strings) channels used in step,
      "messages": {
          "message_variation_id": (string) {  // <=This is the actual id
              "channel": (string) channel type of the message (eg., "email"),
              ... channel-specific fields for this message, see Campaign Details Endpoint API Response for example message responses ...
          }
      }
    },
    ... (more steps)
  ],
  "message": (required, string) the status of the export, returns 'success' when completed without errors
}
```
        
        Tags: Export, Canvas
        
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
        Custom Events List. This endpoint allows you to export a list of custom events that have been recorded for your app. The event names are returned in groups of 250, sorted alphabetically.


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "events" : [
        "Event A",
        "Event B",
        "Event C",
        ...
    ]
}
```

### Fatal Error Response Codes

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code       | Reason / Cause                                                   |
| ---------------- | ---------------------------------------------------------------- |
| 400 Bad Request  | Bad Syntax                                                       |
| 401 Unauthorized | Unknown or missing REST API Key                                  |
| 429 Rate Limited | Over rate limit                                                  |
| 5XX              | Internal server error, you should retry with exponential backoff |
        
        Tags: Export, Custom Events
        
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
        Custom Events Analytics. This endpoint allows you to retrieve a series of the number of occurrences of a custom event in your app over a designated time period.

### Components Used
-[Segment Identifier](https://www.braze.com/docs/api/identifier_types/)


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "count" : (int)
        },
        ...
    ]
}
```

### Fatal Error Response Codes
The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code       | Reason / Cause                                                   |
| ---------------- | ---------------------------------------------------------------- |
| 400 Bad Request  | Bad Syntax                                                       |
| 401 Unauthorized | Unknown or missing REST API Key                                  |
| 429 Rate Limited | Over rate limit                                                  |
| 5XX              | Internal server error, you should retry with exponential backoff |
        
        Tags: Export, Custom Events
        
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
        Daily New Users by Date. This endpoint allows you to retrieve a daily series of the total number of new users on each date.


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "new_users" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, KPI
        
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
        Daily Active Users by Date. This endpoint allows you to retrieve a daily series of the total number of unique active users on each date.


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "dau" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, KPI
        
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
        Monthly Active Users for Last 30 Days. This endpoint allows you to retrieve a daily series of the total number of unique active users over a 30-day rolling window.

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "mau" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, KPI
        
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
        KPIs for Daily App Uninstalls by Date. This endpoint allows you to retrieve a daily series of the total number of uninstalls on each date.

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "uninstalls" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, KPI
        
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
        News Feed Card Analytics. This endpoint allows you to retrieve a daily series of engagement stats for a card over time.

### Components Used
- [Card ID](https://www.braze.com/docs/api/identifier_types/)
- [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "clicks" : (int) ,
            "impressions" : (int),
            "unique_clicks" : (int),
            "unique_impressions" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, News Feed
        
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
        News Feed Cards Details. This endpoint allows you to retrieve relevant information on the card, which can be identified by the `card_id`.

### Components Used
- [Card ID](https://www.braze.com/docs/api/identifier_types/)
- [News Feed List](https://www.braze.com/docs/api/endpoints/export/news_feed/get_news_feed_cards/)


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) The status of the export, returns 'success' when completed without errors,
    "created_at" : (string) Date created as ISO 8601 date,
    "updated_at" : (string) Date last updated as ISO 8601 date,
    "name" : (string) Card name,
    "publish_at" : (string) Date card was published as ISO 8601 date,
    "end_at" : (string) Date card will stop displaying for users as ISO 8601 date,
    "tags" : (array) Tag names associated with the card,
    "title" : (string) Title of the card,
    "image_url" : (string) Image URL used by this card,
    "extras" : (dictionary) Dictionary containing key-value pair data attached to this card,
    "description" : (string) Description text used by this card,
    "archived": (boolean) whether this Card is archived,
    "draft": (boolean) whether this Card is a draft,
}
```
        
        Tags: Export, News Feed
        
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
        News Feed Cards List. This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. The cards are returned in groups of 100 sorted by time of creation (oldest to newest by default).


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "cards" : [
        {
            "id" : (string) Card API Identifier,
            "type" : (string) type of the card - NewsItem (classic cards), CaptionedImage, Banner or DevPick (cross-promotional cards),
            "title" : (string) title of the card,
            "tags" : (array) tag names associated with the card
        },
        ...
    ]
}
```
        
        Tags: Export, News Feed
        
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
        Segment List. This endpoint allows you to export a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. The segments are returned in groups of 100 sorted by time of creation (oldest to newest by default). Archived segments are not included.

### Request Components
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "segments" : [
        {
            "id" : (string) Segment API Identifier,
            "name" : (string) segment name,
            "analytics_tracking_enabled" : (boolean) whether the segment has analytics tracking enabled,
            "tags" : (array) tag names associated with the segment
        },
        ...
    ]
}
```
        
        Tags: Export, Segment
        
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
        Segment Analytics. This endpoint allows you to retrieve a daily series of the size of a segment over time for a segment.

### Request Components
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) date as ISO 8601 date,
            "size" : (int) size of the segment on that date
        },
        ...
    ]
}
```
        
        Tags: Export, Segment
        
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
        Segment Details. This endpoint allows you to retrieve relevant information on the segment, which can be identified by the `segment_id`.

### Request Components
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
      "message": (required, string) the status of the export, returns 'success' when completed without errors,
      "created_at" : (string) date created as ISO 8601 date,
      "updated_at" : (string) date last updated as ISO 8601 date,
      "name" : (string) segment name,
      "description" : (string) human-readable description of filters,
      "text_description" : (string) segment description, 
      "tags" : (array) tag names associated with the segment
}
```
        
        Tags: Export, Segment
        
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
        App Sessions by Time. This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period.

### Components Used
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "data" : [
        {
            "time" : (string) point in time - as ISO 8601 extended when unit is "hour" and as ISO 8601 date when unit is "day",
            "sessions" : (int)
        },
        ...
    ]
}
```
        
        Tags: Export, Session Analytics
        
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
        User Profile Export by Identifier. This endpoint allows you to export data from any user profile by specifying a form of user identifier. Up to 50 `external_ids` or `user_aliases` can be included in a single request. Should you want to specify `device_id` or `email_address` only one of either identifier can be included per request..

## Request Parameters

| Key | Requirement | Data Type | Details |
|-----|-----|-----|-----|
|`external_ids` | Optional | Array of strings | External identifiers for users you wish export |
|`user_aliases` | Optional | Array of user alias object | User aliases for users to export |
|`device_id` | Optional | String | Device identifier as returned by various SDK methods such as `getDeviceId` |
|`braze_id` | Optional | String | Braze identifier for a particular user |
|`email_address` | Optional | String | Email address of user |
|`phone` | Optional | String | Phone number of user |
|`fields_to_export` | Optional | Array of strings | Name of user data fields to export. Defaults to all if not provided |

### Request Component
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)

### Fields to Export

The following is a list of valid `fields_to_export`. Using `fields_to_export` to minimize the data returned can improve response time of this API endpoint:

* `apps`
* `attributed_campaign`
* `attributed_source`
* `attributed_adgroup`
* `attributed_ad`
* `braze_id`
* `campaigns_received`
* `canvases_received`
* `cards_clicked`
* `country`
* `created_at`
* `custom_attributes`
* `custom_events`
* `devices`
* `dob`
* `email`
* `email_subscribe`
* `external_id`
* `first_name`
* `gender`
* `home_city`
* `language`
* `last_coordinates`
* `last_name`
* `phone`
* `purchases`
* `push_subscribe`
* `push_tokens`
* `random_bucket`
* `time_zone`
* `total_revenue`
* `uninstalled_at`
* `user_aliases`

Please be aware that the `/users/export/ids` endpoint will pull together the entire user profile for this user, including data such as all campaigns and canvases received, all custom events performed, all purchases made, and all custom attributes. As a result, this endpoint is slower than other REST API endpoints.

Depending on the data requested, this API endpoint may have not be able to fulfill your hourly API rate limit. If you anticipate using this endpoint regularly to export users, instead consider exporting users by segment, which is asynchronous and more optimized for larger data pulls. Documentation on that endpoint is below.

### Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "users" : (array of object) the data for each of the exported users, may be empty if no users are found,
    "invalid_user_ids" : (optional, array of string) each of the identifiers provided in the request that did not correspond to a known user
}
```

For an example of the data that is accessible via this endpoint see the example below.

### Sample User Export File Output

User export object (we will include the least data possible - if a field is missing from the object it should be assumed to be null, false, or empty):

```json
{
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string),
    "phone" : (string),
    "language" : (string) ISO-639 two letter code,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key value pairs,
    "custom_events" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "purchases" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "devices" : [
        {
            "model" : (string),
            "os" : (string),
            "carrier" : (string),
            "idfv" : (string) only included for iOS devices,
            "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
            "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
            "roku_ad_id" : (string) only included for Roku devices,
            "windows_ad_id" : (string) only included for Windows devices,
            "ad_tracking_enabled" : (bool)
        },
        ...
    ],
    "push_tokens" : [
        {
            "app" : (string) app name,
            "platform" : (string),
            "token" : (string)
        },
        ...
    ],
    "apps" : [
        {
            "name" : (string),
            "platform" : (string),
            "version" : (string),
            "sessions" : (integer),
            "first_used" : (string) date,
            "last_used" : (string) date
        },
        ...
    ],
    "campaigns_received" : [
        {
            "name" : (string),
            "last_received" : (string) date,
            "engaged" : {
                "opened_email" : (bool),
                "opened_push" : (bool),
                "clicked_email" : (bool),
                "clicked_triggered_in_app_message" : (bool)
            },
            "converted" : (bool),
            "api_campaign_id" : (string),
            "variation_name" : (optional, string) exists only if it is a multivariate campaign,
            "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
            "in_control" : (optional, bool) exists only if it is a multivariate campaign
        },
        ...
    ],
    "canvases_received": [
        {
            "name": (string),
            "api_canvas_id": (string),
            "last_received_message": (string) date,
            "last_entered": (string) date,
            "variation_name": (string),
            "in_control": (bool),
            "last_exited": (string) date,
            "steps_received": [
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                }
            ]
        },
        ...
    ],
    "cards_clicked" : [
        {
            "name" : (string)
        },
        ...
    ]
}
```
        
        Tags: Export, Users
        
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
        User Profile Export by Segment. This endpoint allows you to export all the users within a segment. User data is exported as multiple files of user JSON objects separated by new lines (i.e. one JSON object per line).

> Beginning April 2021, the "fields_to_export" field in this API request will be __required for all new accounts__. The option to default to all field will be removed, and new customers will need to specify the specific fields they'd like to include in their export.

## Request Parameters

| Key | Requirement | Data Type | Details |
|---|---|---|---|
|`segment_id` | Required | String | Identifier for the segment to be exported |
|`callback_endpoint` | Optional | String | Endpoint to post a download url to when the export is available |
|`fields_to_export` | Required* | Array of Strings | Name of user data fields to export, you may also export custom attributes. *Beginning April 2021, new accounts must specify specific fields to export. |
|`output_format` | Optional | String | When using your own S3 bucket, allows to specify file format as 'zip' or 'gzip'. Defaults to zip file format |

### Components Used
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)


### Fields to Export

The following is a list of valid `fields_to_export`. Using `fields_to_export` to minimize the data returned can improve response time of this API endpoint:

* `apps`
* `attributed_campaign`
* `attributed_source`
* `attributed_adgroup`
* `attributed_ad`
* `braze_id`
* `campaigns_received`
* `canvases_received`
* `cards_clicked`
* `country`
* `created_at`
* `custom_attributes`
* `custom_events`
* `devices`
* `dob`
* `email`
* `email_subscribe`
* `external_id`
* `first_name`
* `gender`
* `home_city`
* `language`
* `last_coordinates`
* `last_name`
* `phone`
* `purchases`
* `push_subscribe`
* `push_tokens`
* `random_bucket`
* `time_zone`
* `total_revenue`
* `uninstalled_at`
* `user_aliases`

### Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "message": (required, string) the status of the export, returns 'success' when completed without errors,
    "object_prefix": (required, string) the filename prefix that will be used for the JSON file produced by this export, e.g. 'bb8e2a91-c4aa-478b-b3f2-a4ee91731ad1-1464728599',
    "url" : (optional, string) the URL where the segment export data can be downloaded if you do not have your own S3 credentials
}
```

Once made available, the URL will only be valid for a few hours. As such, we highly recommend that you add your own S3 credentials to Braze.

### Sample User Export File Output

User export object (we will include the least data possible - if a field is missing from the object it should be assumed to be null, false, or empty):

```json
{
    "external_id" : (string),
    "user_aliases" : [
      {
        "alias_name" : (string),
        "alias_label" : (string)
      }
    ],
    "braze_id": (string),
    "first_name" : (string),
    "last_name" : (string),
    "email" : (string),
    "dob" : (string) date for the user's date of birth,
    "home_city" : (string),
    "country" : (string),
    "phone" : (string),
    "language" : (string) ISO-639 two letter code,
    "time_zone" : (string),
    "last_coordinates" : (array of float) [lon, lat],
    "gender" : (string) "M" | "F",
    "total_revenue" : (float),
    "attributed_campaign" : (string),
    "attributed_source" : (string),
    "attributed_adgroup" : (string),
    "attributed_ad" : (string),
    "push_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "email_subscribe" : (string) "opted_in" | "subscribed" | "unsubscribed",
    "custom_attributes" : (object) custom attribute key value pairs,
    "custom_events" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "purchases" : [
        {
            "name" : (string),
            "first" : (string) date,
            "last" : (string) date,
            "count" : (int)
        },
        ...
    ],
    "devices" : [
        {
            "model" : (string),
            "os" : (string),
            "carrier" : (string),
            "idfv" : (string) only included for iOS devices,
            "idfa" : (string) only included for iOS devices when IDFA collection is enabled,
            "google_ad_id" : (string) only included for Android devices when Google Play Advertising Identifier collection is enabled,
            "roku_ad_id" : (string) only included for Roku devices,
            "windows_ad_id" : (string) only included for Windows devices,
            "ad_tracking_enabled" : (bool)
        },
        ...
    ],
    "push_tokens" : [
        {
            "app" : (string) app name,
            "platform" : (string),
            "token" : (string)
        },
        ...
    ],
    "apps" : [
        {
            "name" : (string),
            "platform" : (string),
            "version" : (string),
            "sessions" : (string),
            "first_used" : (string) date,
            "last_used" : (string) date
        },
        ...
    ],
    "campaigns_received" : [
        {
            "name" : (string),
            "last_received" : (string) date,
            "engaged" : {
                "opened_email" : (bool),
                "opened_push" : (bool),
                "clicked_email" : (bool),
                "clicked_in_app_message" : (bool)
            },
            "converted" : (bool),
            "api_campaign_id" : (string),
            "variation_name" : (optional, string) exists only if it is a multivariate campaign,
            "variation_api_id" : (optional, string) exists only if it is a multivariate campaign,
            "in_control" : (optional, bool) exists only if it is a multivariate campaign
        },
        ...
    ],
    "canvases_received": [
        {
            "name": (string),
            "api_canvas_id": (string),
            "last_received_message": (string) date,
            "last_entered": (string) date,
            "variation_name": (string),
            "in_control": (bool),
            "last_exited": (string) date,
            "steps_received": [
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                },
                {
                    "name": (string),
                    "api_canvas_step_id": (string),
                    "last_received": (string) date
                }
            ]
        },
        ...
    ],
    "cards_clicked" : [
        {
            "name" : (string)
        },
        ...
    ]
}
```
        
        Tags: Export, Users
        
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
        User Profile Export by Global Control Group. User Profile Export by Global Control Group
        
        Tags: Export, Users
        
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
        Get Upcoming Scheduled Campaigns and Canvases. You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. The endpoint will return information about scheduled Campaigns and entry Canvases between now and the designated end_time (ISO 8601 format) specified in the request. Daily, recurring messages will only appear once with their next occurrence. Results returned in this endpoint are only for Campaigns and Canvases created and scheduled in Braze.

## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
    "scheduled_broadcasts": [
      # Example Canvas
      {
        "name" => String,
        "id" => String,
        "type" => "Canvas",
        "tags" => [String tag names],
        "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
        "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
      },
      # Example Campaign
      {
        "name" => String,
        "id" => String,
        "type" => "Campaign",
        "tags" => [String tag names],
        "next_send_time" => "YYYY-MM-DD HH:mm:ss" (may also include time zone if not local/intelligent delivery)
        "schedule_type" => one of "local_time_zones", "intelligent_delivery", or the name of your company's time zone
      },
    ]
}
```
        
        Tags: Messaging, Schedule Mesages
        
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
        Delete Scheduled Messages. The delete scheduled messages endpoint allows you to cancel a message that you previously scheduled _before_ it has been sent.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `schedule_id` | Required | String | The schedule_id to delete (obtained from the response to create schedule) |

## Request Components
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Delete Scheduled API Triggered Campaigns. The delete schedule endpoint allows you to cancel a message that you previously scheduled API Triggered Campaigns before it has been sent.

Scheduled messages or triggers that are deleted very close to or during the time they were supposed to be sent will be updated with best efforts, so last second deletions could be applied to all, some, or none of your targeted users.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `campaign_id`|Required|String| See campaign identifier|
| `schedule_id` | Required | String | The schedule_id to delete (obtained from the response to create schedule) |

## Request Components
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Create Scheduled Messages. Use this endpoint to send messages directly from the API.

The create schedule endpoint allows you to schedule a Campaign, Canvas, or other message to be sent at a designated time (up to 90 days in the future) and provides you with an identifier to reference that message for updates. If you are targeting a segment, a record of your request will be stored in the Developer Console after all scheduled messages have been sent.

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `broadcast` | Optional | Boolean | See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted |
| `external_user_ids` | Optional | Array of strings | See external user identifier |
| `user_aliases` | Optional | Array of user alias objects | See user alias object |
| `audience` | Optional | Connected audience object | See connected audience |
| `segment_id` | Optional | String | See segment identifier |
| `campaign_id`|Required|String| See campaign identifier|
| `recipients` | Optional | Array of recipient objects | See recipients object |
| `send_id` | Optional | String | See send identifier | 
| `override_messaging_limits` | Optional | Boolean | Ignore global rate limits for campaigns, defaults to false |
| `recipient_subscription_state` | Optional | String | Use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed' |
| `schedule` | Required | Schedule object | See schedule object |
| `messages` | Optional | Messaging object | See messaging object |

### Request Components
- [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast)
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
- [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/)
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)
- [API Parameters](https://www.braze.com/docs/api/parameters)

### Available Messaging Objects

- [Android Objects](https://www.braze.com/docs/api/objects_filters/android_objects/)
- [Apple Objects](https://www.braze.com/docs/api/objects_filters/apple_objects/)
- [Content Cards Object](https://www.braze.com/docs/api/objects_filters/content_cards_object/)
- [Email Object](https://www.braze.com/docs/api/objects_filters/email_object/)
- [Kindle or FireOS Object](https://www.braze.com/docs/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object](https://www.braze.com/docs/api/objects_filters/sms_object/)
- [Web Objects](https://www.braze.com/docs/api/objects_filters/web_objects/)
- [Webhook Object](https://www.braze.com/docs/api/objects_filters/webhook_object/)
- [Windows Objects](https://www.braze.com/docs/api/objects_filters/windows_objects/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Schedule API Triggered Campaigns. Use this endpoint to trigger API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to send Campaign messages (up to 90 days in advance) via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an API Triggered Campaign.

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String| See campaign identifier|
|`send_id` | Optional | String | See send identifier |
|`recipients` | Optional | Array of recipient objects | See recipients object |
|`audience` | Optional | Connected audience object | See connected audience |
|`broadcast` | Optional | Boolean | See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" object is omitted |
| `trigger_properties` | Optional | Object | Personalization key value pairs for all users in this send; see trigger properties |
| `schedule` | Required | Schedule object | See schedule object |

## Request Components
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/)
- [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/)
- [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast)
- [Trigger Properties](https://www.braze.com/docs/api/objects_filters/trigger_properties_object/)
- [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Update Scheduled Messages. The messages update schedule endpoint accepts updates to either the `schedule` or `messages` parameter or both. Your request must contain at least one of those two keys.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`schedule_id`|Required|String| The schedule_id to update (obtained from the response to create schedule)|
|`schedule` | Optional | Object | See schedule object |
|`messages` | Optional | Object | See available message object |

## Request Components

- [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)

### Available Messaging Objects

- [Android Objects](https://www.braze.com/docs/api/objects_filters/android_objects/)
- [Apple Objects](https://www.braze.com/docs/api/objects_filters/apple_objects/)
- [Content Cards Object](https://www.braze.com/docs/api/objects_filters/content_cards_object/)
- [Email Object](https://www.braze.com/docs/api/objects_filters/email_object/)
- [Kindle or FireOS Object](https://www.braze.com/docs/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object](https://www.braze.com/docs/api/objects_filters/sms_object/)
- [Web Objects](https://www.braze.com/docs/api/objects_filters/web_objects/)
- [Webhook Object](https://www.braze.com/docs/api/objects_filters/webhook_objects/)
- [Windows Objects](https://www.braze.com/docs/api/objects_filters/windows_objects/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Update Scheduled API Triggered Campaigns. Use this endpoint to update scheduled API Triggered Campaigns, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to send Campaign messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an API Triggered Campaign.

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String| See campaign identifier|
|`schedule_id`| Optional | String | The schedule_id to update (obtained from the response to create schedule) |
|`schedule` | Required | Object | See schedule object |


## Request Components
- [Campaign ID](https://www.braze.com/docs/api/identifier_types/)
- [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Update Scheduled API Triggered Canvases. Use this endpoint to update scheduled API Triggered Canvases, which are created on the Dashboard and initiated via the API. You can pass in `trigger_properties` that will be templated into the message itself.

This endpoint allows you to update scheduled Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a Canvas.

Any schedule will completely overwrite the one that you provided in the create schedule request or in previous update schedule requests. For example, if you originally provide `"schedule" : {"time" : "2015-02-20T13:14:47", "in_local_time" : true}` and then in your update you provide `"schedule" : {"time" : "2015-02-20T14:14:47"}`, your message will now be sent at the provided time in UTC, not in the user's local time. Scheduled triggers that are updated very close to or during the time they were supposed to be sent will be updated with best efforts, so last-second changes could be applied to all, some, or none of your targeted users.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String| See canvas identifier|
|`schedule_id`| Optional | String | The schedule_id to update (obtained from the response to create schedule) |
|`schedule` | Required | Object | See schedule object |

## Request Components

- [Canvas ID](https://www.braze.com/docs/api/identifier_types/)
- [Schedule Object](https://www.braze.com/docs/api/objects_filters/schedule_object/)
        
        Tags: Messaging, Schedule Mesages
        
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
        Create Send IDs For Message Send Tracking. Braze’s Send Identifier adds the ability to send messages and track message performance entirely programmatically, without campaign creation for each send. Using the Send Identifier to track and send messages is useful if you are planning to programmatically generate and send content.

The daily maximum number of custom send identifiers that can be created via this endpoint for a given app group is 100. Each send id - campaign id combination that you create will count towards your daily limit. The response headers for any valid request include the current rate limit status. 

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String|See campaign identifier|
|`send_id`| Optional | String | See send identifier |

## Request Components
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)


## Response

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "message": "success",
  "send_id" : "example_send_id"
}
```
        
        Tags: Messaging, Send Messages
        
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
        Sending Messages Immediately via API Only. This endpoint allows you send your messages using our API. Be sure to include Messaging Objects in your body to complete your requests.

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the Developer Console .

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`broadcast`|Optional|Boolean|See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted|
|`external_user_ids` | Optional | Array of strings | See external identifier |
|`user_aliases`|Optional|Array of user alias objects| See user alias object|
|`segment_id `| Optional | String | See segment identifier |
|`audience`|Optional|Connected audience object|See connected audience|
|`campaign_id`|Optional*|String| *Required if you wish to track campaign stats (e.g. sends, clicks, bounces, etc) on the Braze dashboard. <br>See campaign identifier for more information|
|`send_id`| Optional | String | See send identifier |
|`override_frequency_capping`|Optional|Boolean|Ignore frequency_capping for campaigns, defaults to false |
|`recipient_subscription_state`|Optional|String|Use this to send messages to only users who have opted in ('opted_in'), only users who have subscribed or are opted in ('subscribed') or to all users, including unsubscribed users ('all'), the latter being useful for transactional email messaging. Defaults to 'subscribed'|
|`messages`| Optional | Messaging objects | See available messaging objects|

### Request Components
- [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast)
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
- [Segment Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/)
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/)
- [API Parameters](https://www.braze.com/docs/api/parameters)

### Available Messaging Objects

- [Android Objects](https://www.braze.com/docs/api/objects_filters/android_objects/)
- [Apple Objects](https://www.braze.com/docs/api/objects_filters/apple_objects/)
- [Content Cards Object](https://www.braze.com/docs/api/objects_filters/content_cards_object/)
- [Email Object](https://www.braze.com/docs/api/objects_filters/email_object/)
- [Kindle or FireOS Object](https://www.braze.com/docs/api/objects_filters/kindle_and_fireos_object/)
- [SMS Object](https://www.braze.com/docs/api/objects_filters/sms_object/)
- [Web Objects](https://www.braze.com/docs/api/objects_filters/web_objects/)
- [Webhook Object](https://www.braze.com/docs/api/objects_filters/webhook_object/)
- [Windows Objects](https://www.braze.com/docs/api/objects_filters/windows_objects/)


## Response Details

Message sending endpoint responses will include the message’s `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform). For more information on `dispatch_id` checkout out our [documentation]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
        
        Tags: Messaging, Send Messages
        
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
        Sending Campaign Messages via API Triggered Delivery. API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API.

The send endpoint allows you to send immediate, ad-hoc messages to designated users. If you are targeting a segment, a record of your request will be stored in the Developer Console. Please note that to send messages with this endpoint, you must have a Campaign ID, created when you build an API Triggered Campaign.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`campaign_id`|Required|String|See campaign identifier|
|`send_id`| Optional | String | See send identifier |
|`trigger_properties`|Optional|Object|Personalization key value pairs that will apply to all users in this request|
|`broadcast`|Optional|Boolean|See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted|
|`audience`|Optional|Connected audience object|See connected audience|
|`recipients`|Optional|Array|If not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the campaign|

### Request Components
- [Campaign Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast)
- [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/)
- [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/)
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
- [User Attributes Object](https://www.braze.com/docs/api/objects_filters/user_attributes_object/)
- [API Parameters](https://www.braze.com/docs/api/parameters)

The recipients array may contain up to 50 objects, with each object containing a single `external_user_id` string and `trigger_properties` object.

When `send_to_existing_only` is `true`, Braze will only send the message to existing users. When `send_to_existing_only` is `false` and a user with the given `id` does not exist, Braze will create a user with that id and attributes before sending the message.

For more information on the "broadcast" flag, check out [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast) within our [API Parameters](https://www.braze.com/docs/api/parameters) documentation.

## Response Details
Message sending endpoint responses will include the message’s `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform). 

## Create Send Endpoint

__Using the Attributes Object in Campaigns__

Braze has a Messaging Object called `Attributes` that will allow you to add, create, or update attributes and values for a user before you send them an API Triggered Campaigns using the `campaign/trigger/send` endpoint as this API call will process the User Attributes object before it processes and sends the campaign. This helps minimize the risk of there being issues caused by race conditions.
        
        Tags: Messaging, Send Messages
        
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
        Sending Canvas Messages via API Triggered Delivery. API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API.

This endpoint allows you to send Canvas messages via API Triggered delivery, allowing you to decide what action should trigger the message to be sent. Please note that to send messages with this endpoint, you must have a Canvas ID, created when you build a [Canvas](https://www.braze.com/api/identifier_types/#canvas-api-identifier).

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`canvas_id`|Required|String|See canvas identifier|
|`canvas_entry_properties`|Optional|Object|Personalization key value pairs that will apply to all users in this request|
|`broadcast`|Optional|Boolean|See broadcast -- defaults to false on 8/31/17, must be set to true if "recipients" is omitted|
|`audience`|Optional|Connected audience object|See connected audience|
|`recipients`|Optional|Array|If not provided and broadcast is not set to 'false', message will send to the entire segment targeted by the Canvas|

### Request Components
- [Canvas Identifier](https://www.braze.com/docs/api/identifier_types/)
- [Broadcast](https://www.braze.com/docs/api/parameters/#broadcast)
- [Connected Audience](https://www.braze.com/docs/api/objects_filters/connected_audience/)
- [Recipients](https://www.braze.com/docs/api/objects_filters/recipient_object/)
- [Canvas Entry Properties](https://www.braze.com/docs/api/objects_filters/canvas_entry_properties_object/)
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
- [User Attributes Object](https://www.braze.com/docs/api/objects_filters/user_attributes_object/)
- [API Parameters](https://www.braze.com/docs/api/parameters)

The `recipients` array may contain up to 50 objects, with each object containing a single `external_user_id` string and `canvas_entry_properties` object.

Customers using the API for server-to-server calls may need to whitelist the appropriate API URL if they're behind a firewall.

If you include both specific users in your API call and a target segment in the dashboard, the message will send to specifically the user profiles that are in the API call *and* qualify for the segment filters.

### Response Details
Message sending endpoint responses will include the message’s `dispatch_id` for reference back to the dispatch of the message. The `dispatch_id` is the id of the message dispatch (unique id for each ‘transmission’ sent from the Braze platform). For more information on `dispatch_id` checkout out our [documentation](https://www.braze.com/docs/help/help_articles/data/dispatch_id/).

## Create Send Endpoint

__Using the Attributes Object in Canvas__

Braze has a Messaging Object called `Attributes` that allows you to add, create, or update attributes and values for a user before sending them an API Triggered Canvas using the `canvas/trigger/send` endpoint as this API call will process the User Attributes object before it processes and sends the Canvas. This helps minimize the risk of there being issues caused by race conditions.
        
        Tags: Messaging, Send Messages
        
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
        List User's  Subscription Group Status - Email. Use the endpoint below to get the subscription state of a user in a subscription group. The response from this endpoint will include the external ID and either subscribed, unsubscribed, or unknown for the specific subscription group requested in the API call. This can be used to update the subscription group state in subsequent API calls or to be displayed on a hosted web page.

> *Either `external_id` or `email` are required.

## Response

All successful responses will return `subscribed`, `unsubscribed`, or `unknown` depending on status and user history with the subscription group.

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "status": {
    "1": "Unsubscribed",
    "2": "Subscribed"
  },
  "message": "success"
}
```
        
        Tags: Subscription Groups, SMS
        
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
        List User's Subscription Group - Email. Use the endpoint below to list and get the subscription groups of a certain user.

> If there are multiple users (multiple external ids) who share the same email address, all users will be returned as a separate user (even if they have the same email address or subscription group).
        
        Tags: Subscription Groups, SMS
        
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
        Update User's Subscription Group Status - Email. Use the endpoint below to update the subscription state of a user on the Braze dashboard. You can access a subscription groups `subscription_group_id` by navigating to it on the Subscription Group page.

\* `email` or `external_id` is required

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `subscription_group_id` | Yes | String | The id of your subscription group, |
| `subscription_state` | Yes | String | Available values are “unsubscribed” (not in subscription group) or “subscribed” (in subscription group) |
| `external_id` | Yes* | String | The external_id of the user |
| `email` | Yes* | String | The email address of the user |
| `phone` | Optional | String in E.164 format | Tags must already exist. |

### Example Successful Response

Response: (status 201)

```json
{
    "message": "success"
}
```
        
        Tags: Subscription Groups, SMS
        
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
        List Available Content Blocks. This endpoint will list existing Content Block information.

### Successful Response Properties
```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "count": "integer",
  "content_blocks": [
    {
      "content_block_id": "string",
      "name": "string",
      "content_type": "html or text",
      "liquid_tag": "string",
      "inclusion_count" : "integer",
      "created_at": "time-in-iso",
      "last_edited": "time-in-iso",
      "tags" : "array of strings"
    }
  ]
}
```

### Possible Errors
- `Modified after time is invalid.`
The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified before time is invalid.`
The date you have provided is not a valid or parsable date. Please reformat this value as a string in ISO 8601 format (`yyyy-mm-ddThh:mm:ss.ffffff`).

- `Modified after time must be earlier than or the same as modified before time.`

- `Content Block number limit is invalid.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit must be greater than 0.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Content Block number limit exceeds maximum of 1000.`
The `limit` parameter must be an integer (positive number) greater than 0.

- `Offset is invalid.`
The `offset` parameter must be an integer (positive number) greater than 0.

- `Offset must be greater than 0.`
The `offset` parameter must be an integer (positive number) greater than 0.
        
        Tags: Templates, Content Blocks
        
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
        See Content Block Information. This endpoint will call information for an existing Content Block.

### Successful Response Properties
```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "content_block_id": "string",
  "name": "string",
  "content": "string",
  "description": "string",
  "content_type": "html or text",
  "tags":  "array of strings",
  "created_at": "time-in-iso",
  "last_edited": "time-in-iso",
  "inclusion_count" : "integer",
  "message": "success"
}
```

### Possible Errors
- `Content Block ID cannot be blank.` - A Content Block has not been listed or is not encapsulated in quotes.

- `Content Block ID is invalid for this App Group.` - This Content Block does not exist or is in a different company account or app group.

- `Content Block has been deleted - content not available.` - This Content Block, though it may have existed earlier, has been deleted.

- `Include Inclusion Data - error` - One of true or false is not provided.
        
        Tags: Templates, Content Blocks
        
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
        Create Content Block. This endpoint will create a Content Block.

### Request Parameters

| Parameter | Required | Data Type | Description |
|---|---|---|---|
| `name` | Yes | String | Must be less than 100 characters. |
| `description` | No | String | The description of the content block. Must be less than 250 characters. |
| `content` | Yes | String | HTML or text content within Content Block.
| `state` | Optional | String | Choose "active" or "draft". Defaults to "active" if not specified. |
| `tags` | No | Array of strings | Tags must already exist. |

### Successful Response Properties

```json
{
  "content_block_id": "newly-generated-block-id",
  "liquid_tag": "generated-block-tag-from-name",
  "created_at": "time-created-in-iso",
  "message": success
}
```

### Possible Errors
- `Content cannot be blank.`

- `Content must be a string.`

- `Content must be smaller than 51200.`
The content in your content block must be less than 50kb total.

- `Unable to parse liquid string.`
The liquid provided is not valid or parsable. Please try again or reach out to support.

- `Content Block cannot be referenced within itself.`

- `Content Block description cannot be blank.`

- `Content Block description must be a string.`

- `Content block description must be shorter than 250`
Your content block description must be less than 250 characters. 

- `Content Block name cannot be blank.`

- `Content Block name must be a shorter than 100.`
Your content block name must be shorter than 100 characters. 

- `Content Block name can only contain alphanumeric characters.`
Content Block names can include any of the following characters: the letters (capitalized or lowercase) `A` through `Z`, the numbers `0` through `9`, dashes `-`, and underscores `_`. It cannot contain non-alphanumeric characters like emojis, `!`, `@`, `~`, `&`, and other "special" characters.

- `Content Block with this name already exists.`

- `Content Block state must be either Active or Draft.`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`
        
        Tags: Templates, Content Blocks
        
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
        Update Content Block. ### Request Parameters
| Parameter | Required | Data Type | Description |
|---|---|---|---|
|`content_block_id`|	Yes |	String |	Your Content Block's API Identifier.|
| `name` | Yes | String | Can only be provided when the content block is in a draft state. Must be less than 100 characters. |
| `description` | No | String | The description of the content block. Must be less than 250 characters. |
| `content` | Yes | String | HTML or text content within Content Block.
| `state` | Optional | "active" or "draft" | Choose "active" or "draft". Defaults to `active` if not specified. Can not set an active content block to draft. |
| `tags` | No | Array of Strings. | Tags must already exist. |

### Successful Response Properties

```json
{
  "content_block_id": "newly-generated-block-id",
  "liquid_tag": "generated-block-tag-from-content_block_name",
  "created_at": "time-created-in-iso",
  "message": "success"
}
```

### Possible Errors
- `Content cannot be blank.`

- `Content must be a string.`

- `Content must be smaller than 50kb.`
The content in your content block must be less than 50kb total.

- `Content contains malformed liquid.`
The liquid provided is not valid or parsable. Please try again or reach out to support.

- `Content Block cannot be referenced within itself.`

- `Content Block description cannot be blank.`

- `Content Block description must be a string.`

- `Content block description must be shorter than 250 characters.`
Your content block description must be less than 250 characters.

- `Content Block name cannot be blank.`

- `Content Block name must be a shorter than 100 characters.`

- `Content Block name can only contain alphanumeric characters.`
Content Block names can include any of the following characters: the letters (capitalized or lowercase) `A` through `Z`, the numbers `0` through `9`, dashes `-`, and underscores `_`. It cannot contain non-alphanumeric characters like emojis, `!`, `@`, `~`, `&`, and other "special" characters.

- `Content Block with this name already exists.`

- `Content Block name cannot be updated for active Content Blocks.`

- `Content Block state must be either Active or Draft.`

- `Active Content Block can not be updated to Draft. Please create a new Content Block.`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`
        
        Tags: Templates, Content Blocks
        
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
        List Available Email Templates. Use this endpoint to get a list of available templates in your Braze account.

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

### Successful Response Properties
```json
{
  "count": number of templates returned
  "templates": [template with the following properties]:
    "email_template_id": (string) your email template's API Identifier,
    "template_name": (string) the name of your email template,
    "created_at": (string, in ISO 8601),
    "updated_at": (string, in ISO 8601),
    "tags": (array of strings) tags appended to the template
}
  ```
        
        Tags: Templates, Email Templates
        
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
        See Email Template Information. Use to get information on your email templates.

Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

### Request Components
- [Template Identifier](https://www.braze.com/docs/api/identifier_types/)
        
        Tags: Templates, Email Templates
        
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
        Create Email Template. Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

Users' email subscription status can be updated and retrieved via Braze using a RESTful API. You can use the API to set up bi-directional sync between Braze and other email systems or your own database. All API requests are made over HTTPS.

Use the endpoints below to create email templates on the Braze dashboard. These templates will be available on the Templates and Media page. The response from this endpoint will include a field for `email_template_id`, which can be used to update the template in subsequent API calls.

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`template_name`|Optional|String|The name of your email template|
|`subject`|Optional|String|The email template subject line|
|`body`|Optional|String|The email template body that may include HTML|
|`plaintext_body`|Optional|String|A plaintext version of the email template body|
|`preheader`|Optional|String|The email preheader used to generate previews in some clients|
|`tags`|Optional|String|Tags must already exist|
|`should_inline_css`|Optional|Boolean|Enables or disables the 'inline_css' feature per template.  If  not provided, Braze will use the default setting for the AppGroup.  One of 'true' or 'false' is expected|

### Possible Errors
- `Template Name is required`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.` - A tag was specified which doesn't exist in this environment.

- `Email must have valid content block names.` - The email contains Content Blocks which do not exist in this environment.

- `"Invalid value for 'should_inline_css'.  One of 'true' or 'false' was expected"` - 'should_inline_css' accepts boolean characters only.  The error likely is being shown as the value is being sent as a 'string'.
        
        Tags: Templates, Email Templates
        
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
        Update Email Template. Use the Template REST APIs to programmatically manage the email templates that you have stored on the Braze dashboard, on the Templates & Media page. Braze provides two endpoints for creating and updating your email templates.

> Use the endpoints below to update email templates on the Braze dashboard. You can access an email template's `email_template_id` by navigating to it on the Templates and Media page. The email template creation API endpoint will also return an `email_template_id` reference.<br><br>All fields other than the `email_template_id` are optional, but you must specify at least one field to update.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Required |String|Your email template's API Identifier.|
|`template_name`|Optional|String|The name of your email template|
|`subject`|Optional|String|The email template subject line|
|`body`|Optional|String|The email template body that may include HTML|
|`plaintext_body`|Optional|String|A plaintext version of the email template body|
|`preheader`|Optional|String|The email preheader used to generate previews in some clients|
|`tags`|Optional|String|Tags must already exist|
|`should_inline_css`|Optional|Boolean|Enables or disables the 'inline_css' feature per template.  If  not provided, Braze will use the default setting for the AppGroup.  One of 'true' or 'false' is expected|

### Request Components
- [Template Identifier](https://www.braze.com/docs/api/identifier_types/)

### Possible Errors
- `Template Name is required`

- `Tags must be an array.`

- `All Tags must be Strings.`

- `Some Tags could not be found.`

- `"Invalid value for 'should_inline_css'.  One of 'true' or 'false' was expected"` - 'should_inline_css' accepts boolean characters only.  The error likely is being shown as the value is being sent as a 'string'.
        
        Tags: Templates, Email Templates
        
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
        External ID Remove. For security purposes, this feature is disabled by default. To enable this feature, please reach out to your Success Manager.

Use this endpoint to remove your users' old deprecated external IDs. This endpoint completely removes the deprecated ID and cannot be undone.

>You can send up to 50 external IDs per request.<br><br>You will need to create a new [API key](https://www.braze.com/docs/api/api_key/) with permissions for this endpoint.<br><br>Only deprecated IDs can be removed; attempting to remove a primary external ID will result in an error.

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Required | Array of strings | External identifiers for the users to remove |

## Response Body
The response will confirm all successful removals, as well as unsuccessful removals with the associated errors. Error messages in the `removal_errors` field will reference the index in the array of the original request.

```
{

  "message" : (string) status message,
  "removed_ids" : (array of successful Remove Operations),
  "removal_errors": (array of any <minor error message>)

}
```

The `message` field will return `success` for any valid request. More specific errors are captured in the `removal_errors` array. The `message` field returns an error in the case of:
- Invalid API key
- Empty `external_ids` array
- `external_ids` array with more than 50 items
- Rate limit hit (>1,000 requests/minute)
        
        Tags: User Data, External ID Migration
        
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
        Create New User Aliases. Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users.

> __Adding a user alias for an existing user__ requires an `external_id` to be included in the new user alias object. If the `external_id` is present in the object but there is no user with that `external_id`, the alias will not be added to any users. If an `external_id` is not present, a user will still be created, but will need to be identified later. You can do this using the "Identifying Users" and the `users/identify` endpoint<br><br>__Creating a new alias-only user__ requires the `external_id` to be omitted from the new user alias object. Once the user is created, use the `/users/track` endpoint to associate the alias-only user with attributes, events and purchases, and the `/users/identify` endpoint to identify the user with an `external_id`.

### Request Parameters

| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `user_aliases` | Yes | Array of new user alias objects | See user alias object |

### Request Components
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)<br><br>
For more information on `alias_name` and `alias_label`, check out our [User Aliases documentation](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases).
        
        Tags: User Data
        
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
        User Delete. This endpoint allows you to delete any user profile by specifying a known user identifier. Up to 50 `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request. Only one of `external_ids`, `user_aliases`, or `braze_ids` can be included in a single request.

> Deleting user profiles CANNOT be undone. It will PERMANENTLY remove users which may cause discrepancies in your data. Learn more about [what happens when you delete a user profile via API](https://braze.com/docs/help/help_articles/api/delete_user/) in our Help documentation.

### Request Parameter
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `external_ids` | Optional | Array of strings | External identifiers for the users to delete |
| `user_aliases` | Optional | Array of user alias oblect | User aliases for the users to delete |
| `braze_ids` | Optional | Array of strings | Braze user identifiers for the users to delete |

### Request Components
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
        
        Tags: User Data
        
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
        Identify Users. Use this endpoint to identify an unidentified (alias-only) user.

> Identifying a user requires an `external_id` to be included in the aliases to identify the object. If the `external_id` is not a valid or known ID, it will simply be added to the aliases user's record, and the user will be considered identified.<br><br>Subsequently, you can associate multiple additional user aliases with a single `external_id`. When these subsequent associations are made, only the push tokens and message history associated with the user alias are retained; any attributes, events or purchases will be "orphaned" and not available on the identified user. One workaround is to export the aliased user's data before identification using the `/users/export/ids` endpoint, then re-associate the attributes, events, and purchases with the identified user.<br><br>You can add up to 50 user aliases per request.

### Parameters
| Parameter | Required | Data Type | Description |
| -----------|----------| --------|------- |
| `aliases_to_identify` | Yes | Array of aliases to identify object | See alias to identify object |

### Request Components
- [Alias to Identify Object](https://www.braze.com/docs/api/objects_filters/aliases_to_identify/)
- [User Alias Object](https://www.braze.com/docs/api/objects_filters/user_alias_object/)
<br><br>

### Aliases to Identify Object Specification
```json
{
  "external_id" : (required, string) see External User ID below,
  // external_ids for users that do not exist will return a non-fatal error. 
  // See Server Responses for details.
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```
        
        Tags: User Data
        
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
        User Track. Use this endpoint to record custom events, purchases, and update user profile attributes.

User Track has a base speed limit of 50,000 requests per minute for all customers. Each request can contain up to 75 events, 75 attribute updates, and 75 purchases. Each component (event, attribute, and purchase arrays), can update up to 75 users each (max of 225 individual users). Each update can also belong to the same user for a max of 225 updates to a single user in a request. Please see our page on API limits for details, and reach out to your Customer Success Manager if you need your limit increased.

Please note that Braze processes the data passed via API at face value and customers should only pass deltas (changing data) to minimize unnecessary data point consumption. To read more, check out our [data point documentation](https://www.braze.com/docs/user_guide/onboarding_with_braze/data_points/#data-points).

### Request Parameters
| Parameter | Required | Data Type | Description |
| --------- | ---------| --------- | ----------- |
| `attributes` | Optional | Array of attributes objects | See user attributes object |
| `events` | Optional | Array of event objects | See events object |
| `purchases` | Optional | Array of purchase objects | See purchase object |

### Request Components
- [User Attributes Object](https://www.braze.com/docs/api/objects_filters/user_attributes_object/)
- [Events Object](https://www.braze.com/docs/api/objects_filters/event_object/)
- [Purchases Object](https://www.braze.com/docs/api/objects_filters/purchase_object/)

When creating alias-only users through this endpoint, you must explicitly set the `_update_existing_only` flag to `false`.<br><br>Updating the subscription status with this endpoint will not only update the user specified by their external_id (e.g User1), but it will also update the subscription status of any users with the same email as that user (User1).

## User Track Responses

Upon using any of the aforementioned API requests you should receive one of the following three general responses:

#### Successful Message

Successful messages will be met with the following response:

```json
{
  "message" : "success",
  "attributes_processed" : (optional, integer), if attributes are included in the request, this will return an integer of the number of external_ids with attributes that were queued to be processed,
  "events_processed" : (optional, integer), if events are included in the request, this will return an integer of the number of events that were queued to be processed,,
  "purchases_processed" : (optional, integer), if purchases are included in the request, this will return an integer of the number of purchases that were queued to be processed,,
}
```

#### Successful Message with Non-Fatal Errors

If your message is successful but has non-fatal errors such as one invalid Event Object out of a long list of events you will receive the following response:

```json
{
  "message" : "success",
  "errors" : [
    {
      <minor error message>
    }
  ]
}
```

#### Message with Fatal Errors

In the case of a success, any data that was not affected by an error in the _errors_ array will still be processed. If your message has a fatal error you will receive the following response:

```json
{
  "message" : <fatal error message>,
  "errors" : [
    {
      <fatal error message>
    }
  ]
}
```

#### Queued Responses

During times of maintenance, Braze might pause the real-time processing of the API. In these situations, the server will return an HTTP Accepted 202 response code and the following body, which indicates that we have received and queued the API call but have not immediately processed it. All scheduled maintenance will be posted to [http://status.braze.com](http://status.braze.com) ahead of time.

```json
{
  "message" : "queued"
}
```

#### Fatal Error Response Codes

The following status codes and associated error messages will be returned if your request encounters a fatal error. Any of these error codes indicate that no data will be processed.

| Error Code | Reason / Cause |
| ---------------------| --------------- |
| `400 Bad Request` | Bad Syntax. |
| `401 Unauthorized` | Unknown or missing REST API Key. |
| `404 Not Found` | Unknown REST API Key (if provided). |
| `429 Rate Limited` | Over rate limit. |
| `5XX` | Internal server error, you should retry with exponential backoff. |

###  Importing Legacy User Data

You may submit data through the Braze API for a user who has not yet used your mobile app in order to generate a user profile. If the user subsequently uses the application all information following their identification via the SDK will be merged with the existing user profile you created via the API call. Any user behavior that is recorded anonymously by the SDK prior to identification will be lost upon merging with the existing API generated user profile.

The segmentation tool will include these users regardless of whether they have engaged with the app. If you want to exclude users uploaded via the User API who have not yet engaged with the app you should add the filter -- `Session Count > 0`.

        
        Tags: User Data
        
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