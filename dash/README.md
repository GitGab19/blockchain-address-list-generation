# Dash Addresses List
In order to use this Python script, you must have a Dash full node (Masternode) running on your local machine.
If you don't already have one, you can find full documentation and setup guides at this link: https://docs.dash.org/en/stable/masternodes/setup.html#install-dash-core
<br>
The dash_addresses.py script will generate a single *txt* file (named "zcash_addresses.txt") containing one address per row. If you don't change anything of the script, it will get addresses from block 0 to 1675747. **In order to get also the latest block (and so the latest addresses) you can simply change the *end_block* variable before running it.**