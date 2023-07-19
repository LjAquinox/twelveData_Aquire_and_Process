# twelveData_Aquire_and_Process
Download financial data with free account from twelve data then process it to trim what I deemed unimportant and order it for AI training afterwards

How to use :

Get your API key from the [Twelve Data website](https://twelvedata.com)

Configure all the settings in Global.py

Select the interval, date range and the symbols you want to download.

Now run in order :
1) AquireDataTwelve
2) ProcessDataTwelve
3) FinalProcessingTwelve

If everything was done properly you should get a .npy file for later training.

This is very rudementary but might help someone out there cause I would have liked to find this myself.

PS : some part were made with help from GPT but most is made by hand.
