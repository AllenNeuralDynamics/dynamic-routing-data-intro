# Dynamic Routing data intro

This capsule is to demonstrate data access for Dynamic Routing sessions.
It uses the `npc_sessions` python package to get data in NWB format.

## clone capsule

First off, open up Codeocean in a new tab [here](https://codeocean.allenneuraldynamics.org/).

- hit the `+` icon (top left) and select "New Capsule" > "Clone from Git" and paste the URL for this repo: `https://github.com/AllenNeuralDynamics/dynamic-routing-data-intro`
- the capsule should open at this readme
  
## environment

The environment should be set up and ready to go, but if you need to update it at some point, the only required package is `npc_sessions` (latest version).
  
Note: since `npc_sessions` has a lot of loosely specified dependencies, solving the environment for the capsule can take a while (pip tries to find a version of each dependency that's compatible with all the other dependencies - for certain packages this can lead to many minutues of waiting as pip downloads every published version of the package to test it). To speed this up, we publish a `requirements.txt` with pinned dependencies from a solved environment (for the latest version of Ubuntu x64) [here](https://github.com/AllenInstitute/npc_sessions/blob/main/requirements.txt). Codeocean allows uploading or pasting the contents of this file in `environment/pip3` - just make sure to add the latest version of `npc_sessions` too.

## credentials

Before we can start, we need to ensure 2 sets of credentials are available in the capsule:
1. AWS (to find and read files on S3)
2. Codeocean (to find processed data in "data assets" via the Codeocean API)

- right click on `Account` (bottom left, person icon) and open in a new window, so we can switch back and forth between these instructions
- click `User Secrets` - these are secrets than can be made available as environment variables in Codeocean capsules
- check that there's a secret with the type `AWS Cloud Credentials`: this should have been automatically added to your account, **if it's not there get in touch with Ben**

- next go to `Access Tokens` and click `Generate new token`
- enter the Token Name `Codeocean API (read)` and tick `read` on capsules and datasets
- a token will be generated: click copy (storing it in a password manager, if you use one), then head back to `User Secrets` where we'll paste it into a new secret via `Add secret` > `API credentials`
- description: `Codeocean API (read)`, API key: `CODE_OCEAN_API_KEY`, API secret: paste the copied secret from before (should begin `cop_...`)

- now, refresh the browser page with the capsule so that we can use the newly-added secrets

- in the capsule's file browser (left), click on `environment` under `Core Files` (cog icon) to open the `Environment` tab

- scroll down to the bottom of the page - we'll use `Add secret to capsule` to make secrets available as environment variables within the capsule

- first choose `AWS Cloud Credentials` and select the available option in the dropdown that appears (says `Select AWS Cloud Credentials`)

- `Add secret to capsule` should be blue again, click it and this time choose `API credentials` and, in the dropdown, select `[API credentials] Codeocean API (read)`

Next we'll open up a notebook that will test the credentials.

## launch notebook

On the right of the capsule screen, in the group of icons, hit the "lab" icon to launch JupyterLab - this readme will be replaced by loading screens, but once the environment is built, JupyterLab opens a file browser on the left of the screen - we'll continue in `DynamicRouting.ipynb`. See you there!
