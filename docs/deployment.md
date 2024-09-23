# Deployment

Once your app is ready, you can deploy it to [Azure Web App Service](https://azure.microsoft.com/en-us/products/app-service/web).
`st-undp` makes it easy to do so in a few simple steps.

First, use the CLI to generate a startup script:

```shell
python -m st_undp configure --settings deployment
```

This will add a `startup.sh` at the root of your project. The script
contains settings required to run a Streamlit app on Azure.

???+ note

    `startup.sh` contains a call to modify `.streamlit/config.toml` internally.
    If you don't have any custom configuration settings in that file or 
    you don't have that file to start with, you should not worry about this detail.
    But if you do, bear in mind that you will need to make sure that the file is 
    included in the deployment process. Your theme settings will be overwritten
    in the deployed app. And so will be some server and browser settings required
    to run the app on Azure.

Secondly, create a web app on Azure portal. And add `startup.sh` as a "Startup Command" under 
"Stack settings" in "Settings" -> "Configuration" for your Web App on Azure.

Finally, deploy the app to Azure using your preferred method, e.g.,
GitHub Actions, Azure Pipelines or manually via ZIP upload.
