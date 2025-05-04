# Braze MCP Server

An MCP Server for the Braze API.

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Braze API.


| Tool | Description |
|------|-------------|
| `query_hard_bounced_emails` | Queries and retrieves a list of email addresses that have “hard bounced” email messages within a specified time frame. |
| `query_list_of_unsubscribed_email_addresses` | Retrieve emails that have unsubscribed within a specified date range or for a specific email address, supporting pagination and sorting. |
| `change_email_subscription_status` | Updates the email subscription status for one or multiple users, handling both existing and future-associated email addresses. |
| `remove_hard_bounced_emails` | Removes email addresses from the Braze bounce list and the provider's bounce list. |
| `remove_email_addresses_from_spam_list` | Remove email addresses from Braze spam lists and associated provider lists. Validates input and submits removal request. |
| `blacklist_email_addresses` | Blacklist specified email addresses to unsubscribe users from email and mark them as hard bounced. |
| `campaign_analytics` | Retrieves a daily series of campaign analytics, including message statistics by channel. |
| `campaign_details` | Retrieves relevant information on a specified campaign, which can be identified by the `campaign_id`. |
| `campaign_list` | Retrieve a paginated list of campaigns with optional filters for archived status, page number, and sorting order. |
| `send_analytics` | Retrieves a daily series of various stats for a tracked `send_id`. |
| `canvas_data_series_analytics` | Exports time series data for a specified Canvas, allowing customization of the data range and content. |
| `canvas_data_analytics_summary` | Generates a summary of analytics data for a specified Canvas, including rollups of time series metrics, variant statistics, and step performance details. |
| `canvas_details` | This endpoint allows you to export metadata about a Canvas, such as its name, when it was created, its current status, and more. |
| `canvas_list` | Retrieves a list of Canvases, including the name, Canvas API Identifier and associated Tags. |
| `custom_events_list` | Fetches a list of custom events that have been recorded for your app. |
| `custom_events_analytics` | Retrieves a series of the number of occurrences of a custom event in your app over a designated time period. |
| `daily_new_users_by_date` | Retrieves a daily series of the total number of new users on each date within a specified period and optionally for a specific app. |
| `daily_active_users_by_date` | Retrieves a daily series of the total number of unique active users on each date. |
| `monthly_active_users_for_last30_days` | Retrieves a daily series of the total number of unique active users over a 30-day rolling window. |
| `kpis_for_daily_app_uninstalls_by_date` | Retrieves a daily series of the total number of uninstalls on each date. |
| `news_feed_card_analytics` | Retrieves a daily series of engagement stats for a card over time. |
| `news_feed_cards_details` | This endpoint allows you to retrieve relevant information on the card, which can be identified by the `card_id`. |
| `news_feed_cards_list` | This endpoint allows you to export a list of News Feed cards, each of which will include its name and Card API Identifier. |
| `segment_list` | Exports a list of segments, each of which will include its name, Segment API Identifier, and whether it has analytics tracking enabled. |
| `segment_analytics` | Retrieves a daily series of the size of a segment over time for a segment. |
| `segment_details` | This endpoint allows you to retrieve relevant information on the segment, which can be identified by the `segment_id`. |
| `app_sessions_by_time` | This endpoint allows you to retrieve a series of the number of sessions for your app over a designated time period. |
| `user_profile_export_by_identifier` | This endpoint allows you to export data from any user profile by specifying a form of user identifier. |
| `user_profile_export_by_segment` | This endpoint allows you to export all the users within a segment. |
| `user_profile_export_by_global_control_group` | User Profile Export by Global Control Group |
| `get_upcoming_scheduled_campaigns_and_canvases` | You can view a JSON list of upcoming and scheduled Campaigns and Canvases using the following information and parameters. |
| `delete_scheduled_messages` | The delete scheduled messages endpoint allows you to cancel a message that you previously scheduled _before_ it has been sent. |
| `delete_scheduled_api_triggered_campaigns` | The delete schedule endpoint allows you to cancel a message that you previously scheduled API Triggered Campaigns before it has been sent. |
| `create_scheduled_messages` | Use this endpoint to send messages directly from the API. |
| `schedule_api_triggered_campaigns` | Use this endpoint to trigger API Triggered Campaigns, which are created on the Dashboard and initiated via the API. |
| `schedule_api_triggered_canvases` | Use this endpoint to trigger API Triggered Canvases, which are created on the Dashboard and initiated via the API. |
| `update_scheduled_messages` | The messages update schedule endpoint accepts updates to either the `schedule` or `messages` parameter or both. |
| `update_scheduled_api_triggered_campaigns` | Use this endpoint to update scheduled API Triggered Campaigns, which are created on the Dashboard and initiated via the API. |
| `update_scheduled_api_triggered_canvases` | Use this endpoint to update scheduled API Triggered Canvases, which are created on the Dashboard and initiated via the API. |
| `create_send_ids_for_message_send_tracking` | Braze’s Send Identifier adds the ability to send messages and track message performance entirely programmatically, without campaign creation for each send. |
| `sending_messages_immediately_via_api_only` | This endpoint allows you send your messages using our API. |
| `sending_campaign_messages_via_api_triggered_delivery` | API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API. |
| `sending_canvas_messages_via_api_triggered_delivery` | API Triggered Delivery allows you to house message content inside of the Braze dashboard while dictating when a message is sent, and to whom via your API. |
| `list_user_ssubscription_group_status_email` | Use the endpoint below to get the subscription state of a user in a subscription group. |
| `list_user_ssubscription_group_email` | Use the endpoint below to list and get the subscription groups of a certain user. |
| `update_user_ssubscription_group_status_email` | Use the endpoint below to update the subscription state of a user on the Braze dashboard. |
| `list_available_content_blocks` | This endpoint will list existing Content Block information. |
| `see_content_block_information` | This endpoint will call information for an existing Content Block. |
| `create_content_block` | This endpoint will create a Content Block. |
| `update_content_block` | ### Request Parameters |
| `list_available_email_templates` | Use this endpoint to get a list of available templates in your Braze account. |
| `see_email_template_information` | Use to get information on your email templates. |
| `create_email_template` | Use the endpoints below to create email templates on the Braze dashboard. |
| `update_email_template` | Use the endpoints below to update email templates on the Braze dashboard. |
| `external_id_remove` | For security purposes, this feature is disabled by default. To enable this feature, please reach out to your Success Manager. |
| `create_new_user_aliases` | Use this endpoint to add new user aliases for existing identified users, or to create new unidentified users. |
| `user_delete` | This endpoint allows you to delete any user profile by specifying a known user identifier. |
| `identify_users` | Use this endpoint to identify an unidentified (alias-only) user. |
| `user_track` | Use this endpoint to record custom events, purchases, and update user profile attributes. |
