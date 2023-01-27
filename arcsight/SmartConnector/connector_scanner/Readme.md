 - provided as is - might harm your Smartconnectors - don't blame me. Think before you act.

 - connector_scanner is used to scan for default username/password usage on ArcSight Smart Connector's remote management port
 - The script takes "config.csv" as a an input list for hosts to scan
 - Provide username and password, you know where to find it... i wont tell you.
 - change port_start and port_end, if you use different ports.
 - https_timeout parameterizes the connection timeout for the request, if you have a big list, this might influence the runtime of the script, however
    don't put it too low, as your network might not react fast enough, and you would miss the host/port

- improvements welcome
  
