---
layout: post
title:  "A primer on kernel density estimation"
date:   2017-11-25 12:00:00 -0400
categories: technical
---

Imagine that you're teaching a class, and after giving an exam, you have a set of data containing the marks for each of your students. If you wanted to get a sense of the distribution of marks, what sort of analysis would you do? You might calculate the mean and standard deviation, but those offer a very limited view of the data. If you wanted to visualize the entire distribution of grades, what sort of plot would you use?

Up until about a year ago (i.e., mid-way through my Master's degree), my answer would have been to use a histogram. I would count up how many students had a grade between 70-80%, 80-90%, 90-100%, and so on, and plot the count of each of those bins.

![Histogram of marks]({{site.baseurl}}/images/kde_primer/marks_hist.svg)

It's not that histograms are particularly good, but I was not aware of better alternatives at the time. The most obvious frustration with histograms is that they only give a very coarse and "pixelated" view of the data. This is an acceptable limitation when the data has a smooth and simple shape. But if the data has some detailed structure with multiple modes/peaks, it is quite hard to capture in a histogram.

Imagine a distribution with three peaks - a dataset where points tend to be close to one of three values of \\( x \\):

![Probability density function of trimodal distribution with rugplot]({{site.baseurl}}/images/kde_primer/trimodal_dist_ticks.svg)

Using a random number generator obeying that distribution, I generated a dataset with 100 points, shown as ticks in the above plot. To test the capabilities of the histogram, I created several plots based on this dataset. In principle, plotting a histogram of that data should result in an approximate visualization of the underlying distribution; if the histogram is very close to the underlying distribution, then it is a good approximation.

When plotting a histogram of the dataset, it's necessary to choose several parameters, starting with the width of the bins. Narrower bins give a more detailed picture of the data, but result in spiky artifacts if the points fall in uneven clusters.

![Histogram of trimodal distribution with varying bin width]({{site.baseurl}}/images/kde_primer/trimodal_hist_nbins.svg)

The other main parameter is the starting point for the bins; this is a parameter that is often automatically chosen either by looking at the smallest datapoint, or by some natural boundary in the data, such as 0% for the aforementioned distribution of marks. As it turns out, this choice of starting point is arbitrary in the sense that it has no particular meaning, but it can exert a frighteningly large influence on the visualization.

The bins can be shifted so that they all start at slightly smaller or larger values, but this causes the qualitative shape of the peaks to jump around chaotically.

![Histogram of trimodal distribution with varying bin shift]({{site.baseurl}}/images/kde_primer/trimodal_hist_shift.svg)

As an analyst, you probably want to answer some basic questions, like:

1. How many peaks are there?
2. Where are the peaks located?
3. How broad are the peaks? How steeply or gradually do they fall away?

With these artifacts, it becomes very difficult to get precise answers to these questions; what is the "real" shape of the distribution?

As mentioned above, histograms give an approximate visualization of the underlying distribution that the data came from. They are a kind of *estimator*, in the same sense that the sample mean is an estimator of the population mean. I want to demonstrate one alternative estimator for the distribution: a plot called a [kernel density estimate (KDE)](https://en.wikipedia.org/wiki/Kernel_density_estimation), also referred to simply as a *density plot*.

Epistemic status: Before going any further, I want to emphasize that I do not have a comprehensive background in statistics. I propose that if you have limited formal knowledge of the field, KDEs are a great alternative to histograms, and offer this article as a brief introduction. If you intend to use KDEs for a real application or analysis, I urge you to follow up with a commensurate amount of study and discussion with experts.

In a histogram, a datapoint can only contribute to one bin, which resulted in the artifacts shown above. KDEs get around this problem by smearing out the contribution of a datapoint over a wide area, according to a function called a kernel. Many different functions can be used for kernels, but typical kernels, such as the Gaussian kernel, blur the datapoint so that its influence is highest in its immediate vicinity, and trails off to nothing further away. Actually, KDEs don't have a notion of bins at all - they are continuous functions which can be computed at any point. Together, these properties eliminate artifacts relating to where bins start and stop. The resulting plot is a smoothed out estimate of the distribution. The y-axis is normalized so that the values represent *probability density* and not a raw count of the datapoints.

![Kernel density estimate of trimodal distribution, alongside true distribution]({{site.baseurl}}/images/kde_primer/trimodal_prob_dist_kde.svg)

As can be seen, the KDE comes quite close to approximating the underlying distribution, and gives precise answers to the previously-mentioned basic analytical questions.

To understand how a KDE is constructed, it helps to look at a typical kernel function. Consider the Epanechnikov (or parabolic) kernel:

$$
K_{x_0}(x) =
\begin{cases}
\frac{3}{4} (1 - (x - x_0)^2) & \text{if } |x - x_0| \le 1 \\
0 & \text{otherwise}
\end{cases}
$$

![Epanechnikov kernel, centred at x=0]({{site.baseurl}}/images/kde_primer/kernel.svg)

For a datapoint located at \\(x_0\\), this kernel is its contribution to the plot. To fully plot the KDE, you can imagine just making a kernel centered around each datapoint, adding them all together, and dividing by the number of points to normalize the amount of area under the curve.

$$ \rho(x) = \sum_{i=0}^n \frac{K_{x_i}(x)}{n} $$

For example, consider this tiny dataset with three datapoints: \\( \mathbf{X} = (-0.95, 0.75, 1.0) \\).

Below, the kernels are plotted in orange, and the resulting KDE is plotted in black.

![Construction of a KDE from one kernel per datapoint]({{site.baseurl}}/images/kde_primer/kde_construction_inverted.svg)

You can also conceptualize the KDE as a convolution, where the kernel is convolved with a handful of [Dirac delta functions](https://en.wikipedia.org/wiki/Dirac_delta_function) representing the datapoints. From this perspective, one kernel function slides over the data, and the contributions from each point are summed.

{% include html5Video.html src="/images/kde_primer/kde_construction_convolution.webm" %}

Now, of course, your dataset should have more than 3 points in it for a KDE to be meaningful. But hopefully these perspectives make the workings of KDEs crystal clear.

Other choices of kernel may be seen [here](https://en.wikipedia.org/wiki/Kernel_(statistics)#Kernel_functions_in_common_use), and all should give acceptable performance, but when in doubt, the Epanechnikov and Gaussian kernels are both good choices.

Kernels still contain a parameter for bandwidth, which, like bin width, controls the amount of smoothing. Still, this parameter is relatively well-behaved. Applied to the previous data with a range of values, the resulting plots show increasing levels of detail. For very narrow bandwidths, there are still artifact-y peaks, but they smoothly emerge and stay relatively stationary, rather than jumping around. And as with histograms, there are a few automated methods for choosing a bandwidth - they offer no guarantees, but provide a good starting point.

![KDEs with varying bandwidths]({{site.baseurl}}/images/kde_primer/marks_kde_bws.svg)

I described KDEs as an estimator of the underlying distribution, which is to say that they are an approximation with some amount of uncertainty. For estimators like the sample mean (which approximates the population mean), you can precisely show the uncertainty by making a confidence interval around the estimate. In the case of the mean, confidence intervals are constructed based on a model of the distribution the data comes from (e.g., the normal distribution, or the chi-squared distribution). KDEs don't have an underlying model, so there's no easy formula for making a confidence interval of the distribution, but by using bootstrapping, it's possible to empirically estimate one. Now, this is an estimate of an estimate, which can be a little dicey, but just like KDEs themselves, it's a low-effort way to get some easily-interpreted information about your data.

It works by generating a large number of dummy samples (10,000 as a rule of thumb), hopefully from a distribution similar to the one that resulted in the original data, and computing a KDE for each of them. To generate each dummy sample, randomly sample \\(n\\) points from the original dataset, with replacement (so that even if \\(x=99\\) only appears once in the original data, it may appear multiple times in the dummy sample). There will be some variation in the results, such as how high each peak is (or whether they even appear at all) and the magnitude of variation corresponds to the amount of uncertainty at that point. Note that the uncertainty is generally not constant at all points in the KDE.

Bootstrapping can be used to calculate a confidence interval by [several methods](https://en.wikipedia.org/wiki/Bootstrapping_(statistics)#Deriving_confidence_intervals_from_the_bootstrap_distribution). The simplest one is the percentile method, which just involves comparing all the KDEs computed, and  taking their \\(\alpha/2\\) and \\((1-\alpha/2)\\) percentiles at each value of \\(x\\) to get a confidence interval (e.g., 2.5th and 97.5th for a confidence interval with 5% significance level). Note that this is implicitly assuming that the sampling errors in the KDE are normally-distributed. The bias-corrected and accelerated bootstrap method for constructing a confidence interval appears to be [more accurate and generally applicable](https://web.as.uky.edu/statistics/users/pbreheny/621/F10/notes/9-21.pdf), but unfortunately information on it is a little sparse.

![KDE of trimodal distribution with bootstrapped 95% confidence interval]({{site.baseurl}}/images/kde_primer/trimodal_kde_uncertainty.svg)

There is one awkward problem with KDEs which can create artifacts on the boundaries of the plot. Imagine a dataset where the distribution has some natural limits; in the case of exam grades, all the data would fall inside \\([0\\%, 100\\%]\\), and it would be nonsensical for there to be data outside of that range. But the kernel function doesn't know that, which leads to two possible problems. Firstly, the density will be underestimated at the boundary. Even if there is a peak at \\(x=100\\%\\) in the raw data, the density will peak slightly earlier (depending on the bandwidth) and start to drop off, since there is a sudden absence of datapoints on the other side of the boundary. Secondly, the density will be non-zero past the 100% mark, which is nonsense in this example.

![KDE of marks showing artifacts near boundaries]({{site.baseurl}}/images/kde_primer/marks_kde_bndry.svg)

Several corrections for this artifact have been developed, but they have their own pitfalls (for instance, they may result in areas of negative density). Furthermore, they are not available in ready-made form in many libraries, so in keeping with the theme of low-effort results I will just treat them as a caveat to be aware of. However, if you need them you can Google the terms `boundary correction kernel density estimation`.

If you want to create your own KDEs, you may have to write some code, but there are plenty of libraries that provide easy functions for plotting KDEs. In Python, [Seaborn](https://seaborn.pydata.org/generated/seaborn.kdeplot.html) and [StatsModels](http://www.statsmodels.org/devel/examples/notebooks/generated/kernel_density.html) are good options. In R, [the standard library](https://www.rdocumentation.org/packages/stats/versions/3.4.1/topics/density) and [ggplot2](http://ggplot2.tidyverse.org/reference/geom_density.html) are commonly used. And if you can't find a library for your language of choice, you can always write your own - I did so for some of the plots in this article (you can see my code [here](https://github.com/metavee/kde-primer-plots)), and it wasn't too involved.

KDEs are not the best choice for every scenario. Notably, you can't easily use them to count where the original datapoints fall, and they somewhat obscure the original data - for these a quantile plot of the data vs. their percentiles may be more helpful. And if you are preparing a graph for an audience who is entirely unfamiliar with KDEs, a histogram may be more appropriate. Finally, KDEs are empirical and not mechanistic: if you have an existing model to explain the data (e.g., if you're highly confident that the underlying distribution is a bimodal Gaussian of some sort), a KDE cannot be used to estimate your model parameters.

Nevertheless, with very little effort, KDEs outperform histograms in a variety of scenarios. Now that I know about them, I'm a little shocked that they were never mentioned in any of my engineering courses (which, for the record, included plenty of topics that involved statistical distributions). So try playing around a bit with KDEs and be sure to spread the word.

Happy plotting.

# Bonus: Quantile plots

There is one other distribution plot that bears mentioning as a further alternative: the quantile plot. This is simply a scatter plot of the values of the data vs. the corresponding percentiles or ["quantiles"](https://en.wikipedia.org/wiki/Quantile_function). Unlike the histogram and the KDE, the points are directly plotted without any sort of model or parameters being imposed. See how the quantile plot compares with the KDE for the trimodal distribution from earlier, **noting the swapped axes**:

![Quantile plot of trimodal distribution]({{site.baseurl}}/images/kde_primer/trimodal_quantile.svg)
![KDE of trimodal distribution]({{site.baseurl}}/images/kde_primer/trimodal_kde.svg)


It takes a bit of practice to get comfortable interpreting quantile plots, but all the information is there: in short, plateaus in the quantile plot correspond to peaks in the distribution, and steep cliffs to valleys. If it helps to understand it mathematically, you can think of it as the inverse of the cumulative distribution function. As another example, see the distribution of marks from earlier:

![Quantile plot of marks]({{site.baseurl}}/images/kde_primer/marks_quantile.svg)
![KDE of marks]({{site.baseurl}}/images/kde_primer/marks_kde.svg)

Since there is no parameter for bin position or bandwidth, no fiddling needs to be done to accurately portray the data. And the quantile plot functions remarkably well even with small numbers of datapoints.

You can even use quantiles to compare two distributions, as in a [Q-Q plot](https://en.wikipedia.org/wiki/Q%E2%80%93Q_plot). But that's an exercise left for the reader. It's just one more plot that's worth knowing about.
