# Zcash Addresses list <img align="center" src="https://cryptologos.cc/logos/zcash-zec-logo.png?v=022" width="40" height="40">
In order to use this Python script, you must have a Zcash Full Node running on your local machine.
If you don't already have one, you can find full documentation and setup guides at this link: https://zcash.readthedocs.io/en/latest/rtd_pages/zcashd.html
<br><br>
The zcash_addresses.py script will generate a single *txt* file (named "zcash_addresses.txt") containing one address per row. If you don't change anything of the script, it will get addresses from block 0 to 1677816. **In order to get also the latest block (and so the latest addresses) you can simply change the *end_block* variable before running it.**