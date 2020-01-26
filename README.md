# Docker NZBHydra2

Docker container for [nzbhydra2](https://github.com/theotherp/nzbhydra2), built
with a few things in mind:

* Built to run under k8s, but should run in normal docker fine too

* Run completely as a non-privileged user (not a traditional init, then su down)

* Configure simple options through environment variables (APIKey, Backups, etc)

* Configure more complex options (downloaders, indexers) through ConfigMaps or
  Secrets

## Environmental Variables

| Environment Variable | Config Option |
|----------------------|---------------|
|NZBHYDRA_BACKUP_DAYS  |main.backupEveryXDays|
|NZBHYDRA_APIKEY|main.apiKey|
|NZBHYDRA_BACKUP_KEEP_WEEKS|main.deleteBackupsAfterWeeks|
