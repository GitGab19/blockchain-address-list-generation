# Blockchain(s) Address List Generation
## Introduction
The focus of this repo is to retrieve the full list of addresses ever appeared into any transactions for some of the most famous blockchains using the secp256k1 curve. 
These Python scripts have been used for an academic research at Politecnico di Torino.
If you want to know more about our paper, you can find it at https://arxiv.org/abs/2206.14107.

Repo is divided into different blockchains we've studied; more specifically, blockchains we've analyzed are: 
- Bitcoin <img align="center" src="https://user-images.githubusercontent.com/62447440/177342647-6a567716-55f6-477b-aac8-6ea6c9917ca1.png" width="25" height="25">
- Ethereum <img align="center" src="https://cryptologos.cc/logos/ethereum-eth-logo.png?v=022" width="25" height="25">
- Dogecoin <img align="center" src="https://cryptologos.cc/logos/dogecoin-doge-logo.png?v=022" width="25" height="25">
- Litecoin <img align="center" src="https://cryptologos.cc/logos/litecoin-ltc-logo.png?v=022" width="25" height="25">
- Dash <img align="center" src="https://cryptologos.cc/logos/dash-dash-logo.png?v=022" width="25" height="25">
- Zcash <img align="center" src="https://cryptologos.cc/logos/zcash-zec-logo.png?v=022" width="25" height="25">
- Bitcoin Cash <img align="center" src="https://cryptologos.cc/logos/bitcoin-cash-bch-logo.png?v=022" width="25" height="25">

Every sub-directory contains a README that explains how the specific Python scripts work.

## Notes
The `requirements.txt` file should list all Python libraries that our scripts
depend on, you have to install them before running any script inside this repo by running:

```
pip install -r requirements.txt
```

### Keys file generation 
In order to create the whole list of private and public keys for the subgroup we've chosen, plus the seven cosets we have chosen to investigate, run the *KeysFileGeneration.py* script. 
<br><br>

## Conclusion
Feel free to open issues, or to contribute to the project!
