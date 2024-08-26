This is Wavelet EQ Data equivalent of the official VSX plugin for Steven Slate Audio VSX. It's used to provide Flat EQ correction also on Android device.

I only generated the data for my settings below.

![my settings]("img/my settings.png")

You can generate the data for your settings with the following steps:
1. Use Bertom EQ Curve Analyzer 2 with VSX to generate and export the EQ measurement data named as `eq_data.csv`
 
![EQ Curve]("img/eq curve.png")

2. Run python script `convert-eqcurveanalyzer2autoeq.py` to convert to AutoEQ data named as `autoeq_format.csv`
3. Run python script `convert-autoeq2wavelet.py` to convert to Wavelet EQ Data named as `wavelet_data.txt`. This is the final data you want.

If you generated your data, welcome to open a new issue or pull request to share here!
