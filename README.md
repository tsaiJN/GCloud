# GCloud

[2015.12.10] integration_update.py fix the numerical problem occurs in integration.py which is caused by cannot-represent problem of floating point number 0.1 in python.

# WEB DEVELOPMENT

I didn't actually use Django though, I instead write an html with javascript which pretty much satisfy all the requirement except actually create a back end.
you may access the webpage by the following link:
http://www.csie.ntu.edu.tw/~b01902004/GCloud/pure_html.html

# THE LARGEST PRIME FACTORS

The intuition of the code is simple and clear, do the factorization step by step, from small factors to large factors so that prime factors will always been extracted.

# MULTIPLES OF 3 AND 5

The intuition is again simple and clear. First add up all factors of 3, then factors of 5, and simple substract factors of 15 to get the final result.

# COMBINATION

The first and naive solution is by recursion (recursive_comb in combination.py). However, It would cost a huge branch of computing structure O(2^(logn)) till it reach the stop criteria and thus slow and resource consumming.

The second and efficient solution is by dynamic programming (DP_comb in combination.py). I use a bottom-up approach for efficiency and the time and space complexity are O(n^2)

# INTERGRATION

Where we put the line "intercept += step" would matters alot. if we put it at line 10, it would result in the version of integration approximation as shown in the middle plot (upper bound approximation). If we put in at line 13, it would result in the lower bound version of integration approximation.
