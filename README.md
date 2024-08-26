This is Wavelet EQ Data equivalence of the official VSX plugin for Steven Slate Audio VSX. It's used to provide a flat EQ correction also on Android devices.

I only generated the data for my settings below.

![my settings](img/my%20settings.png)

You can generate the data for your settings with the following steps. The scripts are in the `scripts` folder.
1. Use Bertom EQ Curve Analyzer 2 with VSX to generate and export the EQ measurement data named as `eq_data.csv`. Set the `calib.` so the overall curve is near 0 db.
 
![EQ Curve](img/eq%20curve.png)

2. Run the python script `convert-eqcurveanalyzer2autoeq.py` to convert to AutoEQ data named as `autoeq_format.csv`.
3. Run the python script `convert-autoeq2wavelet.py` to convert to Wavelet EQ Data named as `wavelet_data.txt`. This is the final data you want.

If you generated your data, welcome to open a new issue or pull request to share here!
