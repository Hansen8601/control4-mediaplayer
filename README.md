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

````
### Available configuration parameters
* **platform** (Required): Name of a platform
* **host** (Required):  IP address of a Control 4 Amp
* **port**(Optional): port of Control4 Amp. Defaults to 8750
* **channel** (Required): Output channel of the AMP. 
* **on_volume** (Optional): Default volume for the amp to turn on to. 5 if omitted

### Work to do
The component doesn't support sources yet. If there's an interest, I'll add it. For my configuration, I only use source 1.

#### My Home Assistant Card
![MyCard](https://github.com/Hansen8601/control4-mediaplayer/blob/f7d66aa66f89b2b0bcf36ea5393bb76a07da0f32/Control4AmpCard.png)
