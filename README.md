# README

Lab files for Azure Developer 204 course.

## Lab_001_hello

26 Jul, Fri

Env var can be read from

`https://hello001.scm.azurewebsites.net/Env`

Command

```
 az webapp up --resource-group lab204 --name hello001 --html --sku Free
```

Output

```
The webapp 'hello001' doesn't exist
Creating AppServicePlan 'liewchooichin_asp_7410' or Updating if already exists
Readonly attribute name will be ignored in class <class 'azure.mgmt.web.v2023_01_01.models._models_py3.AppServicePlan'>
Creating webapp 'hello001' ...
Configuring default logging for the app, if not already enabled
Creating zip with contents of dir /home/liewchooichin/Public/projects/lab_developer_204/lab_001_hello/html-docs-hello-world-master ...
Getting scm site credentials for zip deployment
Starting zip deployment. This operation can take a while to complete ...
Deployment endpoint responded with status code 202
Polling the status of async deployment. Start Time: 2024-07-26 07:31:51.917424+00:00 UTC
You can launch the app at http://hello001.azurewebsites.net
Setting 'az webapp up' default arguments for current directory. Manage defaults with 'az configure --scope local'
--resource-group/-g default: lab204
--sku default: FREE
--plan/-p default: liewchooichin_asp_7410
--location/-l default: eastus
--name/-n default: hello001
{
  "URL": "http://hello001.azurewebsites.net",
  "appserviceplan": "liewchooichin_asp_7410",
  "location": "eastus",
  "name": "hello001",
  "os": "Windows",
  "resourcegroup": "lab204",
  "runtime_version": "-",
  "runtime_version_detected": "-",
  "sku": "FREE",
  "src_path": "//home//liewchooichin//Public//projects//lab_developer_204//lab_001_hello//html-docs-hello-world-master"
}
```

Redeploy the app with the same `az webapp up` command used earlier.
