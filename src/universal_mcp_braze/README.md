# Braze MCP Server

An MCP Server for the Braze API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Braze API.


| Tool | Description |
|------|-------------|
| `query_hard_bounced_emails` | Retrieves a list of permanently undelivered email addresses with optional date range, pagination, and email filtering. |
| `query_list_of_unsubscribed_email_addresses` | Retrieves a list of unsubscribed email addresses within a specified date range, optionally filtered by email, with pagination and sorting support. |
| `change_email_subscription_status` | Posts a request to retrieve the current delivery status of a specified email. |
| `remove_hard_bounced_emails` | Removes email addresses from a bounce list using the Braze API. |
| `remove_email_addresses_from_spam_list` | Removes specified email addresses from both the Braze spam list and the associated email provider's spam list using a POST request. |
| `blacklist_email_addresses` | Unsubscribes a user from email and marks them as hard bounced. |
| `campaign_analytics` | Retrieves a data series for a campaign, providing analytics such as message send, open, and click metrics over a specified time period defined by the campaign ID, series length, and ending date. |
| `campaign_details` | Retrieves detailed information for a specified campaign using its unique identifier (campaign_id). |
| `campaign_list` | Retrieves a paginated list of campaigns with optional filtering parameters for archived status, sorting, and edit time range. |
| `send_analytics` | Retrieves a data series for campaign sends with optional filtering by campaign ID, send ID, length, and ending timestamp. |
| `canvas_data_series_analytics` | Exports time series data for a Canvas, allowing users to retrieve analytics based on parameters such as canvas ID, time range, and optional breakdowns by variant, step, or deleted step data. |
| `canvas_data_analytics_summary` | Retrieves summarized analytics data for a specific Canvas, including time-based metrics and optional breakdowns by variants or steps, based on parameters like time range and data granularity. |
| `canvas_details` | Retrieves and returns detailed information about a Canvas resource identified by the provided `canvas_id`. |
| `canvas_list` | Retrieves a paginated list of Canvases including names, API identifiers, and associated tags, sorted in groups and filterable by parameters like archival status and edit time. |
| `custom_events_list` | Retrieves a list of events using the "GET" method at the "/events/list" endpoint, optionally paginating results using the "page" query parameter. |
| `custom_events_analytics` | Retrieves a data series for an event using the specified parameters and returns the relevant data. |
| `daily_new_users_by_date` | Retrieves a data series for new users using the "GET" method, filtered by the specified length, ending date, and app ID. |
| `daily_active_users_by_date` | Retrieves a data series for daily active users (DAU) based on specified parameters such as length, ending date, and application ID. |
| `monthly_active_users_for_last30_days` | Retrieves a data series for monthly active users (MAU) using the "GET" method at "/kpi/mau/data_series," allowing customization with parameters for series length, end date, and application ID. |
| `kpis_for_daily_app_uninstalls_by_date` | Retrieves a series of KPI uninstall data over a specified period with configurable length, end date, and app identifier. |
| `news_feed_card_analytics` | Retrieves a list of data series for a specific card, allowing users to filter by card ID, length, unit, and ending date. |
| `news_feed_cards_details` | Retrieves detailed information about a specific card based on the provided `card_id` using the "GET" method. |
| `news_feed_cards_list` | Retrieves a paginated list of feed items with optional filtering for archived items and sorting direction. |
| `segment_list` | Retrieves a list of segments, each with details such as name, API identifier, and analytics tracking status, allowing optional pagination and sorting by creation time. |
| `segment_analytics` | Retrieves a data series for a specified segment based on the segment ID, data length, and ending date using the API endpoint at "/segments/data_series" via the GET method. |
| `segment_details` | Retrieves detailed information about a specific segment, identified by its ID, using the GET method at the "/segments/details" endpoint. |
| `app_sessions_by_time` | Retrieves data series for sessions using the specified length, unit, ending time, application ID, and segment ID through a GET request to the "/sessions/data_series" endpoint. |
| `user_profile_export_by_identifier` | Exports user IDs using a POST request and returns the result upon successful completion. |
| `user_profile_export_by_segment` | Initiates a user segment export process and returns the export status upon successful creation. |
| `user_profile_export_by_global_control_group` | Exports the global control group data for users using the API endpoint at path "/users/export/global_control_group" via the POST method. |
| `get_upcoming_scheduled_campaigns_and_canvases` | Retrieves a list of scheduled broadcasts between the current time and a specified end time using the GET method. |
| `delete_scheduled_messages` | Deletes a scheduled message and returns a status message upon success. |
| `delete_scheduled_api_triggered_campaigns` | Deletes scheduled triggers for campaigns using a POST request to the "/campaigns/trigger/schedule/delete" endpoint. |
| `schedule_api_triggered_campaigns` | Creates and schedules a triggered campaign action, returning a success status upon completion. |
| `schedule_api_triggered_canvases` | Schedules API-triggered Canvas messages for delivery based on specified actions. |
| `update_scheduled_messages` | Updates a scheduled message and returns a success status upon completion. |
| `update_scheduled_api_triggered_campaigns` | Updates the schedule of a campaign trigger using the POST method and returns a status message. |
| `update_scheduled_api_triggered_canvases` | Updates a scheduled Canvas trigger's configuration using a POST request and returns a success status upon completion. |
| `create_send_ids_for_message_send_tracking` | Creates a new send operation with the specified ID and returns a success status upon completion. |
| `sending_campaign_messages_via_api_triggered_delivery` | Triggers a campaign send operation using a POST request to the "/campaigns/trigger/send" endpoint and returns a successful response upon completion. |
| `sending_canvas_messages_via_api_triggered_delivery` | Sends Canvas messages via API-triggered delivery, allowing users to store message content in the dashboard while specifying recipients and timing through the API. |
| `list_user_ssubscription_group_status_email` | Retrieves the subscription status for a user specified by their external_id, email, or phone number within a subscription group. |
| `list_user_ssubscription_group_email` | Retrieves the subscription status of users by querying identifiers such as external_id, email, or phone, with pagination support via limit and offset parameters. |
| `update_user_ssubscription_group_status_email` | Updates subscription statuses for up to 50 users in a subscription group via batch processing. |
| `list_available_content_blocks` | Retrieves a list of content blocks using the GET method at the "/content_blocks/list" path, allowing filtering by modification dates with parameters like "modified_after" and "modified_before", and pagination control via "limit" and "offset". |
| `see_content_block_information` | Retrieves information about a specified Content Block using its identifier, optionally including data on where it is used in campaigns or Canvases. |
| `create_content_block` | Creates a new content block using the provided data and returns a success response upon completion. |
| `update_content_block` | Updates content blocks using a POST request and returns a success status upon completion. |
| `list_available_email_templates` | Retrieves a list of available email templates with optional filtering by modification time and pagination parameters. |
| `see_email_template_information` | Retrieves information about a specific email template using the "GET" method at the "/templates/email/info" path, based on the provided `email_template_id` query parameter. |
| `create_email_template` | Creates a new email template and returns a confirmation upon successful creation. |
| `update_email_template` | Updates an email template and returns a success status upon completion using a POST request. |
| `external_id_remove` | Removes external user identifiers and returns a successful status response upon completion. |
| `create_new_user_aliases` | Creates a new user alias using the API and returns a status message. |
| `user_delete` | Deletes a user using the API and returns a status message. |
| `identify_users` | Identifies a user and returns a success status upon verification. |
| `user_track` | Tracks user activity by sending data to the API endpoint at "/users/track" using the POST method. |
