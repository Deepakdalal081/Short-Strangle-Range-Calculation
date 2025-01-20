**Stock Price Range Analysis**<br/>
##
This Python script analyzes the historical price ranges of selected stocks using Yahoo Finance data.<br/>
It calculates the 65% and 95% confidence intervals for future stock prices based on historical daily returns.<br/>
##

**Features**<br/>

1. Fetches historical stock data for the last ~27 years (10,000 days).<br/>

2. Computes monthly returns and statistical metrics (mean and standard deviation).<br/>

3. Calculates price ranges for 65% and 95% confidence intervals.<br/>

4. Outputs results for multiple stocks in a clean, readable format.<br/>


**Example Output**<br/>
65% chance stock will remain in this range:<br/>
ABB.NS will remain in 1543.27 -- 1678.42<br/>
<br/>
95% chance stock will remain in this range:<br/>
ABB.NS will remain in 1410.12 -- 1811.57<br/>


**Short Strangle Strategy**.<br/> 
This involves selling both a call and a put option at different strike prices within the 65% or 95% confidence intervals. <br/>
The specific range and risk tolerance depend on the individual trader's preferences and market outlook. <br/>

**Author**<br/>

Deepak Dalal<br/>

Feel free to suggest improvements or contribute to this project!<br/>
