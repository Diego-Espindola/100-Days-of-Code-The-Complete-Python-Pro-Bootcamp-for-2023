import requests
from info import api_key

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


def main():
	## STEP 1: Use https://www.alphavantage.co
	# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

	url = 'https://www.alphavantage.co/query'
	parameters = {
		"function": "TIME_SERIES_DAILY",
		"symbol": STOCK,
		"apikey": api_key
	}
	r = requests.get(url, params=parameters)
	data = r.json()["Time Series (Daily)"]
	dates = list(data)
	yesterday = dates[1]
	the_day_before_yesterday = dates[2]

	final_value = float(data[yesterday]['4. close'])
	initial_value = float(data[the_day_before_yesterday]['1. open'])
	percentage_increase = ((final_value - initial_value) / initial_value) * 100
	print(percentage_increase)
	if percentage_increase > 5:
		print('Get News')

	## STEP 2: Use https://newsapi.org
	# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

	## STEP 3: Use https://www.twilio.com
	# Send a seperate message with the percentage change and each article's title and description to your phone number.


	#Optional: Format the SMS message like this:
	"""
	TSLA: 🔺2%
	Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
	Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
	or
	"TSLA: 🔻5%
	Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
	Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
	"""


if __name__ == "__main__":
	main()