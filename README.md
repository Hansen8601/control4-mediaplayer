# Control 4 Matrix Amp [[Home Assistant](https://www.home-assistant.io/) Component]

#### Component Configuration
```yaml
# Example configuration.yaml entry
media_player:  
  - platform: control4-mediaplayer
    name: Great Room
    host: "192.168.1.123"
    channel: 1 


### Available configuration parameters

| Key | Type | Required | Value | Description |
|---|---|---|---|---|
| `platform` | string | true | `control4-mediaplayer` | Name of a platform |
| `host` | string | true | `192.168.0.123` | IP address of a Control 4 Amp |
| `port` | int | false | integer | port. Defaults to 8750 |
| `channel` | int | true | integer | Output channel of the AMP.  |
| `on_volume` | int | false | integer | Default volume for the amp to turn on to. Defaults to 5 if omitted|
