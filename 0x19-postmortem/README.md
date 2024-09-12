

 Postmortem Report: Web Stack Outage

 Issue Summary

- **Duration:**
  - Start Time: January 20, 2024 3:00 PM (UTC)
  - End Time: January 20, 2024 6:00 PM (UTC)
- **Impact:**
  - Service Affected: Website Hosting Platform
  - User Experience: Users experienced intermittent downtime, with slow response times.
  - % of Users Affected: 30%

- **Root Cause:**
  - An unexpected surge in traffic due to a marketing campaign overwhelmed server resources.

## Timeline

- **Issue Detection:**
  - Detected Time: January 20, 2024 3:15 PM (UTC)
  - Detection Method: Monitoring alert triggered for high server load.

- **Actions Taken:**
  - Investigated: Analyzed server logs and identified the spike in incoming requests.
  - Assumptions: Initially assumed a possible DDoS attack.
  - Escalation: Incident escalated to the DevOps and SysAdmin teams for further analysis.

- **Misleading Paths:**
  - Pursued a DDoS investigation, leading to no evidence of malicious activity.

- **Resolution:**
  - Implemented rate limiting on incoming requests and optimized server configurations to handle increased traffic.

## Root Cause and Resolution

- **Root Cause:**
  - The unexpected traffic surge was triggered by a successful marketing campaign, causing an influx of legitimate user requests.

- **Resolution:**
  - Implemented rate limiting to control the number of incoming requests.
  - Optimized server configurations, including adjusting thread pools and increasing server capacity.

## Corrective and Preventative Measures

- **Improvements/Fixes:**
  - Implement automated scaling to handle sudden traffic spikes.
  - Enhance monitoring to proactively detect and respond to unusual traffic patterns.

- **Tasks to Address the Issue:**
  - Deploy a comprehensive caching strategy to alleviate server load.
  - Conduct a review of marketing campaigns to anticipate potential traffic spikes.


