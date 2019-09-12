# Inverter-Data-Logger add-on for hass.io

Provides [Inverter-DataLogger](https://github.com/XtheOne/Inverter-Data-Logger) for
[Home Assistant](https://www.home-assistant.io/).

The current set-up only allows running a remote server to which your inverter can push its data.
See your inverter documentation on how to add a remote server.

Currently data can only be published to [PVOutput](https://pvoutput.org). Use the
[PVOutput sensor](https://www.home-assistant.io/components/pvoutput/) to show the data on your
dashboard.

## Installation

In Home Assistant open Hass.io. Open the Add-on Store and add the following repository:

```
https://github.com/silvester747/hassio-inverter-data-logger
```

Refresh the Add-on Store and install `Inverter Data Logger`.

## Configuration

### Global options

- `log_level`: Level of logging to enable. Defaults to `info`.

### Inverter settings

Provide the serial number of each inverter and the corresponding PVOutput api key and system id in
the add-on configuration:

```
{
  ...
  "inverters": [
    {
      "serialnumber": "ABCD012342FAKE",
      "pvout_apikey": "1234123412341234234FAKE12431324",
      "pvout_sysid": "1FAKE2"
    }
  ]
}
```

Optionally you can provide for each inverter:
- `pvout_always_upload`: true/false
