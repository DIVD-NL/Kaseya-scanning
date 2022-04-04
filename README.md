# Kaseya-scanning
Scripts, methods and notes for scanning for Kaseya VSA instanes exposed to the internet.

We used these script in June 2021 when handling the Kaseya VSA case and releasing it as part of our [full disclosure](https://csirt.divd.nl/2022/04/04/Kaseya-VSA-Full-Disclosure/)

This methode uses 4 steps:
* 01_find_open_ports - Finding systems that have port 5721 open using zmap
* 01_from_shodan - Downloading a list of Kaseya VSA servers from Shodan
* 02_get_files - Grabbing files of the systems using zgrab
* 03_process_files - Processing what we've got to get to a full list

