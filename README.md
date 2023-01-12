# Control 4 Matrix Amp [[Home Assistant](https://www.home-assistant.io/) Component]

#### Installation

To install, simply copy the control4-mediaplayer folder into your CUSTOM_COMPONENTS folder and restart Home Assistant.

#### Component Configuration
```yaml
# Example configuration.yaml entry
media_player:  
  - platform: control4-mediaplayer
    name: Great Room
    host: "192.168.1.123"
    channel: 1 
    source_list:
      - "Source 1 name"
      - "Source 2 name"
      - "Source 3 name"
      - "Source 4 name"
````
### Available configuration parameters
* **platform** (Required): Name of a platform
* **host** (Required):  IP address of a Control 4 Amp
* **port**(Optional): port of Control4 Amp. Defaults to 8750
* **channel** (Required): Output channel of the AMP. 
* **on_volume** (Optional): Default volume for the amp to turn on to. 5 if omitted
* **source_list** (Optional): List of source names in source order (e.g., first name = source 1 on amp, second name = source 2 on amp)

#### My Home Assistant Card
![MyCard](https://github.com/Hansen8601/control4-mediaplayer/blob/f7d66aa66f89b2b0bcf36ea5393bb76a07da0f32/Control4AmpCard.png)
