# Dash Addresses List <img align="center" src="https://cryptologos.cc/logos/dash-dash-logo.png?v=022" width="40" height="40">
In order to use this Python script, you must have a Dash Full Node (Masternode) running on your local machine.
If you don't already have one, you can find full documentation and setup guides at this link: https://docs.dash.org/en/stable/masternodes/setup.html#install-dash-core
<br><br>
The dash_addresses.py script will generate a single *txt* file (named "dash_addresses_list.txt") containing one address per row. If you don't change anything of the script, it will get addresses from block 0 to 1675747. **In order to get also the latest block (and so the latest addresses) you can simply change the *end_block* variable before running it.**