# Universal Mcp Braze MCP Server

An MCP Server for the Universal Mcp Braze API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_braze/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Trello API.

Here is the markdown table summarizing the tools in the `BrazeApp` class:

| Tool | Description |
|------|-------------|
| `query_hard_bounced_emails` | Queries and retrieves a list of email addresses that have hard bounced email messages within a specified time frame. |
| `query_list_of_unsubscribed_email_addresses` | Retrieve emails that have unsubscribed within a specified date range or for a specific email address, supporting pagination and sorting. |
| `change_email_subscription_status` | Updates the email subscription status for one or multiple users, handling both existing and future-associated email addresses. |
| `remove_hard_bounced_emails` | Removes email addresses from the Braze bounce list and the provider's bounce list. |
| `remove_email_addresses_from_spam_list` | Remove email addresses from Braze spam lists and associated provider lists. Validates input and submits removal request. |
| `blacklist_email_addresses` | Blacklist specified email addresses to unsubscribe users from emails and mark them as hard bounced. |
| `campaign_analytics` | Retrieves a daily series of campaign analytics, including message statistics by channel. |
| `campaign_details` | Retrieves detailed information about a campaign specified by its campaign_id. |
| `campaign_list` | Retrieve a paginated list of campaigns with optional filters for archived status, page number, and sorting order. |
| `send_analytics` | Retrieves a daily series of send analytics for a specific campaign and send, including metrics like deliveries, opens, conversions, and revenue. |
| `canvas_data_series_analytics` | Exports time series data for a specified Canvas, allowing customization of the data range and content. |
| `canvas_data_analytics_summary` | Generates a summary of analytics data for a specified Canvas, including rollups of time series metrics, variant statistics, and step performance details. |
| `canvas_details` | Retrieve metadata and structural details about a Braze Canvas using its API identifier, including creation date, steps, variants, and associated channels. |
| `canvas_list` | Retrieves a list of canvases with optional pagination, archival inclusion, and sorting parameters. |
| `custom_events_list` | Fetches a list of custom events recorded for the app, returning them in groups of up to 250, sorted alphabetically. |
| `custom_events_analytics` | Retrieves analytics data for custom events over a specified time period, returning event counts segmented by time unit. |
| `daily_new_users_by_date` | Retrieves a daily series of the total number of new users on each date within a specified period and optionally for a specific app. |
| `daily_active_users_by_date` | Retrieves a daily series of unique active users (DAU) by date for a specific app or app group. |
| `monthly_active_users_for_last30_days` | Retrieves a daily series of unique active users for the last specified days. If no app_id is provided, returns data for all apps in the app group. |
| `kpis_for_daily_app_uninstalls_by_date` | Retrieves a daily series of total app uninstalls as KPIs by date within a specified date range. |
| `news_feed_card_analytics` | Retrieve a time-series of engagement analytics for a specified news feed card. |
| `news_feed_cards_details` | Retrieves detailed information about a news feed card by its identifier. |
| `news_feed_cards_list` | Retrieves a paginated list of News Feed cards including their metadata, supporting filtering and sorting. |
| `segment_list` | Exports a list of segments, each containing its name, Segment API Identifier, and analytics tracking status. |
| `segment_analytics` | Retrieves a daily series of segment size over time for a given segment ID. |
| `segment_details` | Retrieves detailed information about a Braze segment using its API identifier. |
| `app_sessions_by_time` | Retrieves a time series of session counts for a specific app over a designated period. |
| `user_profile_export_by_identifier` | Exports user profile data by specifying one or more user identifiers, returning comprehensive user information including custom attributes, events, devices, and campaign interactions. |
| `user_profile_export_by_segment` | Exports user profiles within a specified segment, returning the export status. |
| `user_profile_export_by_global_control_group` | Exports user profiles by global control group with specified options |
| `get_upcoming_scheduled_campaigns_and_canvases` | Retrieve upcoming scheduled Campaigns and Canvases between the current time and a specified end time in ISO 8601 format. Results include scheduled broadcasts with next occurrence details, limited to Braze-created schedules. |
| `delete_scheduled_messages` | Deletes a scheduled message by its schedule ID if the message has not been sent. |
| `delete_scheduled_api_triggered_campaigns` | Deletes scheduled API-triggered campaigns, canceling messages before sending. |
| `create_scheduled_messages` | Create and schedule messages (e.g., campaigns, canvases) to be sent at a designated time using the API. |
| `schedule_api_triggered_campaigns` | Schedule API-triggered campaigns with templated content, allowing scheduled message delivery up to 90 days in advance. |
| `schedule_api_triggered_canvases` | Schedules API-triggered canvases with customizable parameters. |
| `update_scheduled_messages` | Updates scheduled messages by modifying either the schedule configuration, message content, or both. |
| `update_scheduled_api_triggered_campaigns` | Updates scheduled API triggered campaigns by overwriting existing schedules or adding new ones. |
| `update_scheduled_api_triggered_canvases` | Updates scheduled API-triggered Canvas messages by specifying canvas ID, schedule, and optional schedule ID, with complete schedule overwrite behavior. |
| `create_send_ids_for_message_send_tracking` | Creates send identifiers for message send tracking in Braze, allowing programmatic message sending without campaign creation. |
| `sending_messages_immediately_via_api_only` | Sends immediate messages through Braze API using specified messaging objects and parameters. |
| `sending_campaign_messages_via_api_triggered_delivery` | Initiates API-triggered message delivery for a Braze campaign, allowing control over recipients and message timing. |
| `sending_canvas_messages_via_api_triggered_delivery` | Sends Canvas messages via API triggered delivery, allowing customization of when and to whom messages are sent. |
| `list_user_ssubscription_group_status_email` | Lists the subscription group status for a user based on the provided email or external ID. |
| `list_user_ssubscription_group_email` | Retrieves and lists the subscription groups for a user based on provided criteria like email, external_id, phone number, with options to limit and offset results. |
| `update_user_ssubscription_group_status_email` | Updates a user's subscription group status via email using the Braze dashboard. |
| `list_available_content_blocks` | Retrieve a paginated list of content blocks with optional filters for modification time ranges. |
| `see_content_block_information` | Retrieves information about an existing Content Block, including its details and optional inclusion data. |
| `create_content_block` | Creates a new content block with the provided parameters and returns the newly created block's metadata. |
| `update_content_block` | Updates a content block with provided parameters, ensuring validations for content, state, and metadata. |
| `list_available_email_templates` | Lists available email templates from a Braze account, filtered by optional parameters such as limit, modified after/before times, and offset. |
| `see_email_template_information` | Retrieve details of a specific email template using its API identifier. |
| `create_email_template` | Creates an email template on the Braze dashboard using the Template REST API. |
| `update_email_template` | Updates an email template using the Braze REST APIs. |
| `external_id_remove` | Remove deprecated external IDs for users, returning confirmations and any errors encountered. |
| `create_new_user_aliases` | Create new user aliases for existing users or create new unidentified users by adding their alias information. |
| `user_delete` | Deletes user profiles permanently using Braze identifiers. |
| `identify_users` | Identifies users by associating aliases with an external ID, merging alias data into the identified user's record. |
| `user_track` | Tracks user data including attributes, events, and purchases via Braze API, handling complex data requirements and rate limits. |
## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_braze/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Trello app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 