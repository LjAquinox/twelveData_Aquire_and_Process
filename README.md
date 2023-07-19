# twelveData_Aquire_and_Process
Download financial data with free account from twelve data then process it to trim what I deemed unimportant and order it for AI training afterwards

How to use :

Get your API key from the [Twelve Data website](https://twelvedata.com)

(probably gonna create a file for all infos to be imported later)

Put it in both AquireData and VisualTradingView 
Now change symbols/timerange that you wanna download, there are things to change in all files except VisualTradingView.
Change the directories where you want your files to be downloaded, there are things to change in all files except VisualTradingView.

Now run in order :
1) AquireDataTwelve
2) ProcessDataTwelve
3) FinalProcessingTwelve

If everything was done properly you should get a .npy file for later training.
This is very rudementary but might help someone out there cause I would have liked to find this myself.

A lot of things are easy to make better for QoL and the code is pretty much crap but works.
PS : some part were made with help from GPT but most is made by hand.
