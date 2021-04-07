## Interesting Bitcoin brain-wallets rabbit hole

Creating btc addresses using some phrases using wordlists from [SecLists](https://github.com/danielmiessler/SecLists) brought up  some 
fascinating results. This led me to the brain-wallet rabbit hole, albeit a little late.
Brain-wallet is a concept of generating a bitcoin address using a memorized pass phrase.
> PassPhrase -> Private Key & BTC address
>


It is very unsafe since often times than not humans are not good at randomness hence passphrases end up being vulnerable to brute-force attacks.\
An attacker can also generate a lot of brainwallets and their respective private keys with a lot of phrases.They then monitor the blockchain (think a bot run on a VPS that watches the addresses) and if any of the addresses receive any funds, the bot quickly swoops in and transfers the funds.


## Scripts

`sha_btc.py` - Generates btc addresses using a simple phrase list and saves them \
`check_addresses.py` - Checks if saved addresses are used or if they have any balance (highly unlikely)

***Requires:***
>
- Selenium webdriver
- Requests
>
This is interesting since you can find some used addresses(maybe created for research, by actual people to store their fortunes ¯\\_(ツ)_/¯ or for other purposes) using a simple word list.

 ## For more on the topic check out:

-[DEF CON 23 - Ryan Castellucci - Cracking CryptoCurrency Brainwallets](https://www.youtube.com/watch?v=foil0hzl4Pg)\
-[https://en.bitcoin.it/wiki/Brainwallet](https://en.bitcoin.it/wiki/Brainwallet) for more info on brain wallets\
-[Brainflayer](https://github.com/ryancdotorg/brainflayer) which is a Proof-of-Concept brainwallet cracking tool 
