---
title: Deploy with Jamf Pro
description: Use Jamf Pro to deploy Docker Desktop for Mac
source_repo: docker/docs
source_ref: main
source_commit: 083f66104
source_path: manuals/enterprise/enterprise-deployment/use-jamf-pro.md
technology: docker
version: main
license: Apache-2.0
retrieved_at: '2026-09-15'
section: enterprise
order: 6230
---

{{< summary-bar feature_name="Jamf Pro" >}}

Learn how to deploy Docker Desktop for Mac using Jamf Pro, including uploading the installer and creating a deployment policy.

First, upload the package:

1. From the Jamf Pro console, navigate to **Computers** > **Management Settings** > **Computer Management** > **Packages**.
2. Select **New** to add a new package.
3. Upload the `Docker.pkg` file.

Next, create a policy for deployment:

1. Navigate to **Computers** > **Policies**.
2. Select **New** to create a new policy.
3. Enter a name for the policy, for example "Deploy Docker Desktop".
4. Under the **Packages** tab, add the Docker package you uploaded.
5. Configure the scope to target the devices or device groups on which you want to install Docker.
6. Save the policy and deploy.

For more information, see [Jamf Pro's official documentation](https://learn.jamf.com/en-US/bundle/jamf-pro-documentation-current/page/Policies.html). 

## Additional resources

- Learn how to [enforce sign-in](../security/enforce-sign-in/index.md) for your users.
