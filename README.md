# Docker NZBHydra2

Docker container for [nzbhydra2](https://github.com/theotherp/nzbhydra2), built
with a few things in mind:

* Built to run under k8s, but should run in normal docker fine too

* Run completely as a non-privileged user (not a traditional init, then su down)

* Configure simple options through environment variables (APIKey, Backups, etc)

* Run a single process, which can easily be health checked and restarted if needed

* Configure more complex options (downloaders, indexers) through ConfigMaps or
  Secrets **Coming Soon**

## Environmental Variables

The following variables can be used to optionally setup configuration options
in the `nzbhydra.yml` file

| Environment Variable | Config Option |
|----------------------|---------------|
|NZBHYDRA_BACKUP_DAYS  |main.backupEveryXDays|
|NZBHYDRA_APIKEY|main.apiKey|
|NZBHYDRA_BACKUP_KEEP_WEEKS|main.deleteBackupsAfterWeeks|

The following config options are set to make things more docker-y

| Config Option | Value |
|---------------|-------|
|main.updateCheckEnabled| False |
|main.showUpdateBannerOnDocker| False |
